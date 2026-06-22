---
title: "Redis"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, in-memory, key-value, cache]
---

# Redis

**Redis** 是流行的开源 [[in-memory-database|in-memory]] key-value store，常被用作 [[cache]]、消息队列和轻量级数据库。它提供丰富的数据结构（strings、hashes、lists、sets、sorted sets 等）。

## 特点

- 数据主要驻留内存，持久化通过异步写盘或 AOF/RDB 快照实现（弱持久化）。
- 由于所有数据在内存中，实现复杂数据结构（如 priority queue、set）相对简单。
- 常被用作缓存层，也可作为主数据库使用。

## 相关

- [[in-memory-database]]
- [[cache]]
- [[storage-engine]]
- [[memcached]]
- [[chapter-04]]
