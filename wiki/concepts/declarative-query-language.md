---
title: "Declarative Query Language"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, query-languages]
---

# Declarative Query Language

**Declarative query language** 让用户声明所需结果的模式（过滤条件、排序、分组、聚合），而不指定数据库如何执行这些操作。

## 优点

- **简洁**：通常比手写算法更短。
- **隐藏实现细节**：query optimizer 可自动选择 index、join 算法和执行顺序。
- **便于优化升级**：存储引擎改进后，同一查询可能自动变快，无需改写。
- **易于并行化**：优化器可把查询拆分到多核或多机执行，而用户无需关心。

## 例子

- [[sql]]
- [[cypher]]
- [[sparql]]
- [[datalog]]

与之相对的是 imperative（命令式）语言，如 Python、Java，需要显式说明操作顺序。

## 相关

- [[query-language]]
- [[data-model]]
- [[chapter-03]]
