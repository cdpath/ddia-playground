---
title: "Parquet"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [serialization, data-formats, columnar]
---

# Parquet

Apache Parquet 是一种面向列的二进制文件格式，广泛用于 [[data-lake]]、[[data-warehouse]] 和大数据分析。它基于 Google Dremel 论文，通过 shredding（striping）技术支持嵌套文档数据模型。

## 说明

Parquet 把数据按列而不是按行存储。这样，分析查询只需读取所需列，大幅减少 I/O。每个列的值在文件内部按块组织，并支持多种压缩和编码方式。

Parquet 文件一旦写入通常不可变。为了支持更新和删除，需要配合 [[apache-iceberg]]、[[delta-lake]] 等 table format，通过新增文件和元数据版本管理来实现。

## 相关

- [[column-oriented-storage]]
- [[column-compression]]
- [[data-lake]]
- [[data-warehouse]]
- [[apache-arrow]]
- [[apache-iceberg]]
- [[delta-lake]]
- [[chapter-04]]
- [[chapter-05]]
