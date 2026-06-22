---
title: "Denormalization"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-modeling, performance]
---

# Denormalization

**Denormalization** 是有意引入数据冗余，以换取更快读取性能的技术。与 [[normalization]] 相反，它把相关数据复制到需要读取的地方，减少 [[join]] 次数。

## 例子

- 在 [[twitter|X/Twitter]] home timeline 中，把每个用户的 timeline 预先计算出来并存入 cache，就是一种 denormalized view（本质上是 [[materialized-view]]）。
- 在 [[data-warehouse]] 中，把 dimension 信息折叠进 fact table，形成 one big table（OBT）。

## 优缺点

- **优点**：读更快，因为不需要 join；查询更简单。
- **缺点**：写更慢、占用更多存储、需要维护多份副本的一致性。

## 与 derived data 的关系

Denormalized 数据可以看作一种 [[derived-data-system]]：只要 source of truth 还在，就可以从 source 重新生成 denormalized 副本。

## 适用场景

- 读多写少，尤其是 analytics。
- 大规模系统里 join 成本过高。
- 可接受最终一致性。

## 相关

- [[normalization]]
- [[materialized-view]]
- [[derived-data-system]]
- [[cache]]
- [[chapter-02]]、[[chapter-03]]
