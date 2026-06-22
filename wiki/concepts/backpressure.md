---
title: "Backpressure"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, performance, flow-control]
---

# Backpressure

**Backpressure**（背压）是系统在面对临时性处理能力不足时，主动减缓或暂停上游请求的机制。目的是防止队列无限增长导致崩溃或雪崩。

## 说明

在 [[lsm-tree]] 存储引擎中，如果写入速度持续超过 compaction 速度，memtable 会迅速填满。此时许多实现（如 [[rocksdb]]）会暂停所有读写，直到 memtable 被 flush 到磁盘，从而避免内存耗尽和延迟进一步恶化。

Backpressure 会表现为写入延迟的突然尖峰，是 log-structured storage 在高写负载下需要注意的现象。

## 相关

- [[lsm-tree]]
- [[compaction]]
- [[memtable]]
- [[storage-engine]]
- [[chapter-04]]
