---
title: "RAMCloud"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [database, in-memory, key-value, research]
---

# RAMCloud

**RAMCloud** 是一个开源的 [[in-memory-database|in-memory]] key-value store，由斯坦福大学开发。它把所有数据存放在 DRAM 中，同时通过日志结构方式持久化到磁盘以保证 durability。

## 特点

- 极低延迟的 key-value 访问。
- 使用 log-structured 方式管理内存和磁盘数据。
- 属于研究型系统，强调内存存储的持久化方案。

## 相关

- [[in-memory-database]]
- [[log-structured-storage]]
- [[storage-engine]]
- [[chapter-04]]
