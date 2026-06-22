---
title: "ScyllaDB"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, nosql, wide-column, lsm-tree, distributed]
---

# ScyllaDB

**ScyllaDB** 是用 C++ 重写的高性能 Cassandra 兼容数据库，采用 [[lsm-tree]] 存储引擎。相比 Cassandra 的 JVM 实现，ScyllaDB 旨在降低延迟并提高吞吐。

## 特点

- 与 Cassandra 兼容的协议和查询语言（CQL）。
- 基于 [[lsm-tree]]，针对现代多核服务器和 SSD 优化。
- 采用 shard-per-core 架构减少锁竞争。

## 相关

- [[cassandra]]
- [[lsm-tree]]
- [[sstable]]
- [[compaction]]
- [[wide-column-store]]
- [[chapter-04]]
