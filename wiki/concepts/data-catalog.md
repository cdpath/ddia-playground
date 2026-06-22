---
title: "Data Catalog"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-lake, metadata, governance]
---

# Data Catalog

**Data catalog** 定义了一个数据库或数据湖中包含哪些表。它用于创建、重命名、删除表，并为 query engine 提供表元数据。

## 说明

在传统的数据仓库中，catalog 与 query engine 集成在一起。随着 data lake 架构的发展，catalog 越来越被解耦为独立服务，支持：

- 数据发现（data discovery）。
- 数据治理（data governance）。
- 跨 query engine 共享元数据。

常见 data catalog：

- Snowflake Polaris
- Databricks Unity Catalog
- Apache Iceberg REST catalog
- Apache Hive Metastore

## 相关

- [[data-lake]]
- [[table-format]]
- [[apache-iceberg]]
- [[delta-lake]]
- [[chapter-04]]
