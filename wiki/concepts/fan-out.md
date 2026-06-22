---
title: "Fan-out"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, distributed-systems, messaging]
---

# Fan-out

**Fan-out** 描述一个初始请求触发多个下游请求，导致请求数量按倍数放大的现象。

## 例子

在 [[twitter|X/Twitter]] 的 home timeline 场景中：

- 用户发一条 post。
- 系统需要把这条 post 分发到该用户所有 follower 的 materialized timeline。
- 如果平均每个用户有 200 个 follower，那么 fan-out factor 就是 200。
- 平均 5,800 posts/秒 × 200 = 约 116 万次 timeline writes/秒。

## 意义

Fan-out 使读路径变得简单快速（直接读 materialized view），但写路径承担了更多工作。设计时需要在读写成本之间做 trade-off，并处理极端 case（如 celebrity 的上亿 follower）。

## 相关

- [[materialized-view]] — fan-out 常用来更新物化视图
- [[scalability]] — fan-out 影响写容量规划
- [[distributed-system]] — fan-out 在分布式消息系统中很常见
