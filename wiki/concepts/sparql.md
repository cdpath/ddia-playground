---
title: "SPARQL"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, query-languages, graph]
---

# SPARQL

**SPARQL**（SPARQL Protocol and RDF Query Language）是用于 [[rdf]] / [[triple-store]] 的 declarative query language。

## 语法特点

- 变量以 `?` 开头。
- 用 `/` 和 `*` 表达路径，例如 `?person :bornIn / :within* / :name "United States"`。
- 不区分 property 和 edge，统一用 predicate 表达。

## 例子

```sparql
PREFIX : <urn:example:>

SELECT ?personName WHERE {
  ?person :name ?personName.
  ?person :bornIn  / :within* / :name "United States".
  ?person :livesIn / :within* / :name "Europe".
}
```

## 实现

- [[apache-jena]]
- [[amazon-neptune]]
- AllegroGraph、Blazegraph、OpenLink Virtuoso 等。

## 相关

- [[rdf]]
- [[triple-store]]
- [[semantic-web]]
- [[cypher]]
- [[chapter-03]]
