---
title: "PostgreSQL"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [database, oltp, sql, document-stores, graph]
---

# PostgreSQL

PostgreSQL 是流行的开源 relational database，以可扩展性和标准兼容性著称。本书将其列为典型的 self-hosted [[online-transaction-processing|OLTP]] 系统。

## Chapter 3 角色

- 支持 JSON/JSONB 类型和内部属性索引，体现了 relational-document convergence。
- 可用 recursive common table expressions（CTE）查询 graph 数据。
- 例子中展示了用两个表（`vertices`、`edges`）建模 property graph。

## 相关

- [[sql]]
- [[relational-model]]
- [[mysql]] — 另一款广泛使用的开源 relational database
- [[duckdb]] — single-node analytical database
- [[chapter-03]]
