---
title: "Write Amplification"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, performance, ssd]
---

# Write Amplification

**Write amplification** 指数据库因维护索引、日志、compaction 等原因，实际写入磁盘的字节数与应用程序请求写入的字节数之比。它是衡量存储引擎写效率的重要指标。

## 说明

任何索引都会增加写放大。例如：

- [[b-tree]]：每条数据至少写两次（一次 [[write-ahead-log|WAL]]，一次 tree page），且 page 覆写时即使只改几个字节也可能写整个 page。
- [[lsm-tree]]：数据先写 WAL，再写 memtable flush，每次 compaction 还可能被重写多次。

写放大越高，在写密集型负载中越容易耗尽磁盘带宽，也会加速 SSD 磨损。

## 经验

- 典型负载下，LSM-tree 的写放大通常低于 B-tree，因为它不需要覆写整个 page，且可以压缩数据块。
- 测量写吞吐时应让实验运行足够长时间，使 compaction 的影响显现出来。

## 相关

- [[read-amplification]]
- [[storage-engine]]
- [[b-tree]]
- [[lsm-tree]]
- [[compaction]]
- [[sequential-write]]
- [[random-write]]
- [[chapter-04]]
