---
title: "Graph Data Model"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-models]
---

# Graph Data Model

**Graph data model** 用 **vertices**（节点/实体）和 **edges**（边/关系）表示数据，适合关系中存在大量 many-to-many、需要多跳遍历的场景。

## 适用场景

- 社交网络：人与人之间的关系。
- 网页图：页面之间的链接（如 PageRank）。
- 路网/铁路网：节点是路口，边是路段。
- 知识图谱：实体之间的复杂语义关系。

## 主要变体

- **Property graph**：顶点和边都有 label 和 properties。实现包括 [[neo4j]]、[[memgraph]]、[[kuzudb]]、[[amazon-neptune]]。
- **Triple store / RDF**：所有信息以 (subject, predicate, object) 三元组存储，用 [[sparql]] 查询。

## 查询方式

Graph 查询通常需要 traversing variable-length paths，可用：

- [[cypher]]
- [[sparql]]
- [[datalog]]
- SQL 的 recursive CTE（较繁琐）

## 与 relational model 的对比

Relational model 也能表示 graph（用两张表分别存 vertices 和 edges），但当关系复杂、遍历深度不定时，查询会变得非常冗长和低效。

## 相关

- [[property-graph]]
- [[triple-store]]
- [[rdf]]
- [[relationship-cardinality]]
- [[chapter-03]]
