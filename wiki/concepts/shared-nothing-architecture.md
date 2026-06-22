---
title: "Shared-nothing architecture"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, distributed-systems, scalability]
---

# Shared-nothing architecture

**Shared-nothing architecture** 是一种分布式系统架构：每个节点拥有自己的 CPU、内存和磁盘，节点之间通过常规网络通信，不共享内存或磁盘。它也被称为 **horizontal scaling** 或 **scaling out**。

## 三种经典扩展架构

| 架构 | 特点 | 主要限制 |
|------|------|----------|
| Shared-memory (vertical scaling / scaling up) | 多核/多线程共享同一台机器的 RAM | 成本非线性增长，硬件瓶颈明显 |
| Shared-disk | 多台机器独立 CPU/RAM，共享 NAS 或 SAN 存储 | 锁与争用限制扩展 |
| Shared-nothing | 每个节点独立，通过网络协调 | 需要 sharding，承担分布式系统复杂度 |

## Shared-nothing 的优势

- 理论上可实现更好的 linear scalability。
- 能使用性价比最高的硬件，特别适合云环境。
- 可根据负载灵活增减资源。
- 通过跨数据中心、跨 region 部署获得更高的 fault tolerance。

## Shared-nothing 的挑战

- 需要显式地进行 sharding/partitioning（详见本书第 7 章）。
- 带来分布式系统的全部复杂度（网络延迟、partial failure、一致性等）。
- 不是所有 workload 都适合；如果单节点 database 已足够，通常应避免分布式带来的复杂度。

## 云原生变体

一些 cloud-native database 采用存储与计算分离的架构：多个计算节点共享一个专门的存储服务。这与传统 shared-disk 有相似之处，但存储服务提供针对 database 优化的 API，避免了 NAS/SAN 的扩展瓶颈。

## 相关

- [[scalability]] — 负载增长时的扩展策略
- [[distributed-system]] — shared-nothing 带来的分布式挑战
- [[cloud-native]] 与 [[separation-of-storage-and-compute]] — 云原生存储计算分离
- [[microservices]] — 将系统拆分为独立组件
