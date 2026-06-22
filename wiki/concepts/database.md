---
title: "Database"
type: concept
source_count: 3
last_updated: 2026-06-22
tags: [data-systems, fundamentals]
---

# Database

**Database** 是让应用（或其他应用）能够存储数据并在之后重新找到它的系统。它是 [[data-intensive-application]] 的基础组件之一。

不同 database 针对不同访问模式优化，包括 [[online-transaction-processing|OLTP]]、[[online-analytical-processing|OLAP]] 和嵌入式场景。它们支持不同的 [[data-model]]，如 [[relational-model]]、[[document-model]]、[[graph-data-model]] 等。

数据库的核心由上层查询处理器和底层 [[storage-engine]] 组成。storage engine 决定数据如何落盘、如何索引、如何支持并发读写以及如何在崩溃后恢复。常见实现包括：

- [[b-tree]] 系列：广泛用于关系型 OLTP 数据库。
- [[lsm-tree]] 系列：适合写密集型 key-value 存储。
- [[column-oriented-storage|列式存储]]：面向分析型查询。
- [[in-memory-database]]：数据常驻内存，磁盘仅作持久化。

本书后续章节会讨论 replication、partitioning 和 transaction。

## 相关

- [[data-intensive-application]]
- [[online-transaction-processing|OLTP]]
- [[online-analytical-processing|OLAP]]
- [[data-model]]
- [[relational-model]]
- [[document-model]]
- [[graph-data-model]]
- [[storage-engine]]
- [[chapter-04]]
