---
title: "Data-intensive application"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, fundamentals]
---

# Data-intensive application

当 **data management** 成为应用开发的主要挑战时，这个应用就被称为 **data-intensive application**；与之相对的是 **compute-intensive** 系统，其主要挑战是并行化超大计算量。

data-intensive application 中真正困难的问题通常包括：

- 存储与处理大规模数据
- 管理数据变更
- 在故障与并发场景下保证一致性
- 保持服务高可用

这些应用通常由以下标准组件拼装而成：

- [[database]] — 存储数据，供后续查找
- [[cache]] — 缓存昂贵操作的结果，加速读取
- [[search-index]] — 按关键词或条件搜索、过滤数据
- [[stream-processing]] — 实时处理事件与数据变更
- [[batch-processing]] — 定期处理累积的大量数据

大多数 data-intensive system 会把上述若干组件用 application code 粘合起来。本书的目标是提供评估与选择工具、方法所需的框架和问题清单。
