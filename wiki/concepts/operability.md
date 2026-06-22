---
title: "Operability"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, operations, maintainability]
---

# Operability

**Operability** 指使运维团队能够轻松保持系统平稳运行的系统特性。它是 [[maintainability]] 的三个核心维度之一（另外两个是 simplicity 与 evolvability）。

## 自动化是双刃剑

在大规模系统中，手工运维成本不可接受，自动化必不可少。但：

- 自动化系统出错时往往比手工操作更难排查。
- 自动化无法覆盖所有 edge case，越是自动化的系统，越需要高素质运维团队处理例外情况。
- 因此自动化要适度，找到适合具体组织和业务的平衡点。

## 良好 operability 的特征

- 提供监控与 [[observability]] 工具，能查看关键指标与运行时行为。
- 不依赖单台机器，支持在不影响服务的情况下下线节点。
- 文档清晰， operational model 易懂（“如果我做 X，Y 就会发生”）。
- 默认行为合理，同时允许管理员覆盖默认配置。
- 在适当情况下自愈，但也保留手动控制能力。
- 行为可预测，减少意外。

## 相关

- [[maintainability]] — operability 是 maintainability 的子维度
- [[observability]] — 运维诊断的核心能力
- [[reliability]] — 好的运维支撑可靠性
