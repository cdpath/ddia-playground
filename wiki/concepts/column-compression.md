---
title: "Column Compression"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, compression, analytics]
---

# Column Compression

**Column compression** 是对 [[column-oriented-storage|列式存储]] 中各列分别进行压缩的技术。由于同一列的数据类型相同、重复值多，压缩效果通常远好于行式存储。

## 常见技术

- **Bitmap encoding**：把低基数列转成若干 bitmap，每个 distinct value 对应一个 bitmap，第 k 位为 1 表示第 k 行等于该值。
- **Run-length encoding (RLE)**：记录连续相同值的长度，对排序后的高重复列特别有效。
- **Roaring bitmaps**：在稀疏和密集场景间自适应切换，兼顾存储空间和位运算效率。

## 好处

- 减少磁盘占用。
- 降低查询时的磁盘 I/O 和网络带宽。
- 有时可以直接在压缩数据上执行位运算，避免解压。

## 相关

- [[column-oriented-storage]]
- [[bitmap-index]]
- [[run-length-encoding]]
- [[roaring-bitmaps]]
- [[data-warehouse]]
- [[chapter-04]]
