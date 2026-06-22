---
title: "Postings List"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, information-retrieval]
---

# Postings List

**Postings list** 是 [[inverted-index]] 中每个 term 对应的文档 ID 列表，记录包含该 term 的所有文档。

## 说明

在 full-text search 中，每个 term 都对应一个 postings list。例如：

- term “apple” → postings list: [doc_1, doc_5, doc_12]
- term “banana” → postings list: [doc_2, doc_5]

查询 “apple AND banana” 时，对两个 postings list 求交集，得到 [doc_5]。

## 表示方式

- 有序整数列表：便于合并和求交集。
- Bitmap：当文档 ID 连续时，可用稀疏 bitmap 表示，配合 [[run-length-encoding]] 或 [[roaring-bitmaps]] 压缩。

## 相关

- [[inverted-index]]
- [[full-text-search]]
- [[bitmap-index]]
- [[roaring-bitmaps]]
- [[chapter-04]]
