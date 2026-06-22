---
title: "Impedance Mismatch"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, software-engineering]
---

# Impedance Mismatch

**Impedance mismatch** 指应用代码中的对象模型与数据库中的 relational model 之间存在的不匹配。这个词借自电子学，原意是电路输入输出阻抗不匹配导致信号反射等问题。

## 表现

- 对象有继承、嵌套、集合等结构，而 relational model 是扁平的 tables/rows/columns。
- 需要在两者之间写转换层，如 [[object-relational-mapping|ORM]]。
- 即使使用 ORM，复杂查询或 schema 设计仍需要开发者理解底层关系模型。

## 为什么重要

阻抗不匹配会影响代码复杂度、查询效率和数据模型设计。Document model 被认为能减少这种不匹配，因为 JSON 文档更接近应用中的对象结构。

## 相关

- [[object-relational-mapping]]
- [[relational-model]]
- [[document-model]]
- [[chapter-03]]
