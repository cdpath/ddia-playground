---
title: "Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, query-optimization]
---

# Index

**Index** 是从主数据派生出来的额外数据结构，用于加速查询。索引本身不影响数据库内容，但会影响查询性能和写入开销。

## 说明

没有索引时，查找特定 key 需要扫描全部数据（O(n)）。索引通过把数据按某种方式组织（如排序、哈希、空间划分）来快速定位目标记录。

索引的权衡：

- **优点**：显著加速读查询，尤其是点查和范围查询。
- **缺点**：占用额外磁盘空间；每次写入都需要更新索引，从而降低写入速度。

因此数据库通常不会自动为所有列建索引，而由应用开发者根据查询模式选择。

## 常见类型

- [[primary-index]] / [[secondary-index]]
- [[b-tree]]
- [[lsm-tree]]
- [[bitmap-index]]
- [[inverted-index]]（用于 full-text search）
- [[multidimensional-index]] / [[r-tree]]（用于空间数据）
- [[vector-index]]（用于语义搜索）

## 相关

- [[primary-index]]
- [[secondary-index]]
- [[clustered-index]]
- [[covering-index]]
- [[heap-file]]
- [[storage-engine]]
- [[query-language]]
- [[chapter-04]]
