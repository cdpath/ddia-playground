# %% N+1 Query Problem
#
# 对应概念：Object-Relational Mapping (ORM)、Impedance Mismatch、Join
# 来源：Chapter 3 — Data Models and Query Languages
#
# 学习目标：
#   - 理解 ORM 中 N+1 查询问题是如何产生的
#   - 对比三种获取「评论及其作者」的策略：naive N+1、单次 JOIN、两查询 batch
#   - 观察查询次数随数据规模增长的变化
#
# 本文件可在 Zed 中按 cell 执行：把光标放在某个 # %% 块内，按 ctrl-shift-enter。
# 也支持在 Jupyter / VS Code / Spyder 等兼容 # %% 的 REPL 中运行。
#
# > 本 demo 是「可执行示意图」，不是生产 benchmark。

# %% 书中的例子
#
# 在 *Designing Data-Intensive Applications* 第 3 章中，作者讨论了 ORM 的常见问题：
#
# 当你想显示 N 条评论以及每条评论的作者时，ORM 的 lazy-loading 可能会让你不自觉地
# 写出这样的代码：先查询所有评论，然后在循环里为每条评论再查一次 users 表获取作者姓名。
# 结果总查询数是 N + 1 次。
#
# 如果手写 SQL，通常会用一次 JOIN 在单条查询中返回所有需要的数据。
#
# 本文件用 Python + SQLite 复现这个场景，并比较三种不同方案。

# %% Imports & config
# 你可以修改这些参数，重新运行下方 cell 观察变化。

import sqlite3
import time

COMMENT_COUNT = 50
NUM_USERS = 5
SIMULATED_LATENCY_S = 0.005  # 模拟每次查询的延迟（秒）

# %% Schema setup + seed data


