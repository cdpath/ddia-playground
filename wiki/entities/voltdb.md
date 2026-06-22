---
title: "VoltDB"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, in-memory, oltp, relational]
---

# VoltDB

**VoltDB** 是一个面向 OLTP 的分布式 [[in-memory-database]]，支持 SQL 和 ACID 事务。它通过消除磁盘数据结构管理开销来追求极低延迟。

## 特点

- 数据主要驻留内存，通过复制和快照实现持久化。
- 采用分片 + 单线程执行模型来避免锁开销。
- 适合需要高吞吐、低延迟的事务处理场景。

## 相关

- [[in-memory-database]]
- [[online-transaction-processing|OLTP]]
- [[singlestore]]
- [[chapter-04]]
