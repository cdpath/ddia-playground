---
title: "RocksDB"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, storage-engine, lsm-tree, embedded]
---

# RocksDB

**RocksDB** 是 Facebook（现 Meta）基于 Google [[leveldb]] 开发的高性能嵌入式 [[storage-engine]]，采用 [[lsm-tree]] 架构。它被广泛应用于需要高写入吞吐的场景。

## 特点

- 基于 [[lsm-tree]]，使用 [[memtable]] + [[sstable]] + [[compaction]]。
- 支持多种 compaction 策略（size-tiered、leveled 等）。
- 在高写负载下可能因 compaction 落后而触发 [[backpressure]]。
- 被 [[cassandra]]、MyRocks 等系统用作底层存储引擎。

## 相关

- [[leveldb]]
- [[lsm-tree]]
- [[sstable]]
- [[memtable]]
- [[compaction]]
- [[embedded-database]]
- [[chapter-04]]
