---
title: "Roaring Bitmaps"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-structures, compression, analytics]
---

# Roaring Bitmaps

**Roaring bitmaps** 是一种压缩 bitmap 数据结构，能够根据数据稀疏程度在多种内部表示之间自适应切换，兼顾存储空间和位运算速度。

## 说明

Roaring 把 32 位整数空间切分成 2^16 个 chunk（高 16 位），每个 chunk 内部根据元素数量选择以下表示之一：

- **Array container**：元素较少时，用 16 位整数数组存储。
- **Bitmap container**：元素较多时，用 65536 位的普通 bitmap。
- **Run container**：存在长连续段时，用 run-length encoding。

这种自适应策略让 Roaring bitmaps 在稀疏和密集场景下都能保持紧凑，同时支持高效的并集、交集、差集等位运算。

## 应用

- 数据库中的 [[bitmap-index]] 压缩。
- 图查询中的邻接集合表示。
- 搜索引擎中的 postings list。

## 相关

- [[bitmap-index]]
- [[run-length-encoding]]
- [[column-compression]]
- [[inverted-index]]
- [[chapter-04]]
