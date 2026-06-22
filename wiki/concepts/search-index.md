---
title: "Search index"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, search]
---

# Search index

**Search index** 让用户能够按关键词或以多种方式过滤数据。它是 [[data-intensive-application]] 的标准组件之一。

与 [[cache]] 类似，search index 通常也是一种 [[derived-data-system]] — 如果丢失，可以从 source data 重建。

## 常见实现

- [[inverted-index]]：全文搜索引擎（如 [[lucene]]）使用 term 到文档列表的映射。
- [[vector-index]]：语义搜索使用向量近似最近邻索引（如 [[hnsw]]、[[ivf]]）。
- [[b-tree]] / [[multidimensional-index]]：结构化数据的索引。

## 相关

- [[cache]]
- [[derived-data-system]]
- [[full-text-search]]
- [[inverted-index]]
- [[vector-index]]
- [[chapter-04]]
