---
title: "Relational Model"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-models]
---

# Relational Model

**Relational model** 由 Edgar Codd 于 1970 年提出，是现代关系型数据库（RDBMS）的理论基础。数据被组织为 **relations**（在 SQL 中称为 tables），每个 relation 是 **tuples**（rows）的无序集合。

## 核心特征

- 数据以 tables、rows、columns 形式组织。
- 通过 primary key 唯一标识每行，通过 foreign key 表达表间关系。
- 用 [[sql]] 查询，支持 [[join]]、filter、aggregate、group 等操作。
- schema 通常是预先定义并强制的（schema-on-write）。

## 优势

- 对 [[relationship-cardinality|many-to-one]] 和 [[relationship-cardinality|many-to-many]] 关系支持良好。
- 声明式查询能力强，query optimizer 可自动优化。
- 在 [[data-warehouse]] 和 analytics 中占主导地位，常用 star/snowflake schema。

## 劣势

- 与面向对象应用代码之间可能存在 [[impedance-mismatch]]，需要 [[object-relational-mapping|ORM]] 转换。
- 对 tree-shaped、one-to-many 数据可能需要把单个逻辑对象拆到多个表（shredding）。

## 相关

- [[sql]]
- [[database]]
- [[normalization]]
- [[denormalization]]
- [[document-model]]
- [[edgar-codd]]
- [[chapter-03]]
