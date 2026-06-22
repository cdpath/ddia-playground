---
title: "Lucene"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [search, information-retrieval, library]
---

# Lucene

**Apache Lucene** 是开源的全文搜索引擎库，是许多搜索产品的基础。它使用 [[inverted-index]] 和 [[log-structured-storage]] 方式管理 segment 文件。

## 特点

- 核心数据结构是 term 到 [[postings-list]] 的映射。
- Segment 文件不可变，后台合并（merge）与 [[lsm-tree]] 的 compaction 思想类似。
- 支持模糊查询、同义词、拼写纠错、n-gram 等高级功能。

## 相关

- [[full-text-search]]
- [[inverted-index]]
- [[postings-list]]
- [[log-structured-storage]]
- [[elasticsearch]]
- [[solr]]
- [[chapter-04]]
