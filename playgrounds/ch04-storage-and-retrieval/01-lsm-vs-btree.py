# %% [markdown]
"""
# LSM-Tree vs B-Tree: 存储引擎的读写权衡

**对应概念**：[storage-engine](../../wiki/concepts/storage-engine.md)、[lsm-tree](../../wiki/concepts/lsm-tree.md)、[b-tree](../../wiki/concepts/b-tree.md)、[write-amplification](../../wiki/concepts/write-amplification.md)、[read-amplification](../../wiki/concepts/read-amplification.md)

**来源**：[Chapter 4 — Storage and Retrieval](../../wiki/sources/chapter-04.md)

**学习目标**：

- 理解 LSM-tree 与 B-tree 在写入、读取、写放大、读放大上的核心差异。
- 通过简化模拟观察两种存储引擎在不同 workload 下的 I/O 行为。
- 体会为什么 LSM-tree 常被称为 write-optimized，而 B-tree 常被称为 read-optimized。

> 本 notebook 是 **可执行示意图**，不是生产 benchmark。它抽象了真实的磁盘、缓存、并发、压缩等因素，只保留两种结构最核心的机制差异。
"""
# %% [markdown]
"""
## 书中的例子

*Designing Data-Intensive Applications* 第 4 章对比了 OLTP 存储引擎的两大流派：

> **Log-structured 存储引擎**（如 LSM-tree）只追加、不修改旧文件，通过后台 compaction 回收空间，通常更适合写密集型 workload。
> **Update-in-place 存储引擎**（如 B-tree）以固定大小的 page 原地更新，配合 WAL 保证崩溃安全，通常读性能更可预测。

本章还指出，衡量存储引擎时常见指标包括：
- **Write amplification**：一次应用写入触发多少底层 I/O 字节。
- **Read amplification**：一次点查需要读取多少 page/segment。
- **Sequential vs random writes**：顺序写与随机写在磁盘/SSD 上的性能差异。

本 notebook 用 Python 模拟两个极简的 key-value 存储引擎，并比较它们在相同 workload 下的行为。
"""
# %%
import bisect
import random
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

# 可调整参数，重新运行下方单元格即可观察变化
N_WRITES = 5_000          # 写入 key 总数
N_READS = 500             # 点查次数
VALUE_SIZE = 32           # 每条 value 的字节数（key 也近似按此估算）
PAGE_SIZE = 4 * 1024      # B-tree page 大小（字节）
LSM_MEMTABLE_LIMIT = 200  # LSM memtable 条目数上限
LSM_MAX_SEGMENTS = 4      # 触发 compaction 的 segment 数量
B_TREE_CAPACITY = 128     # 每个 B-tree node 最多容纳的 key 数
RANDOM_SEED = 42

random.seed(RANDOM_SEED)
# %%
@dataclass
class Metrics:
    writes: int = 0           # 写 I/O 次数
    reads: int = 0            # 读 I/O 次数
    reads_on_get: int = 0     # 仅点查产生的读 I/O 次数
    bytes_written: int = 0
    bytes_read: int = 0
    flushes: int = 0
    compactions: int = 0
    splits: int = 0


class SimpleLSM:
    """
    极简 LSM-tree 模拟：
    - 写入先进入内存 memtable；满后 flush 为不可变 segment。
    - segment 数量达到阈值后，后台 compaction 合并所有 segment。
    - 读取按 memtable -> 新 segment -> 老 segment 的顺序查找。
    """
    def __init__(self,
                 memtable_limit: int = 100,
                 max_segments_before_compact: int = 4,
                 bloom_filter: bool = False,
                 entry_size: int = 32):
        self.memtable: Dict[str, str] = {}
        self.memtable_limit = memtable_limit
        self.segments: List[Dict[str, str]] = []        # 新 segment 在前
        self.segment_filters: List[set] = []            # 每个 segment 的 key 集合，模拟 Bloom filter
        self.max_segments = max_segments_before_compact
        self.bloom_filter = bloom_filter
        self.entry_size = entry_size
        self.metrics = Metrics()

    def put(self, key: str, value: str):
        # WAL：每条 mutation 先追加日志
        self.metrics.writes += 1
        self.metrics.bytes_written += self.entry_size
        self.memtable[key] = value
        if len(self.memtable) >= self.memtable_limit:
            self._flush()
        if len(self.segments) >= self.max_segments:
            self._compact()

    def _flush(self):
        if not self.memtable:
            return
        segment = dict(sorted(self.memtable.items()))
        self.segments.insert(0, segment)
        self.segment_filters.insert(0, set(segment.keys()))
        self.metrics.flushes += 1
        self.metrics.writes += 1
        self.metrics.bytes_written += len(segment) * self.entry_size
        self.memtable.clear()

    def _compact(self):
        if not self.segments:
            return
        # 从老到新合并，保留每个 key 的最新值
        merged: Dict[str, str] = {}
        total_read = 0
        for seg in reversed(self.segments):
            total_read += len(seg) * self.entry_size
            merged.update(seg)
        merged = dict(sorted(merged.items()))
        self.metrics.compactions += 1
        self.metrics.reads += len(self.segments)
        self.metrics.bytes_read += total_read
        self.metrics.writes += 1
        self.metrics.bytes_written += len(merged) * self.entry_size
        self.segments = [merged]
        self.segment_filters = [set(merged.keys())]

    def get(self, key: str) -> Optional[str]:
        if key in self.memtable:
            return self.memtable[key]
        for seg, filt in zip(self.segments, self.segment_filters):
            if self.bloom_filter and key not in filt:
                continue
            self.metrics.reads += 1
            self.metrics.reads_on_get += 1
            self.metrics.bytes_read += self.entry_size
            if key in seg:
                return seg[key]
        return None

    def metrics_summary(self, n_writes: int, n_reads: int) -> dict:
        user_bytes = n_writes * self.entry_size
        return {
            'writes': self.metrics.writes,
            'reads': self.metrics.reads,
            'flushes': self.metrics.flushes,
            'compactions': self.metrics.compactions,
            'bytes_written': self.metrics.bytes_written,
            'bytes_read': self.metrics.bytes_read,
            'write_amplification': self.metrics.bytes_written / user_bytes if user_bytes else 0,
            'avg_reads_per_lookup': self.metrics.reads_on_get / n_reads if n_reads else 0,
        }


