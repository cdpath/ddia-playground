---
title: "Apache Arrow"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [serialization, data-formats, columnar, in-memory]
---

# Apache Arrow

**Apache Arrow** 是一种跨语言的列式内存数据格式，提供高性能的数据交换和计算接口。

## 说明

Arrow 不定义磁盘文件格式，而是定义内存中的列式布局标准。它使得不同系统（如 Pandas、Spark、Polars、DuckDB）之间可以零拷贝共享数据，减少序列化开销。

Arrow 常被用于：

- 数据分析库之间的数据交换。
- 向量化执行引擎的内存表示。
- 流式和 RPC 数据传输。

## 相关

- [[column-oriented-storage]]
- [[vectorized-processing]]
- [[parquet]]
- [[pandas]]
- [[numpy]]
- [[spark]]
- [[duckdb]]
- [[chapter-04]]
