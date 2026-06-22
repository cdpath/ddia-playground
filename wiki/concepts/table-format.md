---
title: "Table Format"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-lake, metadata, storage]
---

# Table Format

**Table format** 定义了哪些文件构成一张表、表的模式（schema）是什么，以及如何处理更新、删除和时间旅行。它位于 storage format（如 [[parquet]]）之上，query engine 之下。

## 说明

以 [[parquet]] 为代表的 storage format 文件一旦写入通常不可变。为了支持行级更新和删除，需要 table format 来管理文件集合和元数据版本。

常见 table format：

- [[apache-iceberg]]
- [[delta-lake]]
- Apache Hudi

Table format 提供的能力包括：

- 哪些文件属于当前版本的表。
- Schema evolution。
- 时间旅行（查询历史版本）。
- 垃圾回收（GC）未引用文件。

## 相关

- [[parquet]]
- [[data-lake]]
- [[apache-iceberg]]
- [[delta-lake]]
- [[data-catalog]]
- [[chapter-04]]
