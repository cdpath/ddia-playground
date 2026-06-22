---
title: "Distributed system"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [distributed-systems, architecture]
---

# Distributed system

**Distributed system** 指多台机器（称为 **node**）通过网络通信协作完成任务的系统。

## 选择 distributed system 的原因

- **Inherent distribution** — 不同用户各自使用不同设备，设备间必须通过网络通信
- **Requests between cloud services** — 数据存在一个服务、在另一个服务处理，必须跨网络传输
- **Fault tolerance / high availability** — 用多台机器提供冗余，单台机器或整个 datacenter 故障时仍能工作
- **Scalability** — 当数据量或计算需求超过单台机器能力时，把负载分散到多台机器
- **Latency** — 在全球部署 server，让用户访问地理位置更近的节点
- **Elasticity** — 忙时扩容、闲时缩容，按实际使用付费
- **Specialized hardware** — 不同部分使用最适合其 workload 的硬件
- **Legal compliance** — 数据驻留法律要求数据存储在特定地理区域内
- **Sustainability** — 在可再生能源充足的时间/地点运行任务，降低碳排放

## 缺点

- 网络调用比进程内调用慢得多
- 任何请求都可能超时或失败；重试可能不安全
- 排查问题困难；[[observability]] 和 tracing 变得至关重要
- 跨服务保持数据一致性成为应用层的问题
- 更多 node 不一定更快；某些场景下单台调优良好的机器可能胜过拥有上百 CPU core 的 cluster

本书建议：除非必要，否则不要把系统做成 distributed。第 9 章会深入讨论 distributed system 的挑战。
