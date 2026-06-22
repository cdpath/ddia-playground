---
title: "Schema Flexibility"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-modeling]
---

# Schema Flexibility

**Schema flexibility** 指数据存储对数据结构变化的适应能力。极端情况下可分为两种模式：

- **Schema-on-write**：写入时数据库强制 schema，所有数据必须符合表结构。这是传统 relational database 的方式。
- **Schema-on-read**：写入时不强制 schema，结构在读取时由应用代码解释。Document database 常采用这种方式。

## Schema-on-read 的优点

- 适合 heterogeneous 数据：集合中文档结构不一致。
- 数据结构由外部系统决定，可能随时变化。
- schema evolution 可通过应用代码处理旧格式，而不必立即做大规模 migration。

## Schema-on-read 的缺点

- 读取代码需要处理历史遗留的多种格式。
- 缺少数据库层面的结构保证，容易在运行时出错。

## Schema-on-write 的优点

- 数据库强制一致性，便于文档化和协作。
- 对同构数据更高效，query optimizer 可利用已知类型。

## Schema-on-write 的缺点

- 修改 schema 在大表上可能很慢（如重写整张表）。
- 对快速变化的结构不够灵活。

## 相关

- [[document-model]]
- [[relational-model]]
- [[schema-migration]]
- [[chapter-03]]
