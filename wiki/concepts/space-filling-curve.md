---
title: "Space-Filling Curve"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [algorithms, spatial, index]
---

# Space-Filling Curve

**Space-filling curve** 是一种把多维空间映射到一维连续曲线的技术。通过这种方式，可以用普通的 [[b-tree]] 索引来近似支持多维范围查询。

## 说明

常见的 space-filling curve 包括：

- **Z-order curve**（Morton order）
- **Hilbert curve**

它们把二维 (x, y) 坐标编码成一个一维值，同时尽量保持局部性：在多维空间中相近的点，在一维编码后也倾向于相近。

## 在数据库中的应用

对于地理空间查询，可以把经纬度通过 space-filling curve 编码成一个数值 key，然后用 B-tree 索引。查询时把多维范围拆分成若干一维区间，再在 B-tree 中查找。

这种方法实现简单，但不如专门的 [[r-tree]] 等空间索引精确，可能产生额外的候选点需要过滤。

## 相关

- [[multidimensional-index]]
- [[r-tree]]
- [[index]]
- [[b-tree]]
- [[chapter-04]]
