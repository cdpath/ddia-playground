---
title: "Hierarchical Navigable Small World"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, ai, index]
---

# Hierarchical Navigable Small World

**Hierarchical Navigable Small World**（**HNSW**）是一种基于图的近似最近邻 [[vector-index]]。它通过构建多层图结构，使查询能够快速导航到与查询向量最近的区域。

## 说明

HNSW 把向量组织成若干层：

- 顶层节点稀疏，层间通过同一节点连接。
- 底层节点密集，包含完整的近邻关系。

查询时，先在顶层找到最近的节点，然后下沉到下一层的同一节点，沿着该层的边继续向更靠近查询向量的节点移动，直到最底层。

## 特点

- 查询速度快。
- 构建索引时内存和计算开销较大。
- 结果是近似 nearest neighbor。

## 典型实现

- Facebook Faiss
- PostgreSQL pgvector（HNSW 索引）
- Pinecone、Weaviate、Milvus、Qdrant

## 相关

- [[vector-index]]
- [[vector-embedding]]
- [[ivf]]
- [[flat-index]]
- [[semantic-search]]
- [[chapter-04]]
