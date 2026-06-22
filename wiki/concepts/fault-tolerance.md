---
title: "Fault tolerance"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, reliability, distributed-systems]
---

# Fault tolerance

**Fault tolerance** 指系统在部分组件发生故障时，仍能继续向用户提供所需服务的能力。它是 [[reliability]] 的核心实现手段。

## Fault vs failure

- **Fault**：系统的某个部分停止正常工作，例如一块硬盘损坏、一台机器宕机、一个依赖服务不可用。
- **Failure**：系统整体未能满足其 SLO，无法向用户提供服务。

同一个事件在不同粒度下可能是 fault 或 failure：单块硬盘损坏对多盘系统是 fault，对单盘系统就是 failure。

## Single point of failure (SPOF)

如果系统无法容忍某个组件的故障，该组件就是 **single point of failure（SPOF）**。消除 SPOF 是设计 fault-tolerant 系统的关键步骤。

## 冗余

应对硬件故障最常用的方法是 **redundancy**：

- 磁盘 RAID、双电源、热插拔 CPU。
- 数据中心备用电池、柴油发电机。
- 跨 availability zone、跨 region 部署。

冗余最有效的前提是各组件故障相互独立；但实际中常存在相关性（同一机架、同一批次硬件）。

## Hardware faults

在大规模系统中，硬件故障是常态：

- 机械硬盘年故障率约 2%–5%。
- SSD 年故障率约 0.5%–1%，且存在不可修复的 bit error。
- 内存、CPU、电源、RAID 控制器也会故障。
- 整个数据中心可能因电力、网络、自然灾害而不可用。

传统上通过硬件冗余减少影响；云时代更强调在软件层面容忍节点、机架甚至 availability zone 的失效，并通过 rolling upgrade 等方式实现不停机维护。

## Software faults

Software faults 往往比 hardware faults 更难处理，因为它们通常是高度相关的：多节点运行同一份代码，同一个 bug 可能同时触发。例子包括：

- leap second 导致大量 Java 应用同时挂起。
- SSD firmware bug 导致所有同型号 SSD 在固定小时数后失效。
- Runaway process 占满 CPU、内存、磁盘、带宽或线程。
- 依赖服务变慢、无响应或返回错误。
- 系统间交互产生的 emergent behavior。
- Cascading failure：一个组件过载拖垮下一个组件。

应对软件故障没有银弹，需要：谨慎审视假设、充分测试、进程隔离、允许崩溃重启、避免 retry storm、完善的监控与 observability。

## Fault injection 与 chaos engineering

通过故意注入故障（如随机 kill 进程）来验证 fault-tolerance 机制，称为 **fault injection**。**Chaos engineering** 是一门通过实验性注入故障来提升对容错机制信心的学科。

## Humans and reliability

运营者的配置变更是生产事故的主要原因之一。把问题简单归咎于“human error”通常适得其反；更好的做法是把错误视为社会技术系统的症状，通过监控、rollback、灰度发布、良好界面设计、[[blameless-postmortem]] 等手段降低影响并持续学习。

## 局限

Fault tolerance 总是有边界的：没有系统能在所有节点同时宕机或地球被黑洞吞噬时继续服务。设计时需要明确“能容忍多少、什么类型的故障”。

## 相关

- [[reliability]] — 高层目标
- [[blameless-postmortem]] — 从人的因素中学习
- [[metastable-failure]] — 过载导致的级联失效
- [[shared-nothing-architecture]] — 通过分布式实现容错
- [[distributed-system]] — 更广泛的分布式挑战
