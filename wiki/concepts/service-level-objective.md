---
title: "Service Level Objective (SLO) & Service Level Agreement (SLA)"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, operations, reliability, performance]
---

# Service Level Objective (SLO) & Service Level Agreement (SLA)

**SLO** 与 **SLA** 是定义服务性能与可用性目标的常用工具。

## SLO

**Service Level Objective（SLO）** 是对服务期望表现的量化目标。例如：

- median response time < 200 ms
- p99 response time < 1 s
- 99.9% 的有效请求返回非错误响应

SLO 为团队提供了可度量的目标，也常与 [[performance]] 的 percentiles 直接挂钩。

## SLA

**Service Level Agreement（SLA）** 是服务提供方与客户之间的合同，规定如果 SLO 未达到会有什么后果（如退款、服务积分）。

## 实践中的挑战

定义良好的 availability 与 performance 指标并不容易。选择哪些指标作为 SLO、设置多高的目标、如何统计错误，都需要仔细权衡。实践中，SLO 与 SLA 既是工程约束，也是业务承诺。

## 相关

- [[performance]] — response time 与 throughput 指标
- [[reliability]] — 可用性目标
- [[observability]] — 度量和监控这些目标
