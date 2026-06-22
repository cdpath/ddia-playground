---
title: "Row-Oriented Storage"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, oltp]
---

# Row-Oriented Storage

**Row-oriented storage** 是一种把表中同一行的所有列值连续存放的存储布局。大多数 OLTP 数据库和文档数据库采用这种布局。

## 说明

在行式存储中，读取一行数据时通常只需一次顺序 I/O，因为该行的所有字段在磁盘上相邻。这非常适合 OLTP 场景：一次事务通常只读写少量完整记录。

但对于分析查询（如扫描上亿行只取 3 列），行式存储会把大量不需要的列也加载到内存中，造成 I/O 浪费。

## 典型系统

- 关系型 OLTP 数据库：[[postgresql]]、[[mysql]]、[[sql-server]]。
- 文档数据库：[[mongodb]]、Couchbase。
- Wide-column store：[[bigtable]]、[[hbase]]（注意：wide-column 仍是行式存储）。

## 相关

- [[column-oriented-storage]]
- [[online-transaction-processing|OLTP]]
- [[online-analytical-processing|OLAP]]
- [[storage-engine]]
- [[chapter-04]]
