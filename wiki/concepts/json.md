---
title: "JSON"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, formats, data-models]
---

# JSON

**JSON（JavaScript Object Notation）** 是一种轻量级文本数据格式，也是 document model 最常用的表示形式之一。

## 特点

- 自描述、易读、人与机器都容易处理。
- 支持嵌套对象和数组，天然适合 tree-shaped 数据。
- 无 schema，常被 document database 用作存储格式。

## 局限性

- 不区分整数和浮点数等数据类型（相比 BSON 等二进制格式）。
- 作为编码格式也有一些问题，将在 [[chapter-05]] 讨论。
- 没有内建日期类型，通常用字符串表示。

## 查询方式

- [[jsonpath]]、JSON Pointer 用于在 JSON 文档中定位数据。
- 现代 relational database（如 PostgreSQL、MySQL）也支持 JSON 类型和 JSON 查询函数。

## 相关

- [[document-model]]
- [[xml]]
- [[mongodb]]
- [[chapter-03]]
