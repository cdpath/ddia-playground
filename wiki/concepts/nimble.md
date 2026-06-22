---
title: "Nimble"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [serialization, data-formats, columnar]
---

# Nimble

**Nimble** 是 Meta（Facebook）开发的列式文件格式，基于 Velox 项目。它针对高吞吐分析和向量化执行优化。

## 说明

Nimble 与 [[parquet]]、ORC 类似，属于现代 [[column-oriented-storage|列式存储]] 格式。它主要在 Meta 内部和 Velox 生态中使用。

## 相关

- [[parquet]]
- [[orc]]
- [[column-oriented-storage]]
- [[vectorized-processing]]
- [[chapter-04]]
