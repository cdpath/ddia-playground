---
title: "Heap File"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage]
---

# Heap File

**Heap file** 是数据库中一种无特定顺序存储数据行的文件。索引中只保存指向 heap file 中具体位置的引用；实际数据按插入顺序或可用空间复用顺序存放，没有排序保证。

## 说明

在 heap file 方案中：

- 索引（通常是 [[secondary-index]]）存储的是数据在 heap file 中的物理位置或主键。
- 更新数据时，如果新值比旧值大，可能需要把记录移到 heap file 的新位置，并更新所有索引。
- 也可以保留一个 forwarding pointer，让旧位置指向新位置，避免更新所有索引。

[[postgresql]] 使用 heap file 方式组织表数据：表的 heap 文件不保证行顺序，索引保存行的物理位置（tid）。

## 优缺点

- **优点**：插入简单，不需要维护排序；更新不移动行时效率高。
- **缺点**：按索引顺序读取时会产生大量随机 I/O；表可能产生碎片，需要 vacuum 等维护操作。

## 相关

- [[index]]
- [[clustered-index]]
- [[covering-index]]
- [[storage-engine]]
- [[fragmentation]]
- [[chapter-04]]
