---
title: "Data Locality"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, performance]
---

# Data Locality

**Data locality** 指相关数据在物理存储上是否彼此靠近。良好的 locality 能减少磁盘 seek 和网络往返，提高读取性能。

## Document model 中的 locality

Document 通常作为一个连续字符串（JSON/BSON）整体存储。如果应用经常需要一次性读取整个对象，这种 locality 非常有利。但如果只访问文档的一小部分，加载整个文档就浪费了。

## 更新代价

文档更新时通常需要重写整个文档，因此建议保持文档较小，避免频繁的小更新。

## Relational model 中的 locality

Relational database 也可以通过 clustered index、interleaved tables、multi-table index cluster tables 等机制实现 locality。例如：

- [[spanner]] 允许子表行嵌套在父表行中。
- Oracle 的 multi-table index cluster tables。
- Wide-column stores（如 [[bigtable]]、[[hbase]]）通过 column family 管理 locality。

## 相关

- [[document-model]]
- [[relational-model]]
- [[performance]]
- [[chapter-03]]
