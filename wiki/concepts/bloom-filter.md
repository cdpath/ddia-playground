---
title: "Bloom Filter"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-structures, probabilistic, storage]
---

# Bloom Filter

**Bloom filter** 是一种空间高效的概率型数据结构，用于判断某个元素是否“可能存在于”集合中。它可能产生**误报**（false positive），但不会产生**漏报**（false negative）。

## 说明

Bloom filter 维护一个位数组。插入元素时，用若干 hash 函数把元素映射到位数组的若干位置，将这些位置置为 1。查询时，同样计算 hash 位置：

- 如果任一位置为 0，则元素**一定不在**集合中。
- 如果所有位置都为 1，则元素**可能在**集合中（也可能是 false positive）。

False positive 的概率取决于位数组大小、hash 函数数量和集合元素数量。经验法则：每个 key 分配约 10 bit 可将 false positive 控制在 1% 左右。

## 在存储引擎中的应用

在 [[lsm-tree]] 中，每个 [[sstable]] segment 可附带一个 Bloom filter。读取 key 时，先检查 Bloom filter：

- 如果 Bloom filter 说 key 不存在，就跳过该 segment，避免一次磁盘 I/O。
- 如果 Bloom filter 说 key 可能存在，再读取 segment 确认。

Bloom filter 对点查（point lookup）非常有效，但对范围查询（range query）帮助有限，因为无法对范围内所有 key 做 hash 检查。

## 相关

- [[lsm-tree]]
- [[sstable]]
- [[storage-engine]]
- [[chapter-04]]
