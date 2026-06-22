---
title: "Semantic Search"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, ai, embeddings]
---

# Semantic Search

**Semantic search** 超越关键词匹配，试图理解文档概念和用户意图。例如搜索 “how to close my account” 也能找到标题为 “canceling your subscription” 的页面，因为二者语义相近。

## 说明

Semantic search 通常使用 [[vector-embedding]] 把文本、图像、音频等转换成高维向量。语义相近的内容在向量空间中距离较近。查询时，把查询文本也转成向量，然后在 [[vector-index]] 中查找最相似的向量。

## 应用场景

- 检索增强生成（RAG）：把搜索结果注入大语言模型上下文。
- 企业知识库问答。
- 跨语言搜索。
- 以图搜图、以文搜图。

## 相关

- [[vector-embedding]]
- [[vector-index]]
- [[hnsw]]
- [[ivf]]
- [[flat-index]]
- [[full-text-search]]
- [[chapter-04]]
