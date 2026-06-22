---
title: "Primary Index"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, index]
---

# Primary Index

**Primary index** 是基于主键（primary key）建立的索引，用于唯一标识表中的一行、文档数据库中的一个文档或图数据库中的一个顶点。其他记录可以通过主键引用这条记录。

## 说明

主键索引与数据的物理组织方式密切相关。根据实现不同，主键索引可以是：

- **[[clustered-index]]**：数据行直接存储在索引结构中，如 [[mysql]] InnoDB 的主键。
- **非聚集主键索引**：索引只存储主键值，实际数据存放在 [[heap-file]] 中，如 [[postgresql]] 的默认组织方式。

主键索引通常提供最快的点查路径，因为绝大多数查询都通过主键定位记录。

## 相关

- [[index]]
- [[secondary-index]]
- [[clustered-index]]
- [[heap-file]]
- [[storage-engine]]
- [[chapter-04]]
