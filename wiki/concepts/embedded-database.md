---
title: "Embedded Database"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [database, storage, library]
---

# Embedded Database

**Embedded database** 是不暴露网络 API、而是以库（library）形式运行在应用进程内的数据库。应用通过函数调用直接读写本地文件。

## 说明

Embedded database 适合以下场景：

- 移动应用本地存储用户数据。
- 后端单机数据量较小、并发事务不多。
- 多租户系统中每个租户数据独立且规模可控，可为每个租户分配一个独立实例。

## 典型系统

- [[sqlite]]：轻量级关系型 embedded database，应用极广。
- [[rocksdb]]、[[leveldb]]：基于 [[lsm-tree]] 的 key-value storage engine。
- [[lmdb]]：基于 copy-on-write B-tree 的 key-value store。
- [[duckdb]]：面向 analytics 的 embedded columnar database。
- KùzuDB：嵌入式图数据库。

## 与客户端/服务器数据库的对比

- **Embedded**：无网络 hop、无独立进程，延迟低，运维简单；但扩展性和并发控制受单机限制。
- **Client/server**：独立进程，支持网络访问，可扩展，但引入额外延迟和运维复杂度。

## 相关

- [[storage-engine]]
- [[in-memory-database]]
- [[sqlite]]
- [[duckdb]]
- [[rocksdb]]
- [[lmdb]]
- [[chapter-04]]
