---
title: "Abstraction"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, maintainability, software-engineering]
---

# Abstraction

**Abstraction** 是管理软件复杂性的核心工具：它隐藏实现细节，提供简洁、可理解的接口，让使用者不必关心内部机制。

## 为什么重要

随着系统规模增长，代码复杂度会迅速上升，形成所谓的“big ball of mud”。复杂度会拖慢所有开发者，并增加修改时引入 bug 的风险。好的 abstraction 能显著降低这种风险。

## 例子

- 高级编程语言隐藏机器码、寄存器和系统调用。
- SQL 隐藏磁盘与内存数据结构、并发请求、崩溃后的不一致恢复。
- 数据库 transactions、indexes、event logs 都是 data system 层面的通用 abstraction。
- Data models（如 [[relational-model]]、[[document-model]]、[[graph-data-model]]）把底层存储细节抽象成不同的问题视角。

## 好 abstraction 的特征

- 隐藏大量实现细节，但接口清晰简单。
- 可复用于多种场景。
- 改进一处，所有使用者受益。

## 与应用层 abstraction 的关系

应用层可以通过 design patterns、domain-driven design (DDD) 等方法创建自己的 abstraction；本书更关注数据库、存储、消息等通用基础设施提供的 abstraction，应用层可以在此基础上构建。

## 相关

- [[maintainability]] — abstraction 是降低维护成本的关键
- [[database]] — SQL 与 transaction 是典型的 abstraction
