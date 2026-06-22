---
title: "Document Model"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-models]
---

# Document Model

**Document model** 把数据表示为自包含的文档，通常以 JSON（或 XML、BSON 等）格式存储。每个文档可以包含嵌套结构和数组，天然适合 tree-shaped、one-to-many 的数据。

## 核心特征

- 数据以 document 为单位读写，而不是 rows/tables。
- 文档内部可以是嵌套对象和数组，locality 好。
- schema 通常不强制，支持 [[schema-flexibility|schema-on-read]]。
- 原生对 [[join]] 支持较弱，但现代 document DB（如 [[mongodb]]）已增加 join 能力。

## 适用场景

- 数据本身像文档或树，如个人简历、商品目录、内容管理系统。
- 读取时通常需要整个对象，且对象内关系主要是 one-to-many。
- 需要快速 schema evolution，字段不固定。

## 与 relational model 的对比

| 维度 | Document model | Relational model |
|------|----------------|------------------|
| 结构 | 嵌套文档 | tables / rows |
| 关系 | 适合 one-to-many | 适合 many-to-one / many-to-many |
| Schema | schema-on-read | schema-on-write |
| Locality | 好 | 需要 join |
| Join | 弱 | 强 |

## 相关

- [[json]]
- [[xml]]
- [[mongodb]]
- [[data-locality]]
- [[schema-flexibility]]
- [[relational-model]]
- [[chapter-03]]
