---
title: "Observability"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [distributed-systems, operations]
---

# Observability

**Observability** 指通过系统的输出理解其内部状态的能力。在 [[distributed-system]] 中，observability 涉及收集系统执行数据，以便同时分析高层指标和单个事件。

**Tracing** 工具（如 OpenTelemetry、Zipkin、Jaeger）可以追踪哪个 client 调用了哪个 server、执行了什么操作、每次调用耗时多久。
