---
title: "Snowflake"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [cloud, data-warehouse, olap, columnar]
---

# Snowflake

Snowflake 是 cloud-based analytical database / [[data-warehouse]]。它是 [[cloud-native]] 系统的典型例子，将 storage 与 compute 分离。

## 本章角色

- 被列为 cloud-native analytical/OLAP 系统
- 依赖 object storage（S3）存放数据
- 内部采用 [[column-oriented-storage|列式存储]]，并通过 [[materialized-view]] 和 [[data-cube]] 加速查询
- 与 self-hosted analytical 系统（Teradata、ClickHouse、Spark）形成对比

## 相关

- [[data-warehouse]]
- [[cloud-native]]
- [[separation-of-storage-and-compute]]
- [[column-oriented-storage]]
- [[materialized-view]]
- [[amazon-s3]]
- [[chapter-04]]