class BTreeNode:
    def __init__(self, leaf: bool = False):
        self.leaf = leaf
        # internal node 存 (key, '') 作为 separator；leaf 存 (key, value)
        self.keys: List[Tuple[str, str]] = []
        self.children: List['BTreeNode'] = []


class SimpleBTree:
    """
    极简 B+ tree 模拟：
    - 固定大小的 page（node），key 按顺序存放。
    - page 满时分裂，median key 提升到父节点作为 separator。
    - 每次 put 写 WAL；查找/插入路径上的每个 page 都计一次读。
    """
    def __init__(self, page_capacity: int = 16, page_size: int = 4096, entry_size: int = 32):
        self.root = BTreeNode(leaf=True)
        self.page_capacity = page_capacity
        self.page_size = page_size
        self.entry_size = entry_size
        self.metrics = Metrics()

    def _sep(self, key: str) -> Tuple[str, str]:
        return (key, '')

    def get(self, key: str) -> Optional[str]:
        node = self.root
        while True:
            self.metrics.reads += 1
            self.metrics.reads_on_get += 1
            self.metrics.bytes_read += self.page_size
            if node.leaf:
                idx = bisect.bisect_left(node.keys, (key, ''))
                if idx < len(node.keys) and node.keys[idx][0] == key:
                    return node.keys[idx][1]
                return None
            idx = bisect.bisect_right(node.keys, self._sep(key))
            node = node.children[idx]

    def put(self, key: str, value: str):
        # WAL
        self.metrics.writes += 1
        self.metrics.bytes_written += self.entry_size
        self.metrics.reads += 1
        self.metrics.bytes_read += self.page_size
        if len(self.root.keys) >= self.page_capacity:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node: BTreeNode, key: str, value: str):
        if node.leaf:
            idx = bisect.bisect_left(node.keys, (key, ''))
            if idx < len(node.keys) and node.keys[idx][0] == key:
                node.keys[idx] = (key, value)
            else:
                node.keys.insert(idx, (key, value))
            self.metrics.writes += 1
            self.metrics.bytes_written += self.page_size
            return
        idx = bisect.bisect_right(node.keys, self._sep(key))
        child = node.children[idx]
        self.metrics.reads += 1
        self.metrics.bytes_read += self.page_size
        if len(child.keys) >= self.page_capacity:
            self._split_child(node, idx)
            if key >= node.keys[idx][0]:
                idx += 1
        self._insert_non_full(node.children[idx], key, value)

    def _split_child(self, parent: BTreeNode, i: int):
        full = parent.children[i]
        mid = len(full.keys) // 2
        new_node = BTreeNode(leaf=full.leaf)
        if full.leaf:
            new_node.keys = full.keys[mid:]
            median_key = self._sep(full.keys[mid][0])
            full.keys = full.keys[:mid]
        else:
            new_node.keys = full.keys[mid + 1:]
            new_node.children = full.children[mid + 1:]
            full.children = full.children[:mid + 1]
            median_key = full.keys[mid]
            full.keys = full.keys[:mid]
        parent.keys.insert(i, median_key)
        parent.children.insert(i + 1, new_node)
        self.metrics.splits += 1
        # 分裂会写入被拆分的 page、新 page 和父 page
        self.metrics.writes += 3
        self.metrics.bytes_written += 3 * self.page_size

    def metrics_summary(self, n_writes: int, n_reads: int) -> dict:
        user_bytes = n_writes * self.entry_size
        return {
            'writes': self.metrics.writes,
            'reads': self.metrics.reads,
            'splits': self.metrics.splits,
            'bytes_written': self.metrics.bytes_written,
            'bytes_read': self.metrics.bytes_read,
            'write_amplification': self.metrics.bytes_written / user_bytes if user_bytes else 0,
            'avg_reads_per_lookup': self.metrics.reads_on_get / n_reads if n_reads else 0,
        }
