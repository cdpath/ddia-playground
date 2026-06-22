---
title: "Multidimensional Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [index, storage, spatial]
---

# Multidimensional Index

**Multidimensional index** 是能够同时查询多个维度的索引。与只能按单一 key range 查询的 [[b-tree]] 或 [[lsm-tree]] 不同，多维索引支持如“纬度在某范围且经度在某范围”的二维范围查询。

## 说明

最简单的多维索引是**拼接索引**（concatenated index）：把多个列拼接成一个复合 key。但它的查询能力受限：只能利用前缀列做范围裁剪。例如按 `(lastname, firstname)` 拼接的索引可以高效查找某个 lastname，但无法高效查找某个 firstname。

真正的多维索引需要把空间划分为区域，使相近的数据点倾向于落在同一子树。常见实现包括：

- [[r-tree]] 及其变体（如 Bkd-tree）。
- [[space-filling-curve]]（如 Z-order、Hilbert curve）把多维坐标映射为一维，再用普通 B-tree 索引。
- 规则网格或六边形层级索引（如 Uber H3）。

## 应用场景

- 地理空间：查找地图矩形范围内的餐厅。
- 颜色空间：在电商中按 RGB 范围搜索商品。
- 时间序列：按 `(date, temperature)` 搜索某年温度在 25~30°C 的观测。

## 相关

- [[r-tree]]
- [[space-filling-curve]]
- [[index]]
- [[b-tree]]
- [[chapter-04]]
