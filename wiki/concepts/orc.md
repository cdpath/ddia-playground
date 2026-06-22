---
title: "ORC"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [serialization, data-formats, columnar]
---

# ORC

**ORC**（Optimized Row Columnar）是 Hadoop 生态中的列式二进制文件格式，针对大规模分析查询优化。

## 说明

ORC 与 [[parquet]] 类似，都使用 [[column-oriented-storage|列式存储]] 和 [[column-compression|列压缩]]。它支持 predicate pushdown、轻量级索引和多种压缩编码，常用于 Hive、Spark 等系统。

## 相关

- [[parquet]]
- [[column-oriented-storage]]
- [[column-compression]]
- [[data-lake]]
- [[apache-hive]]
- [[spark]]
- [[chapter-04]]
