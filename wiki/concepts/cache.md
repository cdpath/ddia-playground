---
title: "Cache"
type: concept
source_count: 3
last_updated: 2026-06-22
tags: [data-systems, performance]
---

# Cache

**Cache** 保存昂贵操作的结果，以便后续读取更快。它是 [[data-intensive-application]] 的常见组件。

cache 通常是一种 [[derived-data-system]] — 即使 cache 数据丢失，也可以从底层 source 重建。

## 例子

在 [[twitter|X/Twitter]] 的 home timeline 设计中，每个用户的 timeline 被预先计算并放在 cache 中；读取时直接返回缓存，避免实时执行复杂查询。这种 cache 本质上也是一种 [[materialized-view]]。

Chapter 3 进一步说明，X/Twitter 的 timeline cache 只存 post ID 和 sender ID，读取时通过 hydration 查询最新 post 内容与用户信息，因此它介于纯 cache 与 materialized view 之间。
