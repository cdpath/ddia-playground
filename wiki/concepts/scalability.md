---
title: "Scalability"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, fundamentals, nonfunctional-requirements]
---

# Scalability

**Scalability** 指系统在负载增加时仍能保持性能的能力。它是 data-intensive system 的三大核心关注点之一，另外两个是 [[reliability]] 和 [[maintainability]]。

## 不是二元属性

说“X 能 scale”或“Y 不能 scale”是没有意义的。讨论 scalability 时应关注具体问题：

- 如果负载以某种方式增长，我们有哪些应对选项？
- 增加哪些计算资源才能保持性能不变？
- 按当前增长趋势，架构何时会触顶？

## 理解负载

首先需要清楚当前 load：

- 每秒请求数、每天新增数据量、每小时交易数等 throughput 指标。
- 峰值、读写比例、cache hit rate、每个用户的数据量等统计特征。
- 瓶颈可能来自平均值，也可能来自少数极端 case。

## 扩展架构

- **Vertical scaling (scaling up)** / shared-memory：换更强的机器；成本非线性、存在瓶颈。
- **Shared-disk**：多机器共享 NAS/SAN 存储；锁和争用限制扩展。
- **Horizontal scaling (scaling out)** / [[shared-nothing-architecture]]：多节点独立；云环境主流，可跨数据中心容错。

## Scalability 原则

- 把系统拆分为可独立运行的小组件（microservices、sharding、stream processing 等）。
- 不要过度设计：如果单节点 database 足够，就不要强行分布式。
- 通常只需提前规划一个数量级的增长；过度超前会锁定不灵活的设计。
- 好的架构通常是多种 pragmatic 方案的混合。

## 相关

- [[performance]] — 负载增长时要保持的指标
- [[shared-nothing-architecture]] — 主流横向扩展架构
- [[distributed-system]] — 横向扩展带来的分布式挑战
- [[cloud-native]] 与 [[microservices]] — 云时代的拆分方式
