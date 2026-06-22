---
title: "Property Graph"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, graph]
---

# Property Graph

**Property graph**（也称 labeled property graph）是最常见的 graph data model 之一。每个 vertex 和 edge 都带有 label 和 properties。

## Vertex 组成

- 唯一标识符
- label（描述顶点类型）
- 出边集合
- 入边集合
- properties（键值对集合）

## Edge 组成

- 唯一标识符
- tail vertex（起点）
- head vertex（终点）
- label（关系类型）
- properties（键值对集合）

## 实现

- [[neo4j]]
- [[memgraph]]
- [[kuzudb]]
- [[amazon-neptune]]
- Apache AGE（基于 PostgreSQL）

## 与 relational 的类比

Property graph 可近似用两个 relational tables 表示：一个 vertices 表，一个 edges 表，并对 tail/head 列建索引。

## 相关

- [[graph-data-model]]
- [[triple-store]]
- [[cypher]]
- [[chapter-03]]
