---
title: "Wiki Index"
type: synthesis
source_count: 4
last_updated: 2026-06-22
tags: [index, navigation]
---

# Wiki Index

本 wiki 围绕 *Designing Data-Intensive Applications* 构建，由 LLM 维护。以下是页面目录。

部分概念还配有可运行的 [Jupyter Notebook playground](../playgrounds/README.md)，方便通过代码验证书中的权衡。

## Source summaries

- [[chapter-01|Chapter 1. Trade-Offs in Data Systems Architecture]]
- [[chapter-02|Chapter 2. Defining Nonfunctional Requirements]]
- [[chapter-03|Chapter 3. Data Models and Query Languages]]
- [[chapter-04|Chapter 4. Storage and Retrieval]]

## Concepts

### 基础概念

- [[data-intensive-application]]
- [[database]]
- [[cache]]
- [[search-index]]
- [[stream-processing]]
- [[batch-processing]]
- [[system-of-record]]
- [[derived-data-system]]
- [[reliability]]
- [[scalability]]
- [[maintainability]]
- [[data-model]]
- [[query-language]]
- [[declarative-query-language]]
- [[query-engine]]

### 数据模型

- [[relational-model]]
- [[document-model]]
- [[graph-data-model]]
- [[json]]
- [[xml]]
- [[dataframe]]
- [[array-database]]
- [[wide-column-store]]

### 数据建模与 schema

- [[normalization]]
- [[denormalization]]
- [[join]]
- [[relationship-cardinality]]
- [[schema-flexibility]]
- [[schema-migration]]
- [[data-locality]]
- [[impedance-mismatch]]
- [[object-relational-mapping]]

### 存储引擎与索引

- [[storage-engine]]
- [[index]]
- [[primary-index]]
- [[secondary-index]]
- [[clustered-index]]
- [[heap-file]]
- [[covering-index]]
- [[b-tree]]
- [[lsm-tree]]
- [[sstable]]
- [[memtable]]
- [[compaction]]
- [[bloom-filter]]
- [[write-ahead-log]]
- [[tombstone]]
- [[log-structured-storage]]
- [[in-memory-database]]
- [[embedded-database]]
- [[fragmentation]]
- [[backpressure]]
- [[write-amplification]]
- [[read-amplification]]
- [[sequential-write]]
- [[random-write]]
- [[garbage-collection-ssd|SSD garbage collection]]

### 分析存储与执行

- [[column-oriented-storage]]
- [[row-oriented-storage]]
- [[column-compression]]
- [[bitmap-index]]
- [[run-length-encoding]]
- [[roaring-bitmaps]]
- [[query-compilation]]
- [[vectorized-processing]]
- [[materialized-view]]
- [[data-cube]]

### 多维、全文与向量索引

- [[multidimensional-index]]
- [[r-tree]]
- [[space-filling-curve]]
- [[full-text-search]]
- [[inverted-index]]
- [[postings-list]]
- [[n-gram]]
- [[semantic-search]]
- [[vector-embedding]]
- [[vector-index]]
- [[flat-index]]
- [[ivf]]
- [[hnsw]]

### 数据湖与开放格式

- [[parquet]]
- [[orc]]
- [[lance]]
- [[nimble]]
- [[apache-arrow]]
- [[apache-iceberg]]
- [[delta-lake]]
- [[table-format]]
- [[data-catalog]]

### 非功能需求与性能

- [[performance]]
- [[service-level-objective|SLO / SLA]]
- [[fan-out]]

### 可靠性与容错

- [[fault-tolerance]]
- [[metastable-failure]]
- [[blameless-postmortem]]

### 可维护性

- [[operability]]
- [[abstraction]]

### Operational 与 Analytical

- [[operational-system]]
- [[analytical-system]]
- [[online-transaction-processing|OLTP]]
- [[online-analytical-processing|OLAP]]
- [[hybrid-transactional-analytical-processing|HTAP]]
- [[data-warehouse]]
- [[data-warehouse-schema]]
- [[data-lake]]
- [[extract-transform-load|ETL]]
- [[data-silo]]

### Graph 与 Semantic Web

- [[property-graph]]
- [[triple-store]]
- [[rdf]]
- [[semantic-web]]

### 查询语言

- [[sql]]
- [[cypher]]
- [[sparql]]
- [[datalog]]
- [[graphql]]
- [[jsonpath]]

### Event Sourcing 与 CQRS

- [[event-sourcing]]
- [[cqrs]]

### 云与分布式架构

- [[cloud-native]]
- [[object-storage]]
- [[separation-of-storage-and-compute]]
- [[shared-nothing-architecture]]
- [[microservices]]
- [[service-oriented-architecture|SOA]]
- [[serverless]]
- [[distributed-system]]
- [[observability]]

### 隐私与社会

- [[data-minimization]]

## Entities

### 人物

- [[edgar-codd|Edgar F. Codd]]

### 书籍

- [[designing-data-intensive-applications]]

### 数据库与存储

- [[mysql]]
- [[postgresql]]
- [[mongodb]]
- [[couchbase]]
- [[rethinkdb]]
- [[oracle]]
- [[neo4j]]
- [[memgraph]]
- [[kuzudb]]
- [[amazon-neptune]]
- [[datomic]]
- [[allegrograph]]
- [[blazegraph]]
- [[apache-jena]]
- [[openlink-virtuoso]]
- [[eventstoredb]]
- [[martendb]]
- [[bigtable]]
- [[spanner]]
- [[hbase]]
- [[accumulo]]
- [[tiledb]]
- [[arcticdb]]
- [[genbank]]
- [[tigerbeetle]]
- [[clickhouse]]
- [[snowflake]]
- [[duckdb]]
- [[amazon-s3]]
- [[rocksdb]]
- [[leveldb]]
- [[sqlite]]
- [[lmdb]]
- [[cassandra]]
- [[scylladb]]
- [[voltdb]]
- [[singlestore]]
- [[oracle-timesten]]
- [[ramcloud]]
- [[redis]]
- [[memcached]]
- [[innodb]]
- [[sql-server]]
- [[vertica]]
- [[teradata]]
- [[sap-hana]]
- [[apache-pinot]]
- [[apache-druid]]
- [[bigquery]]
- [[amazon-redshift]]
- [[influxdb]]
- [[timescaledb]]
- [[postgis]]

### 计算与编排

- [[spark]]
- [[apache-flink]]
- [[dask]]
- [[kubernetes]]
- [[apache-hive]]
- [[trino]]
- [[presto]]
- [[apache-datafusion]]

### 公司与平台

- [[twitter|X / Twitter]]
- [[amazon]]
- [[facebook|Facebook / Meta]]
- [[linkedin]]
- [[wikidata]]
- [[schema-org]]

### 搜索与向量

- [[lucene]]
- [[elasticsearch]]
- [[solr]]
- [[faiss]]
- [[pgvector]]
- [[pinecone]]
- [[weaviate]]
- [[milvus]]
- [[qdrant]]
- [[word2vec]]
- [[bert]]
- [[gpt]]

### 工具与库

- [[sql]]
- [[hibernate]]
- [[activerecord]]
- [[axon-framework]]
- [[apache-kafka]]
- [[pandas]]
- [[numpy]]
- [[hdrhistogram|HdrHistogram]]
- [[t-digest]]
- [[ddsketch|DDSketch]]

### Data catalog 与治理

- [[polaris]]
- [[unity-catalog]]
- [[materialize]]

## Log

查看 [[log]] 了解 wiki 的更新历史。
