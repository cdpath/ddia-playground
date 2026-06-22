---
title: "Secondary Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, index]
---

# Secondary Index

**Secondary index** 是建立在非主键列上的索引，允许通过主键以外的属性查询数据。在关系型数据库中，可用 `CREATE INDEX` 创建多个 secondary index。

## 说明

Secondary index 的 key 不唯一：多个行可能对应同一个索引值。实现方式通常有两种：

1. **Postings list**：每个索引值对应一个行 ID 列表，类似 [[inverted-index]]。
2. **唯一化**：把行 ID 拼接到索引值后面，使每个索引项唯一。

Secondary index 会增加写入开销，因为每次插入、更新、删除行时，所有相关索引都需要更新。过多的 secondary index 会显著降低写入吞吐。

## 相关

- [[index]]
- [[primary-index]]
- [[covering-index]]
- [[inverted-index]]
- [[postings-list]]
- [[storage-engine]]
- [[chapter-04]]
