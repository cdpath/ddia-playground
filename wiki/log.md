---
title: "Wiki Log"
type: synthesis
source_count: 3
last_updated: 2026-06-22
tags: [log, history]
---

# Wiki Log

wiki 的 append-only 历史记录，包括摄入、查询和 lint。

## [2026-06-22] ingest | Chapter 3. Data Models and Query Languages

- 阅读 `raw/chapter3/03.md`
- 创建 source summary：[[chapter-03]]
- 更新 [[materialized-view]]、[[derived-data-system]]、[[cache]]、[[data-warehouse]]、[[database]]、[[online-transaction-processing|OLTP]]、[[online-analytical-processing|OLAP]]、[[abstraction]]
- 新建 concepts：[[data-model]]、[[query-language]]、[[declarative-query-language]]、[[relational-model]]、[[document-model]]、[[graph-data-model]]、[[object-relational-mapping]]、[[impedance-mismatch]]、[[normalization]]、[[denormalization]]、[[join]]、[[relationship-cardinality]]、[[schema-flexibility]]、[[schema-migration]]、[[data-locality]]、[[json]]、[[xml]]、[[data-warehouse-schema]]、[[property-graph]]、[[triple-store]]、[[rdf]]、[[semantic-web]]、[[cypher]]、[[sparql]]、[[datalog]]、[[graphql]]、[[event-sourcing]]、[[cqrs]]、[[dataframe]]、[[array-database]]、[[jsonpath]]、[[wide-column-store]]、[[full-text-search]]
- 新建 entities：[[edgar-codd]]、[[sql]]、[[couchbase]]、[[rethinkdb]]、[[oracle]]、[[hibernate]]、[[activerecord]]、[[neo4j]]、[[memgraph]]、[[kuzudb]]、[[amazon-neptune]]、[[datomic]]、[[allegrograph]]、[[blazegraph]]、[[apache-jena]]、[[openlink-virtuoso]]、[[wikidata]]、[[schema-org]]、[[facebook]]、[[linkedin]]、[[eventstoredb]]、[[martendb]]、[[axon-framework]]、[[apache-kafka]]、[[apache-flink]]、[[pandas]]、[[numpy]]、[[tiledb]]、[[arcticdb]]、[[dask]]、[[cozodb]]、[[logicblox]]、[[genbank]]、[[tigerbeetle]]、[[bigtable]]、[[spanner]]、[[hbase]]、[[accumulo]]
- 更新 entities：[[mongodb]]、[[postgresql]]、[[mysql]]、[[spark]]
- 更新 [[index]] 与本 log
- Backfill：更新 [[mongodb]] 中“文档数据模型将在后续章节更深入讨论”的 placeholder

## [2026-06-22] ingest | Chapter 2. Defining Nonfunctional Requirements

- 阅读 `raw/chapter2/02.md`
- 创建 source summary：[[chapter-02]]
- 更新 [[reliability]]、[[scalability]]、[[maintainability]]、[[cache]]、[[derived-data-system]]
- 新建 concepts：[[performance]]、[[service-level-objective]]、[[fault-tolerance]]、[[metastable-failure]]、[[shared-nothing-architecture]]、[[materialized-view]]、[[fan-out]]、[[abstraction]]、[[operability]]、[[blameless-postmortem]]
- 新建 entities：[[twitter|X / Twitter]]、[[amazon]]、[[hdrhistogram|HdrHistogram]]、[[t-digest]]、[[ddsketch|DDSketch]]
- 更新 [[index]] 与本 log

## [2026-06-22] ingest | Chapter 1. Trade-Offs in Data Systems Architecture

- 阅读 `raw/chapter1/01.md`
- 创建 source summary：[[chapter-01]]
- 从本章提取并创建 31 个 concept/entity 页面
- 在 `CLAUDE.md` 中建立 wiki schema
- 更新本 index 与 log
- 后续按用户要求将所有 Chapter 1 相关页面改写为中文，术语与缩写保持英文

创建的页面：

- Concepts：[[data-intensive-application]]、[[database]]、[[cache]]、[[search-index]]、[[stream-processing]]、[[batch-processing]]、[[operational-system]]、[[analytical-system]]、[[online-transaction-processing]]、[[online-analytical-processing]]、[[data-warehouse]]、[[data-lake]]、[[extract-transform-load]]、[[data-silo]]、[[hybrid-transactional-analytical-processing]]、[[system-of-record]]、[[derived-data-system]]、[[cloud-native]]、[[object-storage]]、[[separation-of-storage-and-compute]]、[[microservices]]、[[service-oriented-architecture]]、[[serverless]]、[[distributed-system]]、[[data-minimization]]、[[reliability]]、[[scalability]]、[[maintainability]]、[[observability]]、[[avro]]、[[parquet]]
- Entities：[[designing-data-intensive-applications]]、[[mysql]]、[[postgresql]]、[[mongodb]]、[[clickhouse]]、[[snowflake]]、[[duckdb]]、[[amazon-s3]]、[[spark]]、[[kubernetes]]
