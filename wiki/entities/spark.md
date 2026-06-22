---
title: "Apache Spark"
type: entity
source_count: 3
last_updated: 2026-06-22
tags: [analytics, big-data, distributed-computing, data-science]
---

# Apache Spark

Apache Spark 是开源的分布式 analytics framework。本书将其列为 self-hosted analytical/OLAP 系统，并指出 data scientist 常与 Python、R 一起使用它。

## Chapter 3 角色

- Spark 支持 [[dataframe]] DataFrame API，用于数据科学和 ML 数据准备。
- Spark 和 Flink 都扩展了 DataFrame 能力，把关系数据转换为矩阵供 ML 使用。

## Chapter 4 角色

- 作为 data lake 生态中的 query engine / 计算框架使用。
- 常与 [[parquet]]、[[orc]]、[[delta-lake]] 等格式配合。
- 支持批处理和流处理（Spark Streaming / Structured Streaming）。

## 相关

- [[online-analytical-processing|OLAP]]
- [[dataframe]]
- [[data-lake]] — Spark 常处理 lake 中的数据
- [[batch-processing]] — Spark 支持 batch workload
- [[parquet]]
- [[orc]]
- [[delta-lake]]
- [[apache-flink]]
- [[chapter-03]]
- [[chapter-04]]
