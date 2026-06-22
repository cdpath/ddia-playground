---
title: "Performance"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, performance, nonfunctional-requirements]
---

# Performance

**Performance** 是 data-intensive system 的核心非功能需求之一，衡量系统执行任务的快慢与处理能力。它通常与 [[reliability]]、[[scalability]]、[[maintainability]] 一起被讨论。

## 主要指标

讨论 performance 时有两个核心指标：

- **Response time**：客户端从发出请求到收到响应的总时间，单位通常是秒、毫秒或微秒。
- **Throughput**：系统每秒处理的请求数或数据量，即“单位时间内的处理量”。

Response time 与 throughput 密切相关：当 throughput 接近硬件容量时，queueing 会导致 response time 急剧上升。

## Response time 的组成

Response time 不是单一数值，而是由多个部分组成：

- **Service time**：服务真正处理请求所花的时间。
- **Queueing delay**：请求等待被处理的时间。CPU 核心数有限，少量慢请求会阻塞后续请求，这种效应称为 **head-of-line blocking**。
- **Network latency / network delay**：请求与响应在网络中传输的时间。
- **Latency**：一个统称，指请求处于“潜伏”状态、未被主动处理的时间。

## 分布与 Percentiles

同一请求多次执行的 response time 也会有波动。Context switch、丢包重传、GC pause、page fault、机械振动等都会引入随机延迟，网络延迟的波动也称为 **jitter**。

因此 response time 应被视为一个分布，而不是单一数值：

- **Mean (average)**：便于估算吞吐上限，但对典型用户体验的代表性不强。
- **Median (p50)**：一半请求比它快，一半比它慢，是典型用户体验的良好指标。
- **Tail latencies**：p95、p99、p999 表示最差的一批请求，直接影响用户感知。例如 [[amazon]] 对内部服务使用 p99.9 作为目标，因为最慢请求往往来自最有价值的客户。
- 多个后端调用并行时，一个慢请求会拖慢整个 end-user 请求，这称为 **tail latency amplification**。

## 计算 Percentiles

在监控 dashboard 中计算 percentiles 需要高效算法，常见开源库包括 [[hdrhistogram|HdrHistogram]]、[[t-digest]]、[[ddsketch|DDSketch]] 和 OpenHistogram。

重要注意：直接对 percentiles 取平均值在数学上没有意义；正确做法是合并 histogram。

## 与 SLO/SLA 的关系

Performance 指标常被写入 [[service-level-objective|SLO]] 和 [[service-level-objective|SLA]]，例如“median response time < 200 ms，p99 < 1 s”。

## 相关

- [[service-level-objective]] — 用 percentiles 定义性能与可用性目标
- [[metastable-failure]] — 过载时的性能崩溃
- [[scalability]] — 负载增长时保持 performance
- [[shared-nothing-architecture]] — 扩展硬件以提升 performance
