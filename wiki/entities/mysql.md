---
title: "MySQL"
type: entity
source_count: 3
last_updated: 2026-06-22
tags: [database, oltp, sql, innodb]
---

# MySQL

MySQL 是广泛使用的开源 relational database。本书将其列为常见的 self-hosted [[online-transaction-processing|OLTP]] 系统之一。

## Chapter 3 角色

- 示例中展示了 MySQL 的 `substring_index` 函数用于 schema migration。
- 现代 MySQL 也支持 JSON 类型和 JSON 查询函数，与 document model 有所融合。

## Chapter 4 角色

- 默认使用 [[innodb]] 存储引擎。
- InnoDB 的主键是 [[clustered-index]]，二级索引存储主键值。
- 默认 page 大小为 16 KiB。

## 相关

- [[sql]]
- [[relational-model]]
- [[innodb]]
- [[b-tree]]
- [[clustered-index]]
- [[postgresql]] — 另一款流行的开源 relational database
- [[mongodb]] — 文档型 database，同样被列为 self-hosted OLTP
- [[chapter-03]]
- [[chapter-04]]
