---
title: "Memtable"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, lsm-tree, in-memory]
---

# Memtable

**Memtable** 是 [[lsm-tree]] 存储引擎中驻留内存的有序数据结构，用于吸收最近的写入。当 memtable 达到一定阈值后，会被刷新（flush）成磁盘上的 [[sstable]] 文件。

## 说明

Memtable 需要支持：

- 任意顺序插入 key。
- 快速按 key 查找。
- 按 key 顺序遍历，以便 flush 成有序的 SSTable。

常用实现包括红黑树、跳表（skip list）或 trie。

## 持久化

由于 memtable 在内存中，崩溃会丢失数据。因此写入 memtable 的同时，必须先把写操作追加到 [[write-ahead-log|WAL]]。重启时通过重放 WAL 恢复 memtable。

当一个 memtable 被 flush 成 SSTable 后，对应的 WAL 段就可以被安全丢弃。

## 相关

- [[lsm-tree]]
- [[sstable]]
- [[write-ahead-log]]
- [[compaction]]
- [[storage-engine]]
- [[chapter-04]]
