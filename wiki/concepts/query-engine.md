---
title: "Query Engine"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, query, analytics]
---

# Query Engine

**Query engine** 是负责解析、优化和执行查询的软件组件。它把用户提交的查询（通常是 SQL）转换成执行计划，并调度执行。

## 说明

在传统的数据仓库中，query engine 与 storage 和 catalog 集成在一起。随着 data lake 架构的发展，query engine 越来越被解耦为独立组件，例如：

- [[trino]]、[[presto]]、[[apache-datafusion]]
- [[spark|Apache Spark]] SQL
- Apache Flink SQL

Query engine 的职责包括：

- 解析 SQL 并生成逻辑执行计划。
- 基于统计信息和成本模型做查询优化。
- 把逻辑计划编译成物理执行计划。
- 调度和执行分布式任务。

## 相关

- [[sql]]
- [[query-language]]
- [[declarative-query-language]]
- [[data-lake]]
- [[data-warehouse]]
- [[chapter-04]]
