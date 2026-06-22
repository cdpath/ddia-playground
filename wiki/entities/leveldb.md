---
title: "LevelDB"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, storage-engine, lsm-tree, embedded]
---

# LevelDB

**LevelDB** 是 Google 开发的嵌入式 key-value [[storage-engine]]，采用 [[lsm-tree]] 架构。它设计简洁，是许多后续 LSM 存储引擎的基础。

## 特点

- 基于 [[lsm-tree]]，使用 leveled compaction。
- 单进程访问，适合作为应用内嵌存储。
- 影响了 [[rocksdb]] 等更复杂的存储引擎。

## 相关

- [[rocksdb]]
- [[lsm-tree]]
- [[sstable]]
- [[memtable]]
- [[embedded-database]]
- [[chapter-04]]
