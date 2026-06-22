---
title: "Vectorized Processing"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [query-execution, performance, analytics]
---

# Vectorized Processing

**Vectorized processing** 是数据库查询引擎一次处理一批列数据（而不是一次处理一行）的执行方式。它通过减少解释开销和利用 CPU 缓存、SIMD 指令来提升分析查询性能。

## 说明

在 vectorized processing 中，operator 接收一列或几列的批量数据，返回另一批结果。例如：

- 对 `product_sk` 列批量执行 `= 30`，返回一个 bitmap。
- 对 `store_sk` 列批量执行 `= 3`，返回另一个 bitmap。
- 对两个 bitmap 做按位 AND，得到满足两个条件的行集合。

由于处理的是连续内存中的列数据，可以：

- 提高 CPU cache 命中率。
- 使用 SIMD 指令并行处理多个值。
- 减少函数调用和分支预测失败。
- 直接在压缩数据上运算，避免解压。

## 与 query compilation 的对比

- **Vectorized processing**：保留解释器，用预定义 operator 批量处理数据。
- **[[query-compilation]]**：为每个查询生成专门的机器码。

两者都用于现代 OLAP 引擎，有时也结合使用。

## 相关

- [[query-compilation]]
- [[column-oriented-storage]]
- [[bitmap-index]]
- [[data-warehouse]]
- [[online-analytical-processing|OLAP]]
- [[chapter-04]]
