---
title: "Sorted Strings Table"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, lsm-tree, file-format]
---

# Sorted Strings Table

**Sorted Strings Table**（**SSTable**）是一种存储 key-value 对的文件格式，要求文件内所有 key 按字典序排序，且同一个 key 只出现一次。SSTable 是 [[lsm-tree]] 存储引擎的核心构建块。

## 说明

SSTable 文件通常被切分为若干块（block，大小为数 KB），每个块内部存储连续的 key-value 对。由于 key 已排序，可以用**稀疏索引**（sparse index）只记录每个块的起始 key 和文件偏移量，而不需要把所有 key 都保留在内存中。

查找一个 key 时：

1. 在稀疏索引中定位到可能包含该 key 的块。
2. 读取对应块（可能已压缩）。
3. 在块内扫描或二分查找。

## 特点

- **不可变**：SSTable 一旦写入就不再修改，简化并发和崩溃恢复。
- **可压缩**：整块压缩可节省磁盘空间并减少 I/O 带宽。
- **可合并**：多个 SSTable 可以用类似 mergesort 的方式合并，保留最新值、丢弃删除标记。
- **可配合 Bloom filter**：每个 SSTable 可附带 [[bloom-filter]]，快速判断 key 是否可能存在于该文件中。

## 与 memtable 的关系

[[memtable]] 是内存中的有序结构，用于吸收写入；当 memtable 满时，它被刷新（flush）成一个新的 SSTable 文件。

## 相关

- [[lsm-tree]]
- [[memtable]]
- [[compaction]]
- [[bloom-filter]]
- [[storage-engine]]
- [[chapter-04]]
