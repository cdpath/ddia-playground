---
title: "Data warehouse"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, analytics, storage]
---

# Data warehouse

**Data warehouse** 是一个独立的数据库系统，保存来自企业 operational system 的只读数据副本，并针对 analytical query 优化。

## 为什么要与 OLTP 分离

- 感兴趣的数据往往分散在许多 operational system 中，形成 [[data-silo]]
- 适合 OLTP 的 schema 和布局并不适合 analytics
- analytical query 很昂贵，会拖累 OLTP 性能
- operational system 可能位于受限制的网络中，出于安全或合规原因不允许直接访问

## 数据如何进入

数据从 OLTP database 被抽取、转换成 analysis-friendly 的 schema、清洗后加载进 data warehouse。这一过程称为 [[extract-transform-load|ETL]]。其变体 **ELT** 则先把数据加载进 warehouse，再在内部完成转换。

Data warehouse 通常使用 relational model 和 SQL，并通过 Tableau、Looker、Power BI 等 BI 工具访问。

## Schema 形式

Data warehouse 常用以下 schema 结构：

- [[data-warehouse-schema|Star schema]]：中心 fact table 加周围 dimension tables。
- [[data-warehouse-schema|Snowflake schema]]：dimension tables 进一步 normalized。
- [[data-warehouse-schema|One big table (OBT)]]：把 dimension 信息 denormalize 进 fact table。

## 相关概念

- [[data-lake]] — 存储原始文件，不强加 relational schema
- [[hybrid-transactional-analytical-processing|HTAP]] — 试图在单一系统中同时支持 OLTP 和 OLAP
- [[online-analytical-processing|OLAP]] — data warehouse 所服务的查询模式
- [[data-warehouse-schema]] — star、snowflake、OBT 等 schema 模式
