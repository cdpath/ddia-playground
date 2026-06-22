---
title: "Inverted Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, index, information-retrieval]
---

# Inverted Index

**Inverted index** 是全文搜索的核心数据结构。它把每个词（term）映射到包含该词的文档 ID 列表，这个列表称为 [[postings-list]]。

## 说明

Inverted index 的结构类似于 key-value store：

- Key：term（词）
- Value：postings list（包含该 term 的文档 ID 列表）

搜索多个 term 时，分别取出各 term 的 postings list，然后求交集（AND）或并集（OR）。

如果文档 ID 是连续整数，postings list 也可以表示为稀疏 bitmap，从而利用高效的位运算。这与 [[bitmap-index]] 思想相同。

## 实现

许多搜索引擎的倒排索引采用 [[log-structured-storage]]方式管理：term 到 postings list 的映射存储在 [[sstable]] 类似的不可变文件中，并在后台合并。

## 相关系统

- [[lucene]]、[[elasticsearch]]、[[solr]]
- [[postgresql]] GIN 索引

## 相关

- [[full-text-search]]
- [[postings-list]]
- [[bitmap-index]]
- [[n-gram]]
- [[search-index]]
- [[chapter-04]]
