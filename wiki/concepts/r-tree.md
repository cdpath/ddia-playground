---
title: "R-Tree"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-structures, index, spatial]
---

# R-Tree

**R-tree** 是一种用于多维空间数据索引的平衡树结构。它把空间划分为嵌套的矩形区域（bounding box），使空间上相近的数据点倾向于存储在同一子树。

## 说明

R-tree 的每个节点对应一个最小外接矩形（MBR），子节点对应的矩形完全包含在父节点的矩形内。查询时，从根节点开始，只访问与查询范围相交的矩形分支，从而避免扫描全表。

R-tree 常用于二维或三维空间数据，如地理坐标、边界框、几何对象。

## 典型实现

- [[postgis]] 基于 PostgreSQL 的 GiST 索引实现地理空间索引。
- 许多 GIS 和数据库系统使用 R-tree 或 R-tree 变体处理空间查询。

## 局限

R-tree 对高维数据效果不佳（维度灾难），因此不适合 [[vector-embedding]] 等高维向量的近似最近邻搜索。

## 相关

- [[multidimensional-index]]
- [[space-filling-curve]]
- [[index]]
- [[vector-index]]
- [[chapter-04]]
