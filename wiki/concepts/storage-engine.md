---
title: "Storage Engine"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, oltp, olap]
---

# Storage Engine

**Storage engine** 是数据库中负责实际存储和检索数据的底层模块。它决定数据如何落盘、如何索引、如何支持并发读写，以及如何在崩溃后恢复。

## 说明

数据库通常由上层查询处理器和底层 storage engine 组成。storage engine 关心的是：

- 数据以什么格式写入磁盘（log、page、column file 等）。
- 使用哪种 index 加速读取（[[b-tree]]、[[lsm-tree]]、bitmap 等）。
- 写入是原地更新（in-place）还是追加写入（append-only）。
- 如何组织行数据（row-oriented 或 column-oriented）。
- 崩溃恢复机制（[[write-ahead-log|WAL]]、snapshot、复制等）。

不同的 workload 需要不同的 storage engine：

- **OLTP workload**：高并发、每次读写少量记录，常用 [[b-tree]] 或 [[lsm-tree]] 等有序索引。
- **OLAP workload**：扫描大量行、只读几列，常用 [[column-oriented-storage|列式存储]] 配合压缩与向量化执行。

## 主要流派

- **Update-in-place**：以固定大小的 page 为单位原地覆写，代表是 B-tree 系列（[[postgresql]]、[[mysql]] InnoDB）。
- **Log-structured**：只追加不修改旧文件，通过后台 compaction 回收空间，代表是 [[lsm-tree]]（[[rocksdb]]、[[cassandra]]、[[hbase]]）。
- **In-memory**：数据常驻内存，磁盘仅作持久化 log，代表是 [[redis]]、VoltDB、SingleStore。

## 关键权衡

- 读放大（read amplification）vs 写放大（write amplification）
- 顺序写 vs 随机写
- 读取延迟 vs 写入吞吐
- 空间占用 vs 查询速度

## 相关

- [[database]]
- [[index]]
- [[b-tree]]
- [[lsm-tree]]
- [[column-oriented-storage]]
- [[in-memory-database]]
- [[embedded-database]]
- [[online-transaction-processing|OLTP]]
- [[online-analytical-processing|OLAP]]
- [[chapter-04]]
