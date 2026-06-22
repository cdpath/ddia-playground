---
title: "Event Sourcing"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, event-driven, architecture]
---

# Event Sourcing

**Event sourcing** 是一种把应用状态的所有变化记录为不可变 event log 的建模方式。event log 是 source of truth，当前状态可以通过重放 events 推导出来。

## 核心原则

- Events 是 immutable 的：不修改、不删除，只 append。
- Events 应该用过去时命名，例如 "SeatsWereBooked"，表示已经发生的事实。
- 多个 **materialized views / projections / read models** 可以从同一 event log 派生。

## 与 CQRS 的关系

Event sourcing 常与 [[cqrs]] 一起使用：用 append-only log 优化写入，用派生视图优化读取。

## 优点

- 表达业务意图清晰。
- Materialized views 可删除后重算，便于修复 bug 和演进系统。
- 支持多个 read-optimized views。
- 自然提供 audit log。
- 顺序写吞吐高，能吸收写入突发。

## 缺点

- 涉及外部数据时，必须保证重放结果 deterministic（如把汇率写入 event 或使用历史汇率查询）。
- Immutable events 与个人数据删除权（GDPR）冲突，需要 crypto-shredding 等技巧。
- 重放事件可能触发外部副作用（如重复发邮件）。
- 需要保证所有 views 按相同顺序处理 events，分布式系统中并不简单。

## 相关

- [[cqrs]]
- [[materialized-view]]
- [[derived-data-system]]
- [[apache-kafka]]
- [[chapter-03]]
