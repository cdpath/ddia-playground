---
title: "SingleStore"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, in-memory, oltp, olap, htap]
---

# SingleStore

**SingleStore** 是一个支持 [[hybrid-transactional-analytical-processing|HTAP]] 的分布式数据库，数据主要驻留内存。它试图同时支持高速 OLTP 和实时 OLAP。

## 特点

- 内存优先架构，声称可消除磁盘数据管理开销。
- 提供统一的 SQL 接口，但底层可能区分事务和分析存储引擎。
- 与 SAP HANA、SQL Server 等并列为 HTAP 系统。

## 相关

- [[in-memory-database]]
- [[hybrid-transactional-analytical-processing|HTAP]]
- [[online-transaction-processing|OLTP]]
- [[online-analytical-processing|OLAP]]
- [[voltdb]]
- [[chapter-04]]
