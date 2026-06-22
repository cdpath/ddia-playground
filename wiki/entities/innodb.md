---
title: "InnoDB"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, storage-engine, b-tree, mysql]
---

# InnoDB

**InnoDB** 是 [[mysql]] 默认的 transactional [[storage-engine]]，使用 [[b-tree]] 索引和 [[write-ahead-log|WAL]] 实现崩溃恢复。

## 特点

- 主键是 [[clustered-index]]，数据行直接存储在主键索引的 leaf page 中。
- 二级索引存储主键值，查询时可能需要回表。
- 支持 ACID 事务、行级锁和外键。
- 默认 page 大小为 16 KiB。

## 相关

- [[mysql]]
- [[b-tree]]
- [[clustered-index]]
- [[secondary-index]]
- [[write-ahead-log]]
- [[storage-engine]]
- [[chapter-04]]
