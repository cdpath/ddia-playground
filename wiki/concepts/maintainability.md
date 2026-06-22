---
title: "Maintainability"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, fundamentals, nonfunctional-requirements]
---

# Maintainability

**Maintainability** 指系统随时间推移仍易于运维、修改和理解的特性。它是 data-intensive system 的三大核心关注点之一，另外两个是 [[reliability]] 和 [[scalability]]。

## 为什么重要

软件不会像机械零件那样磨损，但需求会变化、运行环境会变化、bug 需要修复。软件的大部分成本不在初始开发，而在长期维护（修复 bug、运维、适配新平台、偿还技术债务、新增功能）。

## 三个维度

- **Operability**：让运维团队容易保持系统平稳运行。自动化、监控、[[observability]]、良好文档和可预测行为都属于此范畴。详见 [[operability]]。
- **Simplicity**：降低复杂度，使新工程师容易理解系统，减少修改时引入 bug 的风险。
- **Evolvability**：让系统能随需求变化而演化。

## 管理复杂性

复杂系统难以理解和推理，容易隐藏假设、产生意外交互。管理复杂性的关键工具是 [[abstraction]]：隐藏实现细节、提供清晰接口、实现可复用组件。

好的 abstraction 示例：

- 高级编程语言隐藏机器码和寄存器。
- SQL 隐藏索引、并发和崩溃恢复。
- 数据库 transactions、indexes、event logs 是 data system 层面的通用 abstraction。

## 相关

- [[operability]] — maintainability 的运维维度
- [[abstraction]] — 降低复杂度的核心工具
- [[reliability]] 与 [[scalability]] — 另外两大核心关注点
