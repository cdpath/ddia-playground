---
title: "Online transaction processing (OLTP)"
type: concept
source_count: 2
last_updated: 2026-06-22
tags: [data-systems, oltp, transactions]
---

# Online transaction processing (OLTP)

**OLTP** 是 operational system 典型的访问模式：大量低延迟的小读写，通常通过 key 查找少量记录（**point query**）。

特征：

- 根据用户输入插入、更新或删除记录
- 应用是交互式的，因此 latency 很重要
- 查询通常固定并内嵌在 application code 中
- 出于安全和性能考虑，终端用户一般不能对 OLTP database 运行任意 SQL

transaction 一词最初指商业交易，现在泛指构成逻辑单元的一组读写。更深入的讨论见 [[operational-system]]。

在 data modeling 上，OLTP 系统通常更适合 [[normalization|normalized]] 数据和 [[schema-flexibility|schema-on-write]]，以保持一致性和快速更新。
