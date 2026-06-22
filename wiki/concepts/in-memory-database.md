---
title: "In-Memory Database"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, memory, performance]
---

# In-Memory Database

**In-memory database** 是把数据主要存放在主内存（RAM）中的数据库。由于避免了磁盘 I/O 的开销，它能提供比传统磁盘数据库更低的延迟和更高的吞吐。

## 说明

In-memory database 并非一定不持久化。常见的持久化方式包括：

- 写入 [[write-ahead-log|WAL]] 或 append-only log。
- 定期生成快照（snapshot）到磁盘。
- 把内存状态复制到其他机器。
- 使用特殊硬件（如电池供电 RAM）。

只要磁盘只用于持久化日志或快照、读取完全由内存服务，系统仍被视为 in-memory database。

## 性能优势来源

其性能优势并不完全来自“不需要读磁盘”——即使磁盘数据库，在内存足够时也可能通过 OS cache 避免磁盘读取。真正的优势来自：

- 避免把内存数据结构编码成磁盘格式。
- 可以使用更灵活、更复杂的数据结构（如 Redis 的 sets、priority queues）。
- 减少序列化/反序列化和 buffer manager 的开销。

## 典型系统

- 缓存型：[[memcached]]（弱持久化）。
- 关系型：VoltDB、SingleStore、Oracle TimesTen。
- Key-value：[[redis]]、Couchbase、RAMCloud。

## 相关

- [[embedded-database]]
- [[storage-engine]]
- [[write-ahead-log]]
- [[cache]]
- [[performance]]
- [[chapter-04]]
