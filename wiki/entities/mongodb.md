---
title: "MongoDB"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [database, oltp, nosql, document-stores]
---

# MongoDB

MongoDB 是面向文档的 NoSQL database，也是 [[document-model]] 最具代表性的实现之一。

## 特点

- 数据以 BSON（二进制 JSON）文档存储，支持嵌套对象和数组。
- 灵活的 [[schema-flexibility|schema-on-read]]，适合 heterogeneous 数据。
- 提供 aggregation pipeline，包括 `$lookup` 实现类似 join 的功能。
- 原生支持 sharding，便于 horizontal scaling。

## 本书角色

- Chapter 1 将其作为非 relational 的 self-hosted operational/OLTP database 例子。
- Chapter 3 深入讨论其 document model、schema flexibility 和查询语言。

## 相关

- [[document-model]]
- [[json]]
- [[couchbase]]、[[rethinkdb]]
- [[mysql]]、[[postgresql]] — relational OLTP 例子
- [[chapter-03]]
