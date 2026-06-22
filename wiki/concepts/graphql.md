---
title: "GraphQL"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, query-languages, apis]
---

# GraphQL

**GraphQL** 是一种面向 OLTP 查询的 API query language，设计目标是从客户端（移动应用、前端）请求结构化的 JSON 响应。

## 设计特点

- 客户端可以精确指定需要的字段，服务器返回不多不少的 JSON。
- 查询结构类似 nested document，可跟随关系展开。
- 无需为每个 UI 变化修改服务端 API。

## 限制

- 为了安全，不允许递归查询和任意搜索条件（除非服务端显式开放）。
- 授权、限流、性能治理需要额外工具。
- 通常需要把 GraphQL 请求映射到内部 REST/gRPC 服务。

## 与 graph database 的区别

尽管名字里有 “graph”，GraphQL 并不依赖 graph database，可基于 relational、document 或 graph storage 实现。

## 相关

- [[query-language]]
- [[document-model]]
- [[chapter-03]]
