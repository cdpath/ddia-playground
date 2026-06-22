---
title: "SQLite"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, sql, embedded, oltp]
---

# SQLite

**SQLite** 是世界上最广泛使用的嵌入式 relational database。它是一个运行在应用进程内的 C 库，无需独立服务器进程。

## 特点

- [[embedded-database]] 的典型代表。
- 支持大部分 SQL 标准，适合移动应用、浏览器、IoT 设备等场景。
- 单机、小并发场景下非常高效。
- Bluesky 等多租户系统使用单租户 SQLite 实例作为后端存储例子。

## 相关

- [[sql]]
- [[relational-model]]
- [[embedded-database]]
- [[chapter-04]]