# %%
def run_workload(store, keys: List[str], values: List[str], write_order: List[int],
                 read_keys: List[str]) -> None:
    """对同一个 store 执行写入 + 点查，只让 store 的 metrics 累积。"""
    for i in write_order:
        store.put(keys[i], values[i])
    for k in read_keys:
        assert store.get(k) is not None, f"key {k} not found"


def print_comparison(lsm_summary: dict, btree_summary: dict):
    print(f"{'Metric':<28} {'LSM-tree':>14} {'B-tree':>14}")
    print("-" * 58)
    for metric in ['writes', 'reads', 'bytes_written', 'bytes_read',
                   'write_amplification', 'avg_reads_per_lookup']:
        l = lsm_summary[metric]
        b = btree_summary[metric]
        if isinstance(l, float):
            print(f"{metric:<28} {l:>14.2f} {b:>14.2f}")
        else:
            print(f"{metric:<28} {l:>14,} {b:>14,}")
    print(f"\n{'Extra':<28} {'flushes':>14} {'splits':>14}")
    print(f"{'':<28} {lsm_summary.get('flushes', 0):>14,} {btree_summary.get('splits', 0):>14,}")
    print(f"{'':<28} {'compactions':>14} {'':>14}")
    print(f"{'':<28} {lsm_summary.get('compactions', 0):>14,} {'':>14}")
# %% [markdown]
"""
## 写入密集型 workload：随机写入 N 个 key，然后随机点查

下面生成 N 个不重复的 key，随机顺序写入两个 store，再随机读取其中一部分。观察写入放大和读取放大。
"""
# %%
keys = [f"k{i:06d}" for i in range(N_WRITES)]
values = [f"v{i:010d}" for i in range(N_WRITES)]

write_order = list(range(N_WRITES))
random.shuffle(write_order)

read_keys = [keys[i] for i in random.sample(range(N_WRITES), N_READS)]

lsm = SimpleLSM(memtable_limit=LSM_MEMTABLE_LIMIT,
                max_segments_before_compact=LSM_MAX_SEGMENTS,
                bloom_filter=False,
                entry_size=VALUE_SIZE)
btree = SimpleBTree(page_capacity=B_TREE_CAPACITY,
                    page_size=PAGE_SIZE,
                    entry_size=VALUE_SIZE)

run_workload(lsm, keys, values, write_order, read_keys)
run_workload(btree, keys, values, write_order, read_keys)

lsm_summary = lsm.metrics_summary(N_WRITES, N_READS)
btree_summary = btree.metrics_summary(N_WRITES, N_READS)
print_comparison(lsm_summary, btree_summary)
# %% [markdown]
"""
### 结果通常会长这样

- **LSM-tree**：写入次数/字节较少（主要是顺序 segment 写），但点查需要检查多个 segment，读放大高。
- **B-tree**：每次 put 都要写 WAL + 更新 page，page split 时写放大明显；但点查只需要走树高（通常 2~4 个 page），读放大低。

> 具体数值取决于上面的参数。你可以把 `N_WRITES`、`PAGE_SIZE`、`LSM_MEMTABLE_LIMIT` 等改大改小，重新运行观察变化。
"""
# %% [markdown]
"""
## 规模化：数据量增长时的写放大与读放大

保持其他参数不变，只改变写入 key 的数量，观察两种结构的 I/O 趋势。
"""
# %%
SIZES = [500, 1_000, 2_000, 5_000, 10_000]
READ_FRACTION = 0.1  # 每个 workload 读取 10% 的 key

print(f"{'N':>8} | {'LSM writes':>12} | {'B-tree writes':>14} | {'LSM read/lookup':>16} | {'B-tree read/lookup':>18} | {'LSM W.A.':>10} | {'B-tree W.A.':>12}")
print("-" * 105)

