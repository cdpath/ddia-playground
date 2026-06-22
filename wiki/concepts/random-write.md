---
title: "Random Write"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, performance]
---

# Random Write

**Random write** 是指写入位置分散在磁盘不同区域的写模式。与 [[sequential-write]] 相比，随机写通常吞吐较低。

## 说明

[[b-tree]] 等原地更新存储引擎容易产生随机写：当应用写入散布在整个 key space 的 key 时，需要覆写的 page 也可能散布在磁盘各处。

随机写在机械硬盘上尤其慢，因为需要频繁移动磁头。在 SSD 上，随机写会导致：

- 更多 [[garbage-collection-ssd|garbage collection]]，消耗写带宽。
- 更高 [[write-amplification]]，加速 SSD 磨损。

## 相关

- [[sequential-write]]
- [[b-tree]]
- [[storage-engine]]
- [[write-amplification]]
- [[garbage-collection-ssd]]
- [[chapter-04]]
