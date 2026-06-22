---
title: "Wide-Column Store"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, nosql]
---

# Wide-Column Store

**Wide-column store**（又称 column family store）是一种 NoSQL data model，由 [[bigtable]] 推广。它通过 **column family** 把相关列组织在一起，以优化 data locality 和读写模式。

## 代表系统

- [[bigtable]]（Google）
- [[hbase]]（Apache）
- [[accumulo]]（Apache）

## 与 relational model 的关系

Wide-column store 保留了行和列的概念，但列可以动态增加，同一张表的不同行可以有不同的列。它介于 relational 和 pure key-value store 之间。

## 相关

- [[data-locality]]
- [[bigtable]]
- [[chapter-03]]
