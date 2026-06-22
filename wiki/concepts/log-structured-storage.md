---
title: "Log-Structured Storage"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, oltp, lsm-tree, append-only]
---

# Log-Structured Storage

**Log-structured storage** 是一种只追加（append-only）、不可变（immutable）数据的存储方式。它把写入看成不断向 log 追加记录，并通过后台合并（compaction）来回收旧数据、减少空间占用。

## 说明

在 log-structured storage 中，更新操作并不覆盖旧值，而是写入一条新记录；删除则写入一条 [[tombstone]] 标记。读取时需要找到最新（或唯一有效）的那条记录。

核心优势：

- 写入模式是**顺序写**（sequential write），在磁盘和 SSD 上通常都比随机写更快。
- 文件一旦写成就不可变，崩溃恢复简单：未完成的文件直接丢弃即可。
- 天然适合做快照和增量备份。

核心劣势：

- 读取时可能需要检查多个文件才能找到最新值（[[read-amplification]]）。
- 后台 compaction 会占用磁盘带宽和 CPU，可能与写入竞争资源。
- 删除的数据不会立即消失，必须等 tombstone 被 compaction 推至最老层才能彻底清除。

## 典型实现

- [[lsm-tree]]：最经典的 log-structured index，使用 [[memtable]] + [[sstable]] + compaction。
- 文件系统：log-structured file system（LFS）是早期 inspiration。
- 搜索索引：[[lucene]] 的 segment 文件也采用类似 log-structured 的合并策略。

## 相关

- [[lsm-tree]]
- [[sstable]]
- [[memtable]]
- [[compaction]]
- [[tombstone]]
- [[sequential-write]]
- [[write-amplification]]
- [[read-amplification]]
- [[chapter-04]]
