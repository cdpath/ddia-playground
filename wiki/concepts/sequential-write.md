---
title: "Sequential Write"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, performance]
---

# Sequential Write

**Sequential write** 是指把数据连续写入磁盘相邻位置的模式。与 [[random-write]] 相比，顺序写通常具有更高的吞吐。

## 说明

在机械硬盘上，顺序写避免了频繁的磁头寻道，因此远快于随机写。在 SSD 上，虽然没有机械部件，但顺序写仍然更快，因为：

- 顺序写更容易填满整个 erase block（通常 512 KiB）。
- 删除整个 block 时无需做大量 [[garbage-collection-ssd|garbage collection]]。
- 可以减少 SSD 的写放大和磨损。

[[lsm-tree]] 和 [[log-structured-storage]] 通过把随机写转换为顺序写，获得高写入吞吐。

## 相关

- [[random-write]]
- [[log-structured-storage]]
- [[lsm-tree]]
- [[write-amplification]]
- [[garbage-collection-ssd]]
- [[chapter-04]]
