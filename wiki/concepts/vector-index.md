---
title: "Vector Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, ai, index]
---

# Vector Index

**Vector index** 是用于存储和查询高维 [[vector-embedding]] 的索引结构。给定一个查询向量，vector index 返回与之最相似的若干文档向量。

## 说明

由于 [[r-tree]] 等传统空间索引在高维空间效果不佳，vector index 通常采用近似最近邻（ANN）算法，在精度和速度之间权衡。

常见类型：

- [[flat-index]]：精确但慢，需扫描全部向量。
- [[ivf]]：把向量空间聚类成若干分区，只搜索最相关的分区。
- [[hnsw]]：构建多层图结构，通过贪心导航快速定位近邻。

## 典型系统

- Facebook Faiss
- PostgreSQL pgvector
- Pinecone、Weaviate、Milvus、Qdrant

## 相关

- [[vector-embedding]]
- [[semantic-search]]
- [[hnsw]]
- [[ivf]]
- [[flat-index]]
- [[search-index]]
- [[chapter-04]]
