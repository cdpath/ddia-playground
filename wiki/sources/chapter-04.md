---
title: "Chapter 4. Storage and Retrieval"
type: source
source_count: 1
last_updated: 2026-06-22
tags: [storage, indexing, oltp, olap]
---

# Chapter 4. Storage and Retrieval

来源：[[designing-data-intensive-applications]] · 原文：[`raw/chapter4/04.md`](../../raw/chapter4/04.md)

## 摘要

本章从数据库内部视角讨论 storage 与 retrieval：当应用把数据交给数据库时，数据库如何落盘；当再次查询时，数据库如何找到数据。重点对比了 OLTP 与 OLAP 两种负载下的存储引擎设计，并介绍了从 B-tree、LSM-tree 到列式存储、多维索引、全文检索和向量索引的广泛技术。

## 关键收获

- **索引是主数据的 derived structure**。它能加速读查询，但会占用额外空间并降低写入速度。数据库不会自动为所有列建索引，开发者需根据查询模式选择。
- **OLTP 存储引擎主要有两条路线**：
  - **Log-structured**：只追加、不修改旧文件，用 [[lsm-tree]] + [[sstable]] + [[compaction]] 实现高写入吞吐。代表：[[rocksdb]]、[[cassandra]]、[[hbase]]、[[lucene]]。
  - **Update-in-place**：以固定大小 page 原地覆写，用 [[b-tree]] + [[write-ahead-log|WAL]] 实现可靠读。代表：[[mysql]] InnoDB、[[postgresql]]、[[sql-server]]。
- **OLAP 存储引擎采用完全不同的布局**：[[column-oriented-storage|列式存储]]、[[column-compression|列压缩]]、排序与 bitmap 索引，配合 [[query-compilation]] 或 [[vectorized-processing]] 降低 I/O 和 CPU 开销。
- **存储层面的权衡可量化**：[[write-amplification]]、[[read-amplification]]、[[sequential-write]] vs [[random-write]]、空间占用与延迟，都需要根据实际 workload 测试。
- **多维与语义索引**：[[r-tree]] 和 [[space-filling-curve]] 处理空间数据；[[inverted-index]] 和 [[postings-list]] 支撑全文搜索；[[vector-embedding]] 与 [[hnsw]] / [[ivf]] 支撑语义搜索。

## 本章引入的主要概念

### Storage engine 基础

- [[storage-engine]]
- [[index]]
- [[primary-index]] / [[secondary-index]]
- [[clustered-index]] / [[heap-file]] / [[covering-index]]
- [[in-memory-database]] / [[embedded-database]]
- [[write-ahead-log]]

### Log-structured 存储

- [[log-structured-storage]]
- [[lsm-tree]]
- [[sstable]]
- [[memtable]]
- [[compaction]]
- [[bloom-filter]]
- [[tombstone]]

### B-tree 与可靠性

- [[b-tree]]
- [[fragmentation]]

### 性能与硬件

- [[write-amplification]]
- [[read-amplification]]
- [[sequential-write]] / [[random-write]]
- [[garbage-collection-ssd|SSD garbage collection]]
- [[backpressure]]

### OLAP 与分析存储

- [[column-oriented-storage]]
- [[row-oriented-storage]]
- [[column-compression]]
- [[bitmap-index]]
- [[run-length-encoding]]
- [[roaring-bitmaps]]
- [[query-compilation]]
- [[vectorized-processing]]
- [[materialized-view]] / [[data-cube]]

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
- [[flat-index]] / [[ivf]] / [[hnsw]]

### 数据湖与开放格式

- [[parquet]] / [[orc]] / [[lance]] / [[nimble]]
- [[apache-arrow]]
- [[apache-iceberg]] / [[delta-lake]]
- [[table-format]]
- [[data-catalog]]

## 提到的系统与工具

### OLTP / embedded storage

- [[rocksdb]]、[[leveldb]]、[[sqlite]]、[[lmdb]]
- [[cassandra]]、[[scylladb]]、[[hbase]]、[[bigtable]]
- [[mysql]] / [[innodb]]、[[postgresql]]、[[sql-server]]
- [[redis]]、[[memcached]]、[[couchbase]]
- [[voltdb]]、[[singlestore]]、[[oracle-timesten]]、[[ramcloud]]

### OLAP / data warehouse

- [[snowflake]]、[[clickhouse]]、[[duckdb]]
- [[bigquery]]、[[amazon-redshift]]
- [[vertica]]、[[teradata]]、[[sap-hana]]
- [[apache-pinot]]、[[apache-druid]]
- [[apache-hive]]、[[trino]]、[[presto]]、[[apache-datafusion]]、[[spark]]

### 搜索与向量

- [[lucene]]、[[elasticsearch]]、[[solr]]
- [[faiss]]、[[pgvector]]、[[pinecone]]、[[weaviate]]、[[milvus]]、[[qdrant]]
- [[postgis]]

### 时序与 catalog

- [[influxdb]]、[[timescaledb]]
- [[polaris]]、[[unity-catalog]]

### 模型

- [[word2vec]]、[[bert]]、[[gpt]]

## Playground

- [LSM-tree vs B-tree 的读写权衡](../../playgrounds/ch04-storage-and-retrieval/01-lsm-vs-btree.ipynb)：用标准库模拟两种存储引擎，观察写入放大、读取放大与 Bloom filter 效果。

## 待后续章节展开的线索

- 崩溃恢复、 durability 和并发事务的语义将在 [[chapter-08]] 深入。
- Replication 和 partitioning 分别在 [[chapter-06]] 和 [[chapter-07]] 讨论。
- Stream processing 中的 materialized view 维护将在 [[chapter-12]] 回到。
- Encoding 和 serialization format 的更多细节见 [[chapter-05]]。
