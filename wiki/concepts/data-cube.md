---
title: "Data Cube"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [analytics, data-warehouse, aggregation]
---

# Data Cube

**Data cube**（又称 OLAP cube）是一种按多个维度预先计算聚合的 [[materialized-view]]。每个单元格保存一组维度值组合上的聚合结果（如 `SUM`、`COUNT`、`AVG`）。

## 说明

假设事实表有 `date_key`、`product_sk`、`store_sk` 等维度。Data cube 会在这些维度的组合上预计算聚合。查询“昨天各门店总销售额”时，只需从 cube 中读取预计算结果，无需扫描原始事实表。

Data cube 还可以在每一维上做进一步汇总（如按日期汇总、按产品汇总），形成多层级汇总。

## 优点

- 常见聚合查询速度极快。
- 适合 dashboards 和固定报表。

## 缺点

- 不如原始数据灵活。例如无法回答未作为维度预计算的过滤条件（如“价格高于 $100 的商品占比”）。
- 增加写入和维护开销。

因此 data warehouse 通常保留尽可能多的原始数据，仅在必要时使用 data cube 作为性能加速器。

## 相关

- [[materialized-view]]
- [[data-warehouse]]
- [[online-analytical-processing|OLAP]]
- [[data-warehouse-schema]]
- [[chapter-04]]
