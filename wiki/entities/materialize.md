---
title: "Materialize"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, streaming, materialized-view]
---

# Materialize

**Materialize** 是一个专注于 [[materialized-view]] 维护的数据库系统。它能够自动在底层数据变化时增量更新物化视图。

## 特点

- 基于流处理技术实现物化视图的增量维护。
- 适合需要低延迟查询最新 derived data 的场景。
- 本书在 Chapter 12 会进一步讨论物化视图维护。

## 相关

- [[materialized-view]]
- [[derived-data-system]]
- [[stream-processing]]
- [[chapter-04]]
- [[chapter-12]]
