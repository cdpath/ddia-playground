---
title: "Cypher"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, query-languages, graph]
---

# Cypher

**Cypher** 是用于 property graph 的 declarative query language，最初为 [[neo4j]] 设计，后来发展为 openCypher 开放标准。

## 语法特点

用箭头符号表达 vertex 和 edge 之间的关系：

```cypher
(idaho) -[:WITHIN]-> (usa)
```

## 例子：查找从美国移居欧洲的人

```cypher
MATCH
  (person) -[:BORN_IN]->  () -[:WITHIN*0..]-> (:Location {name:'United States'}),
  (person) -[:LIVES_IN]-> () -[:WITHIN*0..]-> (:Location {name:'Europe'})
RETURN person.name
```

## 实现

- [[neo4j]]
- [[memgraph]]
- [[kuzudb]]
- [[amazon-neptune]]
- Apache AGE

## 相关

- [[property-graph]]
- [[graph-data-model]]
- [[declarative-query-language]]
- [[chapter-03]]
