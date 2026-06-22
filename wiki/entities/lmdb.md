---
title: "LMDB"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, storage-engine, b-tree, embedded]
---

# LMDB

**LMDB**（Lightning Memory-Mapped Database）是一个使用 copy-on-write B-tree 的嵌入式 key-value [[storage-engine]]。

## 特点

- 使用 memory-mapped I/O 和 copy-on-write 技术，读写性能高。
- 不需要 [[write-ahead-log|WAL]]，通过 immutable snapshot 实现崩溃恢复和并发控制。
- 适合读多写少、需要快速查找的嵌入场景。

## 相关

- [[b-tree]]
- [[storage-engine]]
- [[embedded-database]]
- [[chapter-04]]
