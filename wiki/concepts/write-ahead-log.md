---
title: "Write-Ahead Log"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, durability, crash-recovery]
---

# Write-Ahead Log

**Write-ahead log**（**WAL**，又称 journal）是一种追加写入的日志，用于保证数据持久性和崩溃恢复。数据库在把数据真正写入数据结构（如 B-tree page 或 memtable）之前，先把修改记录追加到 WAL。

## 说明

WAL 的核心原则是**先写日志，再写数据**：任何对数据文件的修改必须先记录到 WAL 并刷盘（fsync），才能在崩溃后恢复。

在 [[b-tree]] 存储引擎中，WAL 记录每次 page 修改，崩溃后通过重放日志把树恢复到一致状态。在 [[lsm-tree]] 中，WAL 用于恢复内存中的 [[memtable]]，一旦 memtable 被 flush 成 [[sstable]]，对应 WAL 段即可丢弃。

## 作用

- 保证已提交写入不会因崩溃丢失（durability）。
- 允许延迟把脏页写回磁盘，提高写性能。
- 把随机写变成对日志文件的顺序写。

## 相关

- [[storage-engine]]
- [[b-tree]]
- [[lsm-tree]]
- [[memtable]]
- [[fault-tolerance]]
- [[chapter-04]]
