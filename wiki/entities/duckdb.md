---
title: "DuckDB"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [database, olap, single-node, embedded, columnar]
---

# DuckDB

DuckDB 是面向 single-node 的嵌入式 analytical database。本章把它与 SQLite、KùzuDB 并列为 embedded database 例子，说明强大的 single-node database 已经能让许多 workload 保持非分布式。

## 本章角色

- [[embedded-database]] analytical database 的代表
- 采用 [[column-oriented-storage|列式存储]]，适合 OLAP 查询
- 常与 Python data science 工具链（Pandas、NumPy、Apache Arrow）配合使用

## 相关

- [[online-analytical-processing|OLAP]]
- [[column-oriented-storage]]
- [[embedded-database]]
- [[distributed-system]] — 对比：何时不必选择分布式
- [[chapter-04]]
