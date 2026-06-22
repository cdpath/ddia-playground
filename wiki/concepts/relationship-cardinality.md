---
title: "Relationship Cardinality"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, databases, data-modeling]
---

# Relationship Cardinality

**Relationship cardinality** 描述两个实体之间关联的数量关系，是选择 data model 的重要依据。

## 主要类型

- **One-to-many（one-to-few）**：一个实体关联少量其他实体。例如一个用户有多个职位、多段教育经历。适合用 [[document-model]] 的嵌套数组或 [[relational-model]] 的 separate table 表示。
- **Many-to-one**：多个实体指向同一个实体。例如多个用户居住在同一个地区。在 relational model 中用 foreign key；在 document model 中通常也需要引用 ID。
- **Many-to-many**：实体之间多对多关联。例如一个人可为多个组织工作，一个组织有多个员工。Relational model 用 associative/join table；graph model 用 edges；document model 需要在两边存储 ID 引用（可能不一致）。

## 对模型选择的影响

- 主要是 one-to-many → document model 通常更自然。
- 大量 many-to-one / many-to-many → relational 或 graph model 更合适。

## 相关

- [[relational-model]]
- [[document-model]]
- [[graph-data-model]]
- [[chapter-03]]
