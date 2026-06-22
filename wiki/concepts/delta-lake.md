---
title: "Delta Lake"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-lake, table-format, acid]
---

# Delta Lake

**Delta Lake** 是由 Databricks 开发的开放 table format，基于 [[parquet]] 文件和事务日志，为 [[data-lake]] 提供 ACID 事务、版本控制和时间旅行能力。

## 说明

Delta Lake 把表表示为存储在对象存储中的一组 Parquet 文件，加上一个事务日志（_delta_log）记录所有变更。它支持：

- ACID 事务。
- Schema enforcement 和 evolution。
- 时间旅行（time travel）。
- 高效的 upsert、delete、merge 操作。

Delta Lake 也采用 [[log-structured-storage]] 思想：更新通过追加新文件和日志条目实现。

## 相关

- [[parquet]]
- [[data-lake]]
- [[table-format]]
- [[apache-iceberg]]
- [[spark]]
- [[chapter-04]]
