---
title: "Materialized view"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, performance, derived-data]
---

# Materialized view

**Materialized view** 是预先计算并保存的查询结果。与每次查询都重新计算不同，它通过“以写换读”的方式加速读取路径。

## 典型例子：社交网络时间线

在 [[twitter|X/Twitter]] 风格的社交网络中，每个用户的 home timeline 就是一个 materialized view：

- 用户发帖时，系统把这条 post **fan-out** 到所有 follower 的 timeline。
- 读取 timeline 时直接返回缓存的 materialized view，无需实时做复杂查询。
- 用户可通过订阅自己的 timeline 流接收实时更新。

## 优点与代价

优点：

- 读路径极快。
- 可以 push/subscribe 方式实时通知。
- 在负载尖峰时仍可保持读性能。

代价：

- 写路径更复杂。
- 需要维护 derived data 的一致性。
- Celebrity 发帖会产生极大的 fan-out，需要特殊处理（如单独存储 celebrity posts，读取时合并）。

## 另一个例子：X/Twitter timeline 的 hydration

Chapter 3 指出，X/Twitter 的 materialized timeline 并不存储完整 post 内容，而是只保存 post ID 和 sender ID。读取时再通过两次 join（lookup post 内容与 sender profile）把 ID 解析成人可读信息，这个过程称为 **hydration**。由于点赞数、回复数、用户名、头像等变化很快，把这些信息 denormalize 进 timeline 既不经济也不利于一致性；而 hydration 的并行度很高，成本不依赖粉丝数。

## 与 derived data 的关系

Materialized view 是一种典型的 [[derived-data-system]]：即使丢失，也可以从原始 source 数据重建，但在技术上是冗余的，通常对读性能至关重要。

## 相关

- [[fan-out]] — 更新 materialized view 时的请求放大
- [[cache]] — materialized view 常以 cache 形式存在
- [[derived-data-system]] — materialized view 的本质
- [[online-transaction-processing|OLTP]] — 在线事务场景中的物化视图权衡
