---
title: "Tombstone"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, lsm-tree, deletion]
---

# Tombstone

**Tombstone** 是 [[log-structured-storage]] 中用于表示删除的特殊记录。删除 key 时不是真正删除旧数据，而是追加一条 tombstone 标记。

## 说明

在 [[lsm-tree]] 中，由于 segment 文件不可变，无法直接删除旧值。相反，系统写入一条 tombstone 记录。当 compaction 合并 segment 时，tombstone 会告诉合并过程丢弃该 key 的所有早期版本。

只有 tombstone 被 compaction 推送到最老的层级后，相关旧数据才会真正从磁盘消失。这意味着删除操作在空间回收上存在延迟，对数据保护合规（如 GDPR 彻底删除）可能带来挑战。

## 相关

- [[lsm-tree]]
- [[sstable]]
- [[compaction]]
- [[log-structured-storage]]
- [[chapter-04]]
