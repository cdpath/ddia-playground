---
title: "Derived data system"
type: concept
source_count: 3
last_updated: 2026-06-22
tags: [data-systems, fundamentals]
---

# Derived data system

**Derived data system** 保存的数据来自对另一个系统数据的转换或处理。如果 derived data 丢失，可以从原始来源重建。

例子：

- [[cache]]
- [[search-index]]
- [[materialized-view]]
- [[event-sourcing]] / [[cqrs]] 中的 read model / projection
- denormalized value
- 在数据集上训练出的 ML model

derived data 在技术上是冗余的，但通常对读性能至关重要，也能提供同一数据的不同视角。[[analytical-system]] 通常就是 derived data system，因为它们消费别处产生的数据。

当 derived system 的数据来自 [[system-of-record]] 时，必须有一种机制在 source 变更时更新 derived data。data integration 和 pipeline 解决的就是这个问题。

典型例子：[[twitter|X/Twitter]] 的 home timeline 就是用户关注对象 posts 的 materialized view，通过 [[fan-out]] 机制在 source 数据变化时更新。
