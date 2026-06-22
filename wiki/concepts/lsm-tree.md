---
title: "Log-Structured Merge-Tree"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, index, oltp]
---

# Log-Structured Merge-Tree

**Log-Structured Merge-Tree**（**LSM-tree**）是一种[[log-structured-storage]]索引结构，由 O’Neil 等人于 1996 年提出。它通过维护一组按 key 排序、不可变的 [[sstable]] 文件，并在后台不断合并这些文件，来兼顾高写入吞吐与可接受的读取性能。

## 说明

LSM-tree 的工作流程：

1. 写入先进入内存中的有序结构 [[memtable]]（如红黑树、跳表）。
2. 当 memtable 达到一定大小后，被冻结并顺序写成一个 [[sstable]] segment 文件。
3. 读取时按从新到老的顺序查找 memtable 与各层 segment。
4. 后台运行 [[compaction]]，把多个 segment 合并成新的 segment，丢弃被覆盖或删除的记录。
5. 为了防止崩溃丢失内存数据，写入同时先追加到 [[write-ahead-log|WAL]]。

## 优点

- **写入吞吐高**：顺序写、page 覆写少，写放大通常低于 B-tree。
- **压缩友好**：排序后的数据块易于压缩，空间利用率常优于 B-tree。
- **崩溃恢复简单**：segment 文件不可变，未写完直接丢弃。

## 缺点

- **读取可能慢**：需要检查多个 segment，尤其是读取不存在的 key 或很久未更新的 key。
- **需要 Bloom filter**：用 [[bloom-filter]] 快速判断 key 是否在某个 segment 中，减少无效 I/O。
- **Compaction 可能引发延迟尖峰**：如果写入速度超过 compaction，会触发 [[backpressure]]。

## Compaction 策略

- **Size-tiered compaction**：小文件合并成大文件，写友好，但读放大和空间占用较大。
- **Leveled compaction**：每层大小固定、按 key range 切分，读友好，但写放大更高。

## 相关系统

- [[rocksdb]]、[[leveldb]]
- [[cassandra]]、[[scylladb]]、[[hbase]]
- [[lucene]]、[[elasticsearch]]、[[solr]]

## 相关

- [[sstable]]
- [[memtable]]
- [[compaction]]
- [[bloom-filter]]
- [[write-ahead-log]]
- [[storage-engine]]
- [[sequential-write]]
- [[write-amplification]]
- [[read-amplification]]
- [[chapter-04]]
