---
title: "Data Warehouse Schema"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, data-warehousing, analytics]
---

# Data Warehouse Schema

Data warehouse 通常使用专为分析优化的 schema 结构。本章介绍三种常见模式：star schema、snowflake schema 和 one big table（OBT）。

## Star schema

- 中心是 **fact table**，每一行代表一个业务事件（如一笔销售、一次页面浏览）。
- 周围是 **dimension tables**，描述事件的 who、what、where、when、how、why。
- 可视化时像一颗星星，因此得名。

## Snowflake schema

- dimension tables 进一步拆分为 subdimensions，更加 normalized。
- 比 star schema 更省空间，但分析师使用起来更复杂。

## One big table（OBT）

- 把 dimension 信息全部 denormalize 进 fact table，预先完成 join。
- 存储更大，但查询可能更快，适合某些现代数据仓库场景。

## 与 OLTP 的对比

在 analytics 中，denormalization 问题较小，因为数据通常是只读的历史日志，写入开销和一致性压力不像 OLTP 那么突出。

## 相关

- [[data-warehouse]]
- [[online-analytical-processing|OLAP]]
- [[extract-transform-load|ETL]]
- [[normalization]]
- [[denormalization]]
- [[chapter-03]]
