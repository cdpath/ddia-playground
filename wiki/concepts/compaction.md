---
title: "Compaction"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, lsm-tree, maintenance]
---

# Compaction

**Compaction** 是 [[lsm-tree]] 等日志结构存储引擎在后台执行的合并过程：把多个 sorted 数据文件合并成新的 sorted 文件，同时丢弃被覆盖的旧值和已删除记录，回收磁盘空间。

## 说明

在 LSM-tree 中，更新和删除都是追加写，旧的 key 版本会散布在不同 segment 中。Compaction 的作用：

- 减少文件数量，降低 [[read-amplification]]。
- 回收被覆盖或删除记录占用的空间。
- 保证查询 eventually 只看到每个 key 的最新值。
- 传播 [[tombstone]]，使其最终到达最老层并被彻底清除。

## 主要策略

- **Size-tiered compaction**：较新、较小的 SSTable 合并成较老、较大的 SSTable。写吞吐高，但读放大和空间占用较大。
- **Leveled compaction**：每层 SSTable 大小固定，按 key range 分区；当某层超过阈值时，把该层的 SSTable 合并到下一层。读放大低，但写放大较高。

## 影响

- Compaction 与前台写入竞争磁盘带宽，可能触发 [[backpressure]]。
- 频繁的 compaction 会增加 [[write-amplification]] 和 SSD 磨损。
- 选择合适的 compaction 策略需要权衡读写比例、工作集大小和磁盘容量。

## 相关

- [[lsm-tree]]
- [[sstable]]
- [[memtable]]
- [[write-amplification]]
- [[read-amplification]]
- [[tombstone]]
- [[backpressure]]
- [[chapter-04]]
