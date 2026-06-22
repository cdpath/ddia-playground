---
title: "Flat Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, ai, index]
---

# Flat Index

**Flat index** 是最简单的 [[vector-index]]：直接存储所有向量，查询时逐一计算查询向量与每个存储向量的距离。

## 说明

Flat index 的结果是精确的（exact nearest neighbor），但代价是必须扫描整个数据集。当向量数量很大或维度很高时，查询速度很慢。

因此 flat index 只适用于数据量较小或对精度要求极高的场景。大规模语义搜索通常使用 [[hnsw]] 或 [[ivf]] 等近似索引。

## 相关

- [[vector-index]]
- [[vector-embedding]]
- [[hnsw]]
- [[ivf]]
- [[semantic-search]]
- [[chapter-04]]
