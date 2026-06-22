---
title: "Join"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, query-languages]
---

# Join

**Join** 是根据共同字段把多张表的数据组合起来的操作，是 relational model 的核心能力之一。

## 为什么需要 join

在 [[normalization|normalized]] schema 中，相关数据分散在不同表里。例如 `users` 表存 `region_id`，真实地区名在 `regions` 表。要同时显示用户信息和地区名，就需要 join：

```sql
SELECT users.*, regions.region_name
FROM users
JOIN regions ON users.region_id = regions.id
WHERE users.id = 251;
```

## Join 与 graph 查询

Graph 查询中每遍历一条边，本质上都相当于与 edges 表做一次 join。区别在于 graph 查询的遍历深度往往不固定，需要用 recursive CTE 等机制表达。

## 优缺点

- **优点**：保持数据 normalized，避免冗余；表达力强。
- **缺点**：在大规模系统里 join 可能成为性能瓶颈。

## 相关

- [[relational-model]]
- [[normalization]]
- [[denormalization]]
- [[graph-data-model]]
- [[chapter-03]]
