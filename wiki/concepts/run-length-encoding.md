---
title: "Run-Length Encoding"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [compression, encoding, storage]
---

# Run-Length Encoding

**Run-length encoding**（**RLE**）是一种无损压缩技术，把连续重复的单个值表示为“值 + 重复次数”。例如序列 `aaaaabbbcc` 可编码为 `a5b3c2`。

## 说明

RLE 对具有长连续重复序列的数据非常有效。在数据库中，它常用于：

- [[bitmap-index]] 的压缩：记录连续 0 或 1 的段长度。
- [[column-oriented-storage|列式存储]] 中排序列的压缩：例如按日期排序后，同一日期的值会形成长连续段。

RLE 的压缩效果在第一排序键上最强；后续排序键值更分散，连续段较短。

## 相关

- [[column-compression]]
- [[bitmap-index]]
- [[roaring-bitmaps]]
- [[column-oriented-storage]]
- [[chapter-04]]