def make_connection():
    """创建一个内存 SQLite 连接，启用外键并返回 Row 工厂。"""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def setup_schema(conn):
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE comments (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id),
            body TEXT NOT NULL
        )
    """)


def seed_data(conn, num_comments, num_users=5):
    users = [(i, f"User {i}") for i in range(1, num_users + 1)]
    comments = [
        ((i % num_users) + 1, f"Comment {i}")
        for i in range(1, num_comments + 1)
    ]
    conn.executemany("INSERT INTO users(id, name) VALUES(?, ?)", users)
    conn.executemany("INSERT INTO comments(user_id, body) VALUES(?, ?)", comments)
    conn.commit()


# 建立连接并填充数据
conn = make_connection()
setup_schema(conn)
seed_data(conn, COMMENT_COUNT, NUM_USERS)
print(f"Seeded {NUM_USERS} users and {COMMENT_COUNT} comments.")

# %% Query counter wrapper
#
# 包装 sqlite3 连接，统计 execute() 调用次数，并模拟每次查询的固定延迟。
# 这样在小规模数据下也能直观看到 N+1 与 JOIN 的时间差异。


class CountingConnection:
    def __init__(self, conn, latency=SIMULATED_LATENCY_S):
        self._conn = conn
        self._latency = latency
        self._count = 0

    def execute(self, sql, parameters=None):
        self._count += 1
        if self._latency > 0:
            time.sleep(self._latency)
        if parameters is None:
            return self._conn.execute(sql)
        return self._conn.execute(sql, parameters)

    def executemany(self, sql, parameters):
        # executemany 只计为一次数据库交互
        self._count += 1
        if self._latency > 0:
            time.sleep(self._latency)
        return self._conn.executemany(sql, parameters)

    def commit(self):
        return self._conn.commit()

    def close(self):
        return self._conn.close()

    @property
    def query_count(self):
        return self._count

    def reset_count(self):
        self._count = 0


# %% Strategy A: Naive N+1 (ORM lazy-loading 风格)
#
# 先查询所有评论，再在循环里为每条评论查询一次作者。
# 预期查询次数：1 + N


def fetch_comments_naive(conn, n=COMMENT_COUNT):
    comments = conn.execute("SELECT id, user_id, body FROM comments").fetchall()
    results = []
    for c in comments[:n]:
        user = conn.execute(
            "SELECT name FROM users WHERE id = ?",
            (c["user_id"],)
        ).fetchone()
        results.append({
            "comment_id": c["id"],
            "body": c["body"],
            "author": user["name"]
        })
    return results


# 运行并统计
conn = CountingConnection(make_connection(), latency=SIMULATED_LATENCY_S)
setup_schema(conn)
seed_data(conn, COMMENT_COUNT, NUM_USERS)
conn.reset_count()

start = time.perf_counter()
rows = fetch_comments_naive(conn, COMMENT_COUNT)
elapsed = time.perf_counter() - start

print(f"查询次数: {conn.query_count}")
print(f"耗时: {elapsed:.3f}s")
print(f"返回行数: {len(rows)}")
print("前 3 行:", rows[:3])

# %% Strategy B: Single JOIN
#
# 利用 relational model 的 JOIN，在一条查询中同时返回评论和作者姓名。
# 预期查询次数：1


def fetch_comments_join(conn, n=COMMENT_COUNT):
    rows = conn.execute("""
        SELECT c.id AS comment_id, c.body, u.name AS author
        FROM comments c
        JOIN users u ON c.user_id = u.id
        LIMIT ?
    """, (n,)).fetchall()
    return [dict(r) for r in rows]


# 运行并统计
conn = CountingConnection(make_connection(), latency=SIMULATED_LATENCY_S)
setup_schema(conn)
seed_data(conn, COMMENT_COUNT, NUM_USERS)
conn.reset_count()

start = time.perf_counter()
rows = fetch_comments_join(conn, COMMENT_COUNT)
elapsed = time.perf_counter() - start

print(f"查询次数: {conn.query_count}")
print(f"耗时: {elapsed:.3f}s")
print(f"返回行数: {len(rows)}")
print("前 3 行:", rows[:3])

# %% Strategy C: Two-query Batch + in-memory assembly
#
# 有些场景下不方便写 JOIN（例如 ORM 的批量加载、跨服务查询），可以用两条查询：
#   1. 先查评论
#   2. 收集所有涉及的 user_id，用 IN (...) 一次查出作者
#   3. 在 Python 内存中组装
# 预期查询次数：2


def fetch_comments_batch(conn, n=COMMENT_COUNT):
    comments = conn.execute(
        "SELECT id, user_id, body FROM comments LIMIT ?",
        (n,)
    ).fetchall()

    user_ids = tuple({c["user_id"] for c in comments})
    user_map = {}
    if user_ids:
        placeholders = ",".join("?" * len(user_ids))
        users = conn.execute(
            f"SELECT id, name FROM users WHERE id IN ({placeholders})",
            user_ids
        ).fetchall()
        user_map = {u["id"]: u["name"] for u in users}

    return [
        {
            "comment_id": c["id"],
            "body": c["body"],
            "author": user_map.get(c["user_id"])
        }
        for c in comments
    ]


# 运行并统计
conn = CountingConnection(make_connection(), latency=SIMULATED_LATENCY_S)
setup_schema(conn)
seed_data(conn, COMMENT_COUNT, NUM_USERS)
conn.reset_count()

start = time.perf_counter()
rows = fetch_comments_batch(conn, COMMENT_COUNT)
elapsed = time.perf_counter() - start

print(f"查询次数: {conn.query_count}")
print(f"耗时: {elapsed:.3f}s")
print(f"返回行数: {len(rows)}")
print("前 3 行:", rows[:3])

# %% 三种策略对比


def benchmark(strategy, n, latency=SIMULATED_LATENCY_S):
    conn = CountingConnection(make_connection(), latency=latency)
    setup_schema(conn)
    seed_data(conn, n, NUM_USERS)
    conn.reset_count()
    start = time.perf_counter()
    strategy(conn, n)
    elapsed = time.perf_counter() - start
    return conn.query_count, elapsed


strategies = [
    ("Naive N+1", fetch_comments_naive),
    ("Single JOIN", fetch_comments_join),
    ("Batch (2 queries)", fetch_comments_batch),
]

print(f"{'Strategy':<20} {'Queries':>10} {'Time (s)':>12}")
print("-" * 46)
for name, fn in strategies:
    q, t = benchmark(fn, COMMENT_COUNT)
    print(f"{name:<20} {q:>10} {t:>12.3f}")

# %% 规模化：查询次数随评论数增长
#
# 改变 COMMENT_COUNT，观察 naive 策略的查询次数线性增长，而 JOIN 和 batch 保持常数。

COMMENT_COUNTS = [5, 10, 25, 50, 100]

print(f"{'Comments':>10} | {'Naive N+1':>12} | {'JOIN':>8} | {'Batch':>8}")
print("-" * 50)
for n in COMMENT_COUNTS:
    naive_q, _ = benchmark(fetch_comments_naive, n, latency=0)
    join_q, _ = benchmark(fetch_comments_join, n, latency=0)
    batch_q, _ = benchmark(fetch_comments_batch, n, latency=0)
    print(f"{n:>10} | {naive_q:>12} | {join_q:>8} | {batch_q:>8}")

# %% 本 demo 的诚实声明
#
# 它展示了什么：
#   - N+1 问题的机制：循环里重复发起关联查询。
#   - 不同策略在查询次数上的数量级差异。
#   - JOIN 和 batch loading 如何把关联查询的复杂度从 O(N) 降到 O(1)。
#
# 它没有展示什么：
#   - 真实延迟：本地 SQLite 查询通常在微秒级，这里用 time.sleep 人为放大差异。
#   - 真实并发：单进程脚本无法复现连接池耗尽、锁竞争、网络排队等。
#   - ORM 细节：不同 ORM 的 eager-loading API 不同，本 demo 用原始 SQL 模拟其底层行为。
#   - 缓存与索引：真实系统里索引、缓存、查询计划都会影响实际性能。
#
# 因此，本文件是一个「可执行示意图」，不是生产环境的 benchmark。

# %% 练习
#
# 1. 把 SIMULATED_LATENCY_S 调到 0.1，重新运行上方 cell，感受 N+1 策略的耗时增长。
# 2. 在 users 表的 id 列上添加索引，观察是否改变结果（提示：主键默认已有索引）。
# 3. 把 batch 策略改成使用子查询 WHERE user_id IN (SELECT user_id FROM comments LIMIT ?)。
# 4. 尝试写一段 SQLAlchemy 风格的伪代码，说明 eager loading 如何改变行为。

# %% 自检：确保三种策略的查询次数符合预期
conn = CountingConnection(make_connection(), latency=0)

setup_schema(conn)
seed_data(conn, 10, NUM_USERS)

conn.reset_count()
fetch_comments_naive(conn, 10)
assert conn.query_count == 11, f"Expected 11 queries for naive, got {conn.query_count}"

conn.reset_count()
fetch_comments_join(conn, 10)
assert conn.query_count == 1, f"Expected 1 query for JOIN, got {conn.query_count}"

conn.reset_count()
fetch_comments_batch(conn, 10)
assert conn.query_count == 2, f"Expected 2 queries for batch, got {conn.query_count}"

print("✅ 所有自检通过：Naive=11, JOIN=1, Batch=2")
