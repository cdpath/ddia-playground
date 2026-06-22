---
title: "PostgreSQL"
type: entity
source_count: 3
last_updated: 2026-06-22
tags: [database, oltp, sql, document-stores, graph, full-text-search]
---

# PostgreSQL

PostgreSQL 是流行的开源 relational database，以可扩展性和标准兼容性著称。本书将其列为典型的 self-hosted [[online-transaction-processing|OLTP]] 系统。

## Chapter 3 角色

- 支持 JSON/JSONB 类型和内部属性索引，体现了 relational-document convergence。
- 可用 recursive common table expressions（CTE）查询 graph 数据。
- 例子中展示了用两个表（`vertices`、`edges`）建模 property graph。

## Chapter 4 角色

- 默认使用 [[heap-file]] 组织表数据，二级索引指向 heap 中的位置（tid）。
- 默认 page 大小为 8 KiB。
- 通过 GIN 索引支持 [[full-text-search]] 和 JSON 内部属性索引。
- 通过 pgvector 扩展支持 [[vector-index]]（包括 [[hnsw]]）。
- 需要 vacuum 进程处理 [[fragmentation]] 和事务 ID 回绕。

## 相关

- [[sql]]
- [[relational-model]]
- [[heap-file]]
- [[b-tree]]
- [[full-text-search]]
- [[vector-index]]
- [[hnsw]]
- [[fragmentation]]
- [[mysql]] — 另一款广泛使用的开源 relational database
- [[duckdb]] — single-node analytical database
- [[chapter-03]]
- [[chapter-04]]
