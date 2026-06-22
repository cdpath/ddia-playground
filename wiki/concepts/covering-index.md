---
title: "Covering Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, index]
---

# Covering Index

**Covering index**（又称 index with included columns）是一种把查询所需的部分列直接存储在索引中的 secondary index。当查询所需的所有列都在索引中时，数据库无需再回表查主数据，这种查询被称为“被索引覆盖”（covered by the index）。

## 说明

Covering index 是 [[clustered-index]] 和 [[heap-file]] 之间的折中：

- 它不像 clustered index 那样存储整行数据，只存储查询常用的列。
- 它可以避免从索引跳到 heap 或 clustered index 的额外 I/O。

## 权衡

- **优点**：某些查询可以完全靠索引回答，速度更快。
- **缺点**：索引占用更多磁盘空间；写入时需要维护更多数据，写放大增加。

## 相关

- [[index]]
- [[secondary-index]]
- [[clustered-index]]
- [[heap-file]]
- [[storage-engine]]
- [[chapter-04]]
