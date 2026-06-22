---
title: "Object-Relational Mapping"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, software-engineering]
---

# Object-Relational Mapping

**Object-relational mapping（ORM）** 是在面向对象应用代码与 relational database 之间做自动转换的框架，用于减少样板代码。

## 常见工具

- [[activerecord]]（Ruby on Rails）
- [[hibernate]]（Java）
- Django ORM、SQLAlchemy（Python）等

## 解决的问题

- 把对象自动映射为 relational tables、rows、columns。
- 封装 schema migration、缓存、CRUD 样板。

## 常见问题

- 无法完全隐藏 relational 与 object 两种模型的差异，开发者仍需要同时思考两者。
- 主要用于 OLTP 应用开发，数据分析人员仍需直接操作底层表。
- 对非关系型系统（搜索引擎、图数据库、NoSQL）支持有限。
- 自动生成 schema 可能不适合直接访问数据的人。
- 容易产生 **N+1 query problem**：先查 N 条记录，再为每条记录发起一次关联查询。

## Playground

- [N+1 Query Problem（Jupyter Notebook）](../../../playgrounds/ch03-data-models/01-n-plus-one.ipynb) — 用 Python + SQLite 演示 ORM lazy-loading 导致的 N+1 查询，以及 JOIN / batch loading 的对比。
- [N+1 Query Problem（Zed / # %% cell 格式）](../../../playgrounds/ch03-data-models/01-n-plus-one.py) — 同上，可在 Zed 等编辑器内按 cell 执行。

## 相关

- [[impedance-mismatch]]
- [[relational-model]]
- [[chapter-03]]
