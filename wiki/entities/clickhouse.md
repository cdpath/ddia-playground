---
title: "ClickHouse"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [database, olap, analytics, columnar]
---

# ClickHouse

ClickHouse 是开源的列式 DBMS，针对 analytical query 优化。本书既把它列为 self-hosted analytical/OLAP 系统，也列为 real-time analytics 系统。

## 本章角色

- self-hosted OLAP engine 的例子
- 与 Pinot、Druid 并列为 product analytics / real-time analytics 系统
- 采用 [[column-oriented-storage|列式存储]]、[[column-compression|列压缩]] 与 [[vectorized-processing|向量化执行]] 来加速分析查询

## 相关

- [[online-analytical-processing|OLAP]]
- [[data-warehouse]]
- [[column-oriented-storage]]
- [[vectorized-processing]]
- [[chapter-04]]