for n in SIZES:
    keys_n = [f"k{i:06d}" for i in range(n)]
    vals_n = [f"v{i:010d}" for i in range(n)]
    order = list(range(n))
    random.shuffle(order)
    reads = int(n * READ_FRACTION)
    read_keys_n = [keys_n[i] for i in random.sample(range(n), reads)]

    l = SimpleLSM(memtable_limit=max(50, n // 20),
                  max_segments_before_compact=4,
                  bloom_filter=False,
                  entry_size=VALUE_SIZE)
    b = SimpleBTree(page_capacity=B_TREE_CAPACITY,
                    page_size=PAGE_SIZE,
                    entry_size=VALUE_SIZE)
    run_workload(l, keys_n, vals_n, order, read_keys_n)
    run_workload(b, keys_n, vals_n, order, read_keys_n)
    ls = l.metrics_summary(n, reads)
    bs = b.metrics_summary(n, reads)
    print(f"{n:>8} | {ls['writes']:>12,} | {bs['writes']:>14,} | {ls['avg_reads_per_lookup']:>16.2f} | {bs['avg_reads_per_lookup']:>18.2f} | {ls['write_amplification']:>10.2f} | {bs['write_amplification']:>12.2f}")
# %% [markdown]
"""
## Bloom filter 的作用

LSM-tree 读放大最坏的场景是查一个不存在的 key：必须检查所有 segment。真实系统用 Bloom filter 跳过不可能包含该 key 的 segment。下面开启 Bloom filter 后观察读 I/O 变化。
"""
# %%
N = 2_000
keys_b = [f"k{i:06d}" for i in range(N)]
vals_b = [f"v{i:010d}" for i in range(N)]
order_b = list(range(N))
random.shuffle(order_b)

# 查不存在的 key
missing_keys = [f"missing_{i:06d}" for i in range(500)]

# 故意不 compaction，产生大量 segment，才能让 Bloom filter 的效果显现
for use_bloom in [False, True]:
    store = SimpleLSM(memtable_limit=100,
                      max_segments_before_compact=100,  # 本次不触发 compaction
                      bloom_filter=use_bloom,
                      entry_size=VALUE_SIZE)
    for i in order_b:
        store.put(keys_b[i], vals_b[i])
    print(f"After writes: {len(store.segments)} segments")
    for k in missing_keys:
        assert store.get(k) is None
    s = store.metrics_summary(N, len(missing_keys))
    print(f"Bloom filter={use_bloom!s:<5} | reads={s['reads']:>6,} | avg reads/lookup={s['avg_reads_per_lookup']:>6.2f}")
    print()
# %% [markdown]
"""
## 本 demo 的诚实声明

### 它展示了什么

- LSM-tree **只追加、后台合并**的基本机制，以及 segment 数量对读放大的影响。
- B-tree **page 分裂、原地更新**的基本机制，以及 page split 对写放大的影响。
- Write amplification 与 read amplification 的量化思路。
- Bloom filter 如何降低 LSM-tree 的读放大。

### 它没有展示什么

- **真实磁盘 I/O**：本模拟只计数 page/segment 读写，未建模寻道、 rotational latency、SSD GC、文件系统缓存等。
- **压缩、并发、缓存、MVCC**：这些都是真实存储引擎的核心，但被简化掉了。
- **精确的 LSM compaction 策略**：size-tiered / leveled compaction 的复杂 trade-off 未被完整模拟。
- **生产级 B-tree**：真实 B-tree 还有 prefix compression、delete/merge、copy-on-write 等细节。

因此，本 notebook 是一个**可执行的概念模型**，帮助你建立直觉，而不是用来 tuning 真实数据库。
"""
# %%
# 自检：确保两种结构都能正确存储和检索所有 key
TEST_N = 1_000
ks = [f"k{i:06d}" for i in range(TEST_N)]
vs = [f"v{i:010d}" for i in range(TEST_N)]
order = list(range(TEST_N))
random.shuffle(order)

lsm_test = SimpleLSM(memtable_limit=100, max_segments_before_compact=4, entry_size=32)
btree_test = SimpleBTree(page_capacity=64, page_size=4096, entry_size=32)

for i in order:
    lsm_test.put(ks[i], vs[i])
    btree_test.put(ks[i], vs[i])

for k in ks:
    assert lsm_test.get(k) is not None, f"LSM missing {k}"
    assert btree_test.get(k) is not None, f"B-tree missing {k}"

print("✅ 自检通过：LSM-tree 与 B-tree 都能正确返回所有已写入的 key。")
# %% [markdown]
"""
## 练习

1. 把 `LSM_MEMTABLE_LIMIT` 调大或调小，观察 flush 次数和读放大如何变化。
2. 把 `B_TREE_CAPACITY` 调大，观察 B-tree 的 splits 次数和读放大如何变化。
3. 改为顺序写入（`write_order = list(range(N_WRITES))`），比较两种结构的写放大差异。
4. 尝试实现一个简单的 range query：分别用 LSM 和 B-tree 扫描 `[k000100, k000200]` 之间的 key，统计需要读取多少 segment/page。
5. 思考：为什么真实系统里，LSM-tree 更适合写日志型 workload，而 B-tree 更适合需要稳定延迟的 OLTP 点查？
"""