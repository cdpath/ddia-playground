---
title: "Fragmentation"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, maintenance, b-tree]
---

# Fragmentation

**Fragmentation** 指数据库文件中存在未被有效利用的空闲空间。它会导致文件比实际数据更大，并降低顺序 I/O 效率。

## 说明

在 [[b-tree]] 存储引擎中，随着大量 key 被删除，原本属于 B-tree 的 page 可能变成空闲，但由于它们位于文件中间，无法轻易归还操作系统。后续插入可以复用这些 page，但文件大小不会立即缩小。

例如，[[postgresql]] 需要通过 vacuum 等后台进程整理 page，回收空间并更新统计信息。

相比之下，[[lsm-tree]] 由于 compaction 会定期重写 segment 文件，碎片问题较轻。

## 相关

- [[b-tree]]
- [[storage-engine]]
- [[heap-file]]
- [[chapter-04]]
