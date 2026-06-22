---
title: "Read Amplification"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [storage, performance]
---

# Read Amplification

**Read amplification** 指一次逻辑读取操作实际需要读取的磁盘数据量。它衡量读操作的 I/O 效率。

## 说明

不同存储引擎的读放大差异显著：

- [[b-tree]]：查找 key 通常只需读取树的几层 page（通常 3~4 次 I/O），读放大低且稳定。
- [[lsm-tree]]：读取可能需要检查 memtable 和多个 SSTable segment，尤其是 key 不存在或很久未更新时。配合 [[bloom-filter]] 可减少无效读取。
- [[column-oriented-storage]]：分析查询只需读取所需列，但可能扫描大量行；行式存储则需加载整行。

读放大直接影响读取延迟和吞吐，是选择存储引擎时的重要考量。

## 相关

- [[write-amplification]]
- [[storage-engine]]
- [[b-tree]]
- [[lsm-tree]]
- [[bloom-filter]]
- [[column-oriented-storage]]
- [[chapter-04]]
