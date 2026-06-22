---
title: "System of record"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, fundamentals]
---

# System of record

**System of record**（也称 **source of truth**）保存数据的权威、canonical 版本。当新数据进入系统时（例如来自用户输入），首先写在这里。

属性：

- 每个事实只表示一次
- 表示通常是 normalized 的
- 如果其他系统与 system of record 冲突，以后者为准

区分 system of record 与 [[derived-data-system]] 不取决于工具，而取决于它在应用中的使用方式：同一个 database 既可能是前者，也可能是后者。
