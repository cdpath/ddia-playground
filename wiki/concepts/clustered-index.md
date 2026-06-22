---
title: "Clustered Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, index]
---

# Clustered Index

**Clustered index** 是把实际数据行（或文档）直接存储在索引结构中的索引。换句话说，索引的 leaf page 就是数据本身。

## 说明

在 clustered index 中，数据按索引 key 的排序顺序物理存放。这带来两个主要效果：

- 按主键做范围查询时，数据在磁盘上连续，I/O 效率高。
- 不需要先从索引找到指针再去别处读数据，减少了随机 I/O。

常见实现：

- [[mysql]] InnoDB：每个表的主键都是 clustered index。
- [[sql-server]]：可显式指定一个 clustered index。

Secondary index 在 clustered index 表中通常存储主键值，查询时需要两次查找：先在 secondary index 找到主键，再用主键查 clustered index。

## 相关

- [[index]]
- [[primary-index]]
- [[secondary-index]]
- [[heap-file]]
- [[covering-index]]
- [[storage-engine]]
- [[chapter-04]]
