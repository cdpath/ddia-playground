---
title: "B-Tree"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-structures, storage, index]
---

# B-Tree

**B-tree** 是一种自平衡的树状数据结构，1970 年由 Bayer 和 McCreight 提出。它是数据库中最常用的索引实现，广泛应用于关系型数据库（如 [[postgresql]]、[[mysql]] InnoDB、[[sql-server]]）和许多非关系型数据库。

> 可运行示例：[LSM-tree vs B-tree 的读写权衡](../../playgrounds/ch04-storage-and-retrieval/01-lsm-vs-btree.ipynb)

## 说明

B-tree 把数据分成固定大小的 **page**（块），传统大小为 4 KiB，PostgreSQL 默认 8 KiB，MySQL InnoDB 默认 16 KiB。每个 page 包含若干 key 和指向子 page 的引用，子 page 负责一个连续的 key range。

查找 key 时，从 root page 开始，根据 key 的范围逐层下放到 leaf page，通常只需 3~4 次 page 访问。一棵 4 KiB page、branching factor 为 500 的四层 B-tree 可存储约 250 TB。

## 更新操作

- **更新已有 key**：找到 leaf page，覆写该 page。
- **插入新 key**：找到目标 page，若空间不足则把 page 分裂成两个半满的 page，并更新父 page；分裂可能一直传到 root。
- **删除 key**：可能触发 page 合并，逻辑较复杂。

## 可靠性

因为 B-tree 需要原地覆写多个 page（如 page split），崩溃可能导致树结构损坏。因此 B-tree 实现通常依赖 [[write-ahead-log|WAL]] 来恢复一致性。某些实现（如 [[lmdb]]）采用 copy-on-write 代替 WAL。

## B-tree 变体

- **B+ tree**：数据全部放在 leaf page，内部 page 只存 key 边界；leaf page 之间用兄弟指针连接，便于范围扫描。
- **Copy-on-write B-tree**：修改 page 时写到新位置，并沿路径更新父 page，得到 immutable snapshot。
- **缩写 key**：内部 page 只存足够区分范围的 key 前缀，提高 branching factor。

## 相关

- [[index]]
- [[storage-engine]]
- [[write-ahead-log]]
- [[lsm-tree]]
- [[write-amplification]]
- [[fragmentation]]
- [[chapter-04]]
