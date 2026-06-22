---
title: "Full-Text Search"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, search, information-retrieval]
---

# Full-Text Search

**Full-text search** 是一种在文本集合中按关键词查找相关文档的能力。它广泛应用于网页搜索、电商商品搜索、文档检索等场景。

## 说明

Full-text search 可以看作一种特殊的多维查询：每个可能出现的词（term）是一个维度，包含该词的文档在该维度上为 1，否则为 0。搜索“red apples”即寻找在 `red` 和 `apples` 两个维度上都为 1 的文档。

实际实现远比这复杂，还涉及：

- 分词与语言处理（尤其对中文、日文等无空格语言）。
- 词干提取、拼写纠错、同义词。
- 相关性排序（如 TF-IDF、BM25）。

本书主要关注底层数据结构：[[inverted-index]]。

## 核心数据结构

- [[inverted-index]]：从 term 映射到包含该 term 的文档 ID 列表（[[postings-list]]）。
- [[n-gram]]：把文本切成固定长度子串，用于子串匹配和正则搜索。

## 相关系统

- [[lucene]]、[[elasticsearch]]、[[solr]]
- [[postgresql]] 的 GIN / GIST 索引

## 相关

- [[search-index]]
- [[inverted-index]]
- [[postings-list]]
- [[n-gram]]
- [[semantic-search]]
- [[vector-embedding]]
- [[chapter-04]]
