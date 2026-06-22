---
title: "Bitmap Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, index, analytics]
---

# Bitmap Index

**Bitmap index** 是一种把列的每个 distinct value 表示为一个 bitmap 的索引。bitmap 的第 k 位为 1 表示第 k 行具有该值。

## 说明

Bitmap index 特别适合基数较低的列（例如“产品类别”“门店 ID”），因为这类列的 distinct value 数量远小于行数。

查询示例：

- `WHERE product_sk IN (31, 68, 69)`：把三个 value 对应的 bitmap 做按位 OR。
- `WHERE product_sk = 30 AND store_sk = 3`：把两个列的 bitmap 做按位 AND。

由于列式存储中各列行顺序一致，不同列的 bitmap 可以直接按位运算。

## 压缩

Bitmap 通常很稀疏，因此常用 [[run-length-encoding]] 或 [[roaring-bitmaps]] 压缩。

## 相关

- [[column-oriented-storage]]
- [[column-compression]]
- [[run-length-encoding]]
- [[roaring-bitmaps]]
- [[inverted-index]]
- [[chapter-04]]
