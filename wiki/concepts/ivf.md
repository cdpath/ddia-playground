---
title: "Inverted File Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, ai, index]
---

# Inverted File Index

**Inverted file index**（**IVF**）是一种 [[vector-index]]。它把向量空间聚类成若干分区（centroids），查询时只检查与查询向量最接近的少数分区，从而减少距离计算量。

## 说明

IVF 工作流程：

1. 训练阶段：用聚类算法（如 k-means）把向量库分成若干 centroid。
2. 存储阶段：每个向量归属于最近的 centroid。
3. 查询阶段：计算查询向量与 centroids 的距离，选择最近的若干个分区（probes），然后只在这些分区内部做精确比较。

## 权衡

- **probes 越多**：精度越高，速度越慢。
- **probes 越少**：速度越快，但可能漏掉真正的近邻（因为查询向量与目标向量可能被分到不同分区）。

IVF 通常比 [[flat-index]] 快，但结果是近似的。

## 相关

- [[vector-index]]
- [[vector-embedding]]
- [[hnsw]]
- [[flat-index]]
- [[semantic-search]]
- [[chapter-04]]
