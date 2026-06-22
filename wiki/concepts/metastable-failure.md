---
title: "Metastable failure"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, reliability, performance, overload]
---

# Metastable failure

**Metastable failure** 指系统在接近容量上限时，因 response time 增加导致客户端超时重试，进而使负载进一步上升，陷入即使原始负载下降也无法自行恢复的恶性循环。

## 形成过程

1. 系统 throughput 接近硬件容量。
2. Queueing delay 增加，response time 变长。
3. 客户端 timeout 并重试，形成 **retry storm**。
4. 请求量进一步增加，系统效率下降，更难恢复。
5. 即使触发源负载回落，系统仍可能保持过载状态，需要重启或外部干预。

## 缓解机制

为避免或打破 metastable failure，常用手段包括：

- **Exponential backoff with jitter**：增加并随机化重试间隔，防止重试同步放大负载。
- **Circuit breaker**：客户端暂时停止向近期出错或超时的服务发请求。
- **Token bucket**：限制请求速率。
- **Load shedding**：服务端在接近过载时主动拒绝部分请求。
- **Backpressure**：服务端通知客户端减速。

queueing 与负载均衡算法的选择也会影响系统是否能从过载中恢复。

## 相关

- [[performance]] — throughput 与 response time 的关系
- [[fault-tolerance]] — 如何容忍过载与故障
- [[scalability]] — 预留与扩展容量
