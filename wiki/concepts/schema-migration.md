---
title: "Schema Migration"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-modeling]
---

# Schema Migration

**Schema migration** 是在不中断服务的情况下修改数据库 schema 的过程，例如添加列、修改数据类型、重命名表等。

## 关系型数据库中的挑战

- 大表上的 `ALTER TABLE` 可能需要重写整张表，耗时很长。
- `UPDATE` 全表来填充新列同样可能很慢。
- 需要避免长时间锁表导致应用不可用。

## 常用工具

- `pt-online-schema-change`（Percona Toolkit）
- `gh-ost`（GitHub 的 MySQL online schema migration 工具）
- `pg-osc`、`pgroll`（PostgreSQL）

## 与 document model 的对比

Document database 通常 schema-on-read，新字段可以随文档直接写入，老文档由读取代码兼容处理。但这只是把 schema 管理的责任从数据库转移到了应用代码。

## 相关

- [[schema-flexibility]]
- [[relational-model]]
- [[document-model]]
- [[chapter-03]]
