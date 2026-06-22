---
title: "Normalization"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-modeling]
---

# Normalization

**Normalization** 是将数据组织成减少冗余、避免更新异常的结构的过程。核心思想是：把对人可读的信息集中存储，其他地方只引用其 ID。

## 例子

在用户信息中，用 `region_id` 引用 regions 表，而不是在每个用户记录里重复写 `Washington, DC, United States`。这样：

- 保持名称拼写一致。
- 避免同名歧义。
- 更新地名时只需改一处。
- 便于本地化（不同语言显示不同名称）。
- 通过 region 层级支持更好的搜索。

## 优缺点

- **优点**：减少冗余、避免不一致、写操作更快（只需改一处）。
- **缺点**：查询时通常需要 [[join]] 把 ID 解析成可读内容。

## 适用场景

- OLTP 系统，读写都频繁。
- 小到中等规模系统，join 成本可接受。
- 数据一致性要求高。

## 相关

- [[denormalization]]
- [[join]]
- [[relational-model]]
- [[chapter-03]]
