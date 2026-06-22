---
title: "Vector Embedding"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [ai, embeddings, search]
---

# Vector Embedding

**Vector embedding** 是将文本、图像、音频等内容表示成高维浮点数向量的技术。语义相近的内容在向量空间中的距离也相近。

## 说明

Embedding model（通常是神经网络）把输入映射成向量。例如：

- “agriculture” → [0.38, 0.83, 0.41]
- “vegetables” → [0.36, 0.64, 0.67]
- “star schema” → [0.85, 0.10, -0.52]

前两个向量距离近，后一个距离远。实际使用的向量通常有上千维。

## 历史模型

- 文本：Word2Vec、BERT、GPT。
- 现代模型多为多模态，可同时处理文本、图像、音频。

## 距离度量

常用距离函数包括余弦相似度（cosine similarity）和欧氏距离（Euclidean distance）。

## 相关

- [[semantic-search]]
- [[vector-index]]
- [[hnsw]]
- [[ivf]]
- [[flat-index]]
- [[chapter-04]]
