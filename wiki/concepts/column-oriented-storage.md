---
title: "Column-Oriented Storage"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, analytics, olap]
---

# Column-Oriented Storage

**Column-oriented storage**（又称 columnar storage）是一种把表中每一列的值连续存放的存储布局。与 [[row-oriented-storage|行式存储]] 不同，它不把所有字段按行聚在一起，而是把同一列的所有值聚在一起。

## 说明

在列式存储中，每一列单独存储，且各列的行顺序保持一致。如果需要重组完整行，只需取各列的第 k 个值拼接即可。

实际实现通常不会把整个列存在一个文件中，而是把表切成包含成千上万行的块（block），每个块内再按列分别存储。为了支持按时间范围裁剪，常让每个块包含某段时间内的所有行。

## 为什么适合 OLAP

典型数据仓库查询只访问事实表中的 4~5 列，但需要扫描大量行。列式存储让查询只读取所需列，避免加载整行，从而显著减少 I/O。

## 相关技术

- [[column-compression]]：列内数据重复度高，适合压缩。
- [[bitmap-index]] / [[run-length-encoding]]：低基数列的有效编码。
- [[query-compilation]] / [[vectorized-processing]]：配合列式数据高效执行。

## 典型系统与格式

- 数据库：[[snowflake]]、Vertica、[[apache-pinot]]、[[apache-druid]]、[[clickhouse]]、[[duckdb]]、InfluxDB IOx、TimescaleDB。
- 文件格式：[[parquet]]、ORC、Lance、Nimble。
- 内存格式：Apache Arrow、Pandas/NumPy。

## 与 wide-column store 的区别

[[wide-column-store]]（如 [[bigtable]]、[[hbase]]）虽然名字带 column，但仍然是**行式存储**：同一行的所有列值存放在一起。

## 相关

- [[row-oriented-storage]]
- [[column-compression]]
- [[bitmap-index]]
- [[data-warehouse]]
- [[online-analytical-processing|OLAP]]
- [[chapter-04]]
