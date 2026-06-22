---
title: "Reliability"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, fundamentals, nonfunctional-requirements]
---

# Reliability

**Reliability** 指系统即使在出现故障时也能继续正确工作。它是 data-intensive system 的三大核心关注点之一，另外两个是 [[scalability]] 和 [[maintainability]]。

## 含义

一个 reliable 的系统通常满足：

- 执行用户期望的功能。
- 容忍用户误操作或意外使用方式。
- 在预期负载和数据量下 performance 足够好。
- 防止未授权访问和滥用。

概括地说，reliability ≈ “即使出问题，也继续正确工作”。

## Fault tolerance

实现 reliability 的主要手段是 [[fault-tolerance]]：系统在部分组件发生 fault 时仍能继续提供服务。关键区分：

- **Fault**：组件级错误（硬盘坏、机器宕、依赖服务不可用）。
- **Failure**：系统整体未能满足 SLO。
- **SPOF (single point of failure)**：无法容忍故障的组件。

## 故障来源

- **Hardware faults**：在大规模系统中几乎每天发生；云时代更强调跨节点/availability zone 的软件级容错。
- **Software faults**：通常高度相关（同一份代码的 bug），如 leap second、firmware bug、runaway process、cascading failure 等。
- **Humans**：配置变更等人为操作是生产事故的重要原因。应通过 [[blameless-postmortem]] 等文化从系统中学习，而不是追责个人。

## 为什么 reliability 重要

Reliability 不仅关乎核电站或空中交通管制；普通业务应用也会因 bug 造成生产力损失、法律风险、收入损失或声誉损害。永久性的数据丢失或损坏尤其严重。

## 相关

- [[fault-tolerance]] — 可靠性的实现机制
- [[blameless-postmortem]] — 处理人为因素
- [[metastable-failure]] — 过载导致的级联失效
- [[performance]] 与 [[scalability]] — 另外两大核心关注点
