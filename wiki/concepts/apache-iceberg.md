---
title: "Apache Iceberg"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-lake, table-format, metadata]
---

# Apache Iceberg

**Apache Iceberg** 是一种开放的 table format，用于在对象存储或分布式文件系统上管理大规模数据集。它把一组 immutable 文件（如 [[parquet]]）组织成逻辑表，并支持更新、删除、时间旅行等高级特性。

## 说明

Iceberg 通过维护表级元数据（manifest 和 manifest list）来解决 Hive 等早期 catalog 的问题，例如：

- 支持高效的分区裁剪，无需依赖目录布局。
- 支持 schema evolution。
- 支持快照隔离和时间旅行查询。
- 提供 REST catalog 接口。

## 相关

- [[parquet]]
- [[data-lake]]
- [[table-format]]
- [[delta-lake]]
- [[apache-hive]]
- [[trino]]
- [[spark]]
- [[chapter-04]]
