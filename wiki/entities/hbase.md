---
title: "HBase"
type: entity
source_count: 2
last_updated: 2026-06-22
tags: [databases, wide-column, apache, lsm-tree]
---

# HBase

**HBase** 是 Apache 开源的分布式 wide-column store，基于 [[bigtable]] 的设计思想。它使用 [[lsm-tree]] 存储模型，通过 HFile（类似 SSTable）存储数据。

## 本章角色

- [[lsm-tree]] 存储引擎的分布式实现代表
- 继承 Bigtable 的 memtable + SSTable 架构
- 属于 [[wide-column-store]] / [[row-oriented-storage|行式存储]]

## 相关

- [[bigtable]]
- [[accumulo]]
- [[lsm-tree]]
- [[sstable]]
- [[chapter-03]]
- [[chapter-04]]
