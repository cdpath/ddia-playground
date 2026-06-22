---
title: "Chapter 3. Data Models and Query Languages"
type: source
source_count: 1
last_updated: 2026-06-22
tags: [data-models, query-languages]
---

# Chapter 3. Data Models and Query Languages

本章讨论 data models 与 query languages 的选择，以及它们如何影响我们思考问题的方式。从 relational model、document model、graph model 到 event sourcing、DataFrames，本章比较了各种模型的适用场景与权衡。

## 核心观点

- 应用软件通常由多层 data model 堆叠而成；每一层隐藏下层复杂度，提供清晰接口。
- 没有绝对最好的 data model，关键看数据关系的类型和查询模式。
- **Relational model** 适合 many-to-one / many-to-many 关系，query 表达能力强，在 analytics 中占主导。
- **Document model** 适合 tree-shaped、one-to-many 数据，具有更好的 data locality，但对 join 支持较弱。
- **Graph model** 适合任意 many-to-many、需要遍历多跳关系的数据。
- **Event sourcing** 把状态变化写成不可变 event log，通过 **CQRS** 生成多个 read-optimized materialized views。
- **DataFrames / array databases** 面向 analytics、ML 和科学计算，补充了传统数据库模型。

## 主要内容

### 1. Declarative query languages

SQL、Cypher、SPARQL、Datalog 都是 **declarative query languages**：用户描述想要什么结果和转换，而不指定执行计划。数据库的 query optimizer 决定使用哪些 index 和 join 算法。这与命令式语言形成对比，使查询更简洁且更易于并行化。

### 2. Relational vs. document models

- **Relational model**：数据组织为 relations（tables）和 tuples（rows），由 Edgar Codd 于 1970 年提出 [[edgar-codd]]。
- **Object-relational mismatch**：OOP 对象与 relational tables 之间需要 **ORM**（如 [[hibernate]]、[[activerecord]]）做转换，可能产生 N+1 query problem。
- **Document model**：以 JSON 文档表示数据，适合 one-to-many（one-to-few）关系，locality 好。
- **Normalization vs. denormalization**：normalized 数据写快、查慢；denormalized 读快、写慢。Join 是 relational 的核心能力。
- **Schema flexibility**：document model 通常 **schema-on-read**；relational 是 **schema-on-write**。
- **Convergence**：relational DB 增加 JSON 支持，document DB 增加 joins 与 declarative queries。

### 3. Graph-like data models

- **Property graph**：vertices 和 edges 都带 label 和 properties，用 [[neo4j]]、[[memgraph]]、[[kuzudb]] 等实现。
- **Triple store / RDF**：subject-predicate-object，用 [[sparql]] 查询，与 Semantic Web 相关。
- **Query languages**：[[cypher]]、[[sparql]]、[[datalog]]、[[graphql]]。
- Graph 数据也可用 SQL 的 recursive CTE 查询，但语法繁琐。

### 4. Event sourcing and CQRS

- **Event sourcing**：把状态变更写成 append-only immutable event log，作为 source of truth。
- **CQRS**：将 write-optimized event log 与 read-optimized materialized views 分离。
- 优点：意图清晰、可回放重算、支持多视图、审计友好、写吞吐高。
- 缺点：外部数据确定性、GDPR 删除、副作用重放等问题需要小心处理。

### 5. DataFrames, matrices, and arrays

- **DataFrames**：[[pandas]]、[[spark|Apache Spark]]、[[dask]]、[[arcticdb]] 等支持，面向数据科学家。
- 可将关系表 pivot 成 sparse matrix，供 ML 使用。
- **Array databases**（如 [[tiledb]]）用于科学数据集。

## 相关概念

- [[data-model]]
- [[relational-model]]
- [[document-model]]
- [[graph-data-model]]
- [[declarative-query-language]]
- [[object-relational-mapping]]
- [[impedance-mismatch]]
- [[normalization]]
- [[denormalization]]
- [[join]]
- [[relationship-cardinality]]
- [[schema-flexibility]]
- [[data-locality]]
- [[data-warehouse-schema]]
- [[property-graph]]
- [[triple-store]]
- [[rdf]]
- [[semantic-web]]
- [[cypher]]
- [[sparql]]
- [[datalog]]
- [[graphql]]
- [[event-sourcing]]
- [[cqrs]]
- [[materialized-view]]
- [[derived-data-system]]
- [[dataframe]]
- [[array-database]]

## 相关实体

- [[edgar-codd]]
- [[sql]]
- [[mongodb]]
- [[couchbase]]
- [[rethinkdb]]
- [[postgresql]]
- [[mysql]]
- [[oracle]]
- [[hibernate]]
- [[activerecord]]
- [[neo4j]]
- [[memgraph]]
- [[kuzudb]]
- [[amazon-neptune]]
- [[datomic]]
- [[allegrograph]]
- [[blazegraph]]
- [[apache-jena]]
- [[openlink-virtuoso]]
- [[wikidata]]
- [[schema-org]]
- [[facebook]]
- [[linkedin]]
- [[eventstoredb]]
- [[martendb]]
- [[axon-framework]]
- [[apache-kafka]]
- [[spark]]
- [[apache-flink]]
- [[pandas]]
- [[numpy]]
- [[tiledb]]
- [[arcticdb]]
- [[dask]]
- [[cozodb]]
- [[logicblox]]
- [[genbank]]
- [[tigerbeetle]]
- [[bigtable]]
- [[spanner]]
- [[hbase]]
- [[accumulo]]

## Open threads

- 本章只讲 data model 和 query language；具体 storage engine 实现将在 [[chapter-04]] 展开。
- JSON 作为 encoding format 的问题将在 [[chapter-05]] 讨论。
- 多文档 atomic transactions、stream processing 的一致性在 [[chapter-08]]、[[chapter-10]]、[[chapter-12]] 深入。
- Full-text search 和 vector search 将在 [[chapter-04]] 的 “Full-Text Search” 中涉及。
