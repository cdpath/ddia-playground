---
title: "RDF"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, formats, graph]
---

# RDF

**RDF（Resource Description Framework）** 是 W3C 为 Semantic Web 设计的 data model，基于 subject-predicate-object 三元组。

## 编码格式

- **Turtle**：较简洁的文本格式。
- **RDF/XML**：更冗长，用 XML 编码。
- 工具如 Apache Jena 可在不同格式间转换。

## URI 作为命名空间

RDF 的 subject、predicate、object 常以 URI 表示，例如 `<http://my-company.com/namespace#within>`。这样可以把不同来源的数据合并而避免命名冲突。

## 与 triple store 的关系

Triple store 通常基于 RDF 模型，用 [[sparql]] 查询。

## 现代应用

虽然 Semantic Web 原初愿景未完全实现，但 RDF/linked data 仍用于知识图谱、生物医学本体、Schema.org 等场景。

## 相关

- [[triple-store]]
- [[semantic-web]]
- [[sparql]]
- [[chapter-03]]
