---
title: "CQRS"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, architecture, event-driven]
---

# CQRS

**CQRS（Command Query Responsibility Segregation）** 是一种把“写模型”和“读模型”分离的架构模式。写入针对 write-optimized 表示，读取针对 read-optimized materialized views。

## 与 event sourcing 的关系

CQRS 常与 [[event-sourcing]] 一起使用：

- Commands 来自用户请求，先被验证。
- 有效命令变成 event，append 到 immutable event log。
- Materialized views 异步从 event log 派生，服务不同查询需求。

## 优点

- 读模型可以针对具体查询 denormalize，读性能高。
- 写模型简单快速（append-only log）。
- 不同团队可独立演进读写模型。

## 缺点

- 增加架构复杂度。
- Read views 与 write model 之间是最终一致。
- 需要处理重放、side effects、schema evolution 等问题。

## 相关

- [[event-sourcing]]
- [[materialized-view]]
- [[derived-data-system]]
- [[chapter-03]]
