---
title: "DataFrame"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, analytics, machine-learning]
---

# DataFrame

**DataFrame** 是一种面向数据科学和分析的 data model，类似 spreadsheet 或 relational table，但提供比 SQL 更灵活的程序化操作接口。

## 支持系统

- R 语言
- Python 的 [[pandas]]、[[dask]]
- [[spark|Apache Spark]]
- [[arcticdb]]
- Apache Flink（也提供 DataFrame API）

## 典型操作

- 对整列或整行应用函数。
- 按条件过滤。
- 分组聚合。
- 基于 key merge（相当于 SQL join）。
- 把关系数据 pivot 成矩阵。

## 与 relational model 的区别

DataFrame 通常不是声明式查询语言，而是一系列逐步变换命令。数据科学家常在本地私有副本上迭代处理，而不是直接操作共享数据库。

## 与 ML 的衔接

DataFrame 可方便地把关系表转换为 sparse matrix 或 multidimensional array，供 ML 算法使用。常用技术包括 one-hot encoding。

## 相关

- [[array-database]]
- [[pandas]]
- [[spark]]
- [[chapter-03]]
