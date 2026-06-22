---
title: "Bigtable"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [databases, wide-column, google, lsm-tree]
---

# Bigtable

**Bigtable** 是 Google 开发的分布式 wide-column store，通过 column family 管理 data locality。它影响了 [[hbase]]、[[accumulo]] 等开源系统，并引入了 SSTable 和 memtable 等术语。

## 本章角色

- 使用 [[lsm-tree]] / [[log-structured-storage]] 实现高写入吞吐
- 其不可变 segment 文件（SSTable）思想被 [[rocksdb]]、[[cassandra]]、[[hbase]] 等继承
- 注意：Bigtable 是 [[wide-column-store]]，但仍是 [[row-oriented-storage|行式存储]]，不是列式存储

## 相关

- [[wide-column-store]]
- [[row-oriented-storage]]
- [[lsm-tree]]
- [[sstable]]
- [[hbase]]
- [[accumulo]]
- [[spanner]]
- [[chapter-03]]
- [[chapter-04]]
