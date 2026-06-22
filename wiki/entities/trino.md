---
title: "Trino"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [query-engine, data-lake, sql]
---

# Trino

**Trino**（原 PrestoSQL）是开源的分布式 SQL query engine，用于查询 [[data-lake]] 和多种数据源。它不自己存储数据，而是解析 SQL、生成执行计划并在分布式集群上执行。

## 本章角色

- 现代 data lake query engine 的代表。
- 常与 [[apache-iceberg]]、[[delta-lake]]、[[parquet]] 等 table format 配合使用。
- 与 [[presto]]（PrestoDB）同源但独立发展。

## 相关

- [[query-engine]]
- [[data-lake]]
- [[parquet]]
- [[apache-iceberg]]
- [[delta-lake]]
- [[presto]]
- [[chapter-04]]
