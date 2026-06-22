---
title: "Query Language"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases]
---

# Query Language

**Query language** 是与 data model 配套的接口，用于从数据存储中读取、过滤、聚合和转换数据。

## Declarative vs. imperative

- **Declarative**：用户描述“想要什么结果”，由数据库的 query optimizer 决定如何执行。例如 [[sql]]、[[cypher]]、[[sparql]]、[[datalog]]。
- **Imperative**：用户显式写出操作步骤，如大多数编程语言（Python、Java）。

Declarative query language 通常更简洁，也更容易让数据库在内部做并行化或选择更优执行计划，而无需修改用户查询。

## 与 data model 的关系

一种 data model 往往有对应的 query language：

- Relational model → [[sql]]
- Document model → MongoDB aggregation pipeline、[[jsonpath]]、XQuery/XPath
- Property graph → [[cypher]]、GQL、Gremlin
- Triple store / RDF → [[sparql]]
- Datalog facts/rules → [[datalog]]
- API 层 → [[graphql]]

## 相关

- [[declarative-query-language]]
- [[data-model]]
- [[chapter-03]]
