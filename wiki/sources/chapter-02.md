---
title: "Chapter 2. Defining Nonfunctional Requirements"
type: source
source_count: 1
last_updated: 2026-06-22
tags: [nonfunctional-requirements, performance, reliability, scalability, maintainability]
---

# Chapter 2. Defining Nonfunctional Requirements

本章从功能性需求之外的角度，定义和度量 data-intensive system 的四大非功能需求：[[performance]]、[[reliability]]、[[scalability]] 与 [[maintainability]]。这些术语将在后续章节反复出现。

## 案例：社交网络首页时间线

本章以 [[twitter|X/Twitter]] 风格的社交网络为例：

- 5 亿 posts/天，平均约 5,800 posts/秒，峰值可达 150,000 posts/秒。
- 平均用户关注 200 人、被 200 人关注；但少数 celebrity 拥有上亿 follower。
- 核心 read 操作是 **home timeline**：展示关注对象最近的 posts。

### 直接查询 vs 物化时间线

直接按关系数据库查询 timeline 会在 read 时做大量 JOIN 与排序，polling 时会产生 4 亿次 lookups/秒，成本极高。更好的做法是 **materialization**：每个用户预先计算并保存自己的 home timeline。发帖时把 post **fan-out** 到所有 follower 的 timeline cache 里。

- 写放大：平均 fan-out factor 为 200，意味着每秒约 100 万次 timeline writes，但远低于直接查询的 4 亿次 lookups。
- 读极快：timeline 直接来自 [[cache]]。
- 特殊处理：普通用户可容忍少量 timeline writes 被丢弃；celebrity post 则单独存储，读取时与 materialized timeline 合并。

这个例子说明：data system 的 performance 和 [[scalability]] 常常需要在 read 与 write 之间做 trade-off，而 [[materialized-view]] 是一种常见的 derived data 优化手段。

## 描述 Performance

Performance 通常用两类指标度量：

- **Response time**：从客户端发出请求到收到响应的总时间（含 network latency、queueing delay、service time）。
- **Throughput**：单位时间内处理的请求数或数据量。

Response time 是一个分布，不是单一数值：

- 平均值（mean）容易被 outlier 拉高，不能代表典型用户体验。
- 中位数（median / p50）表示一半请求比它快、一半比它慢。
- 高百分位（p95、p99、p999，即 **tail latency**）反映最差体验，对高价值用户尤为重要。
- 多个后端调用并行时，一个慢调用会拖慢整个 end-user 请求，即 **tail latency amplification**。

这些指标常作为 [[service-level-objective|SLO]] / [[service-level-objective|SLA]] 的定义依据。

## 过载与 Metastable failure

当 throughput 接近硬件上限时，queueing delay 急剧上升，客户端超时并重试，形成 **retry storm**。系统可能进入即使负载下降也无法自行恢复的恶性循环，即 **metastable failure**。

缓解手段包括：

- [[metastable-failure|Exponential backoff]] 与 jitter，避免重试同步。
- [[metastable-failure|Circuit breaker]]：暂时停止向故障服务发请求。
- [[metastable-failure|Token bucket]]：限制请求速率。
- [[metastable-failure|Load shedding]]：服务端主动拒绝部分请求。
- [[metastable-failure|Backpressure]]：服务端要求客户端降速。

## Reliability 与 Fault Tolerance

**Reliability** 指系统即使在出错时也能继续正确工作。本章区分：

- **Fault**：系统某一部分出错（磁盘坏、机器宕、外部服务不可用）。
- **Failure**：系统整体无法满足 SLO。

[[fault-tolerance]] 指系统在特定 fault 下仍能继续服务；无法容忍的组件称为 **single point of failure (SPOF)**。

- **Hardware faults**：在大规模系统中几乎每天发生，传统靠冗余（RAID、双电源、备用发电机）解决；云时代更强调跨节点/availability zone/region 的软件级容错。
- **Software faults**：通常高度相关（所有节点跑同一份代码），如 leap second、firmware bug、runaway process、依赖服务异常、cascading failure 等，更难预防。
- **Humans**：配置变更是生产事故的主要原因。应把“human error”视为社会技术系统的症状，通过 [[blameless-postmortem]] 等方式学习改进，而非追责。

## Scalability

**Scalability** 不是“X 能不能 scale”这种二元标签，而是一组问题：

- 负载以何种方式增长？
- 需要增加哪些计算资源？
- 当前架构何时会触顶？

理解 load 是讨论 scalability 的前提。理想情况是 **linear scalability**：资源翻倍、吞吐翻倍、性能不变。现实往往超线性增长。

扩展架构：

- **Vertical scaling (scaling up)** / shared-memory：换更强的机器，但成本非线性、存在瓶颈。
- **Shared-disk**：多机器共享 NAS/SAN 存储，受锁与争用限制。
- **Horizontal scaling (scaling out)** / [[shared-nothing-architecture]]：多节点各自独立，通过网络协调，是云与分布式系统的主流。

好的 scalability 原则：把系统拆分为可独立运行的小组件（microservices、sharding、stream processing 等），但不要过度复杂；能用单节点 database 时不必强行分布式。

## Maintainability

软件的大部分成本在维护。Maintainability 包含三个维度：

- **Operability**：让运维团队容易保持系统平稳运行。自动化必不可少，但过度自动化也会增加排障难度。
- **Simplicity**：降低系统复杂度，使新工程师容易理解，减少修改时引入 bug 的风险。
- **Evolvability**：让系统能随需求变化而演化。

[[abstraction]] 是管理复杂性的核心工具；好的 abstraction 隐藏实现细节、可复用、提高整体质量。数据系统层面的 abstraction 包括 database transactions、indexes、event logs 等。

## Key takeaways

1. 非功能需求与功能需求同等重要：慢、不可靠、难维护的系统等于不存在。
2. Performance 需要同时看 response time 与 throughput，并用 percentiles 描述分布。
3. 读快写慢、写快读慢是常见 trade-off；[[materialized-view]] 与 [[fan-out]] 是典型案例。
4. Reliability 的核心是 [[fault-tolerance]]，必须区分 hardware/software/human 三类故障。
5. Scalability 是关于增长选项的问题，不是单一属性；[[shared-nothing-architecture]] 是主流扩展方式。
6. Maintainability 来自 operability、simplicity、evolvability 和良好的 abstraction。

## Open threads

- 后续章节将深入讨论 replication、partitioning/sharding、transactions、consistency 等具体实现如何支撑 reliability 与 scalability。
- [[materialized-view]] 与 stream processing 的关系将在第 11–12 章展开。
- Exactly-once semantics 与 fan-out 将在第 12 章详细讨论。
