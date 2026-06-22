---
title: "Separation of storage and compute"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [cloud, architecture, data-systems]
---

# Separation of storage and compute

**Separation of storage and compute**（也称 *disaggregation*）是一种架构选择：将 storage 与 computation 作为可独立扩展的服务处理，而非耦合在同一台机器上。

## 传统架构

单台计算机同时负责 durable storage（disk）和 computation（CPU/RAM）。这很简单，但限制了扩展与故障恢复。

## Cloud-native 架构

- compute instance 被视为 ephemeral
- 长期数据存放在专用 storage service（如 [[object-storage]] 或 cloud database 的专用存储层）
- compute 可独立于数据规模进行扩缩容
- 故障的 compute instance 可被替换，无需迁移数据

## Trade-offs

- storage 与 compute 之间的网络传输会增加 latency 和成本
- 云原生系统必须从一开始就避免 block-device emulation 的开销
- multitenancy 带来隔离与安全要求

这一模式是许多 [[cloud-native]] data system（如 Snowflake、AWS Aurora）的核心。
