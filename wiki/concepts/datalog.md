---
title: "Datalog"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, query-languages, graph]
---

# Datalog

**Datalog** 是比 SPARQL 和 Cypher 更古老的 declarative query language，源于 1980 年代的学术研究。它基于 relational data model，但尤其适合递归 graph 查询。

## 基本概念

- **Facts**：数据库中的事实，对应 relational table 的一行，如 `location(2, "United States", "country")`。
- **Rules**：由 `:-` 分隔，左侧是推导出的虚拟表，右侧是匹配条件。
- 规则可以互相引用，也可以递归调用自己。

## 例子：递归查找地点层级

```prolog
within_recursive(LocID, PlaceName) :- location(LocID, PlaceName, _).
within_recursive(LocID, PlaceName) :- within(LocID, ViaID),
                                      within_recursive(ViaID, PlaceName).
```

## 特点

- 通过逐步推导规则构建复杂查询，类似把代码拆成互相调用的函数。
- 递归规则天然支持 graph traversal。
- 在主流数据库中支持不广，但 [[datomic]]、LogicBlox、CozoDB、LinkedIn 的 LIquid 等在使用。

## 相关

- [[declarative-query-language]]
- [[graph-data-model]]
- [[relational-model]]
- [[chapter-03]]
