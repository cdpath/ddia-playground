---
title: "Triple Store"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, graph]
---

# Triple Store

**Triple store** 是与 property graph 基本等价的 graph data model，但使用不同的术语：所有信息以 **(subject, predicate, object)** 三元组存储。

## 三元组的含义

- **Subject**：相当于 graph 中的 vertex。
- **Predicate**：
  - 当 object 是基本类型值时，predicate 相当于 vertex 的 property name。
  - 当 object 是另一个 vertex 时，predicate 相当于 edge label。
- **Object**：基本类型值或另一个 vertex。

## 例子

```turtle
_:lucy :name "Lucy".
_:lucy :bornIn _:idaho.
_:idaho :within _:usa.
```

## 实现

- [[datomic]]
- [[allegrograph]]
- [[blazegraph]]
- [[apache-jena]]
- [[openlink-virtuoso]]
- [[amazon-neptune]]

## 相关

- [[rdf]]
- [[sparql]]
- [[semantic-web]]
- [[graph-data-model]]
- [[chapter-03]]
