---
title: "Data Model"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, fundamentals]
---

# Data Model

**Data model** 是描述数据如何组织、存储和查询的抽象框架。它不仅是软件实现问题，还会深刻影响开发者如何思考待解决的问题。

## 分层抽象

应用软件通常由多层 data model 堆叠而成：

1. 应用层：用对象、数据结构、API 表示现实世界实体。
2. 通用 data model：如 JSON/XML documents、relational tables、graph vertices/edges。
3. 存储层：数据库把 documents、relations、graphs 编码为内存/磁盘/网络字节。
4. 硬件层：字节最终用电、光、磁信号表示。

每一层都为上层隐藏下层的实现细节。

## 常见 data models

- [[relational-model]]：tables、rows、SQL。
- [[document-model]]：JSON/BSON 文档，tree-shaped 数据。
- [[graph-data-model]]：vertices 和 edges，适合复杂关系。
- [[dataframe]]：面向分析和 ML 的表式抽象。
- [[event-sourcing]]：以不可变 event log 作为真相源。

## 为什么重要

不同的 data model 对同一种数据的表达能力差异很大。有些查询在一种模型里很自然，在另一种模型里却很别扭。选择合适的 model 是 system design 的核心决策之一。

## 相关

- [[query-language]] — 与 data model 配套的查询接口
- [[abstraction]] — data model 是屏蔽复杂度的关键 abstraction
- [[chapter-03]] — 本章详细比较了主要 data models
