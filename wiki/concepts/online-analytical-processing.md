---
title: "Online analytical processing (OLAP)"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, olap, analytics]
---

# Online analytical processing (OLAP)

**OLAP** 是 analytical system 典型的访问模式：查询扫描大量记录并计算聚合统计量，而非返回单条记录。

特征：

- 用户是 business analyst 和 data scientist，用于决策支持
- 查询通常是任意的、探索性的，可手写，也可由 BI 工具生成
- 单次查询复杂，但整体查询量低
- 数据通常代表一段时间内的历史事件

OLAP 负载通常运行在 [[data-warehouse]] 或 [[data-lake]] 上，而不是直接跑在 operational OLTP system 上。原因包括性能隔离，以及 analytics 需要整合多个来源的数据。

在 data modeling 上，OLAP 系统通常更适合 [[denormalization|denormalized]] 数据（如 [[data-warehouse-schema|star schema]] 或 one big table），因为写入是批量进行，读性能是主要关注点。
