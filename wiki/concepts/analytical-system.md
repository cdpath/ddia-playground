---
title: "Analytical system"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, olap, analytics]
---

# Analytical system

**Analytical system** 服务于 business analyst 和 data scientist，保存来自 operational system 的只读数据副本，并针对 analytics 负载优化。

主要特征：

- 用户通常不修改原始数据
- 查询会扫描大量记录并计算聚合统计量（count、sum、average 等）
- 查询通常是任意的、探索性的
- 数据代表一段时间内的历史事件
- 数据集通常比 operational 数据集更大

analytical system 与 [[online-analytical-processing|OLAP]] 密切相关，通常通过 [[extract-transform-load|ETL]] 从 operational system 导入 [[data-warehouse]] 或 [[data-lake]]。

近年出现的 **product analytics** 或 **real-time analytics** 将 analytical 查询嵌入到面向用户的产品中，例如 Pinot、Druid、ClickHouse。
