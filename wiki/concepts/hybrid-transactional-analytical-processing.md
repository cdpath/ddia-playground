---
title: "Hybrid transactional/analytical processing (HTAP)"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, oltp, olap]
---

# Hybrid transactional/analytical processing (HTAP)

**HTAP** 旨在让 [[online-transaction-processing|OLTP]] 和 [[online-analytical-processing|OLAP]] 两种 workload 在同一系统中运行，无需通过 [[extract-transform-load|ETL]] 从一套系统导入另一套系统。

## 现实情况

许多 HTAP 系统内部实际上仍是 OLTP engine 与独立的 analytical engine 的组合，只是对外暴露统一接口。因此，operational 与 analytical 的区分对于理解这些系统仍然有用。

HTAP 不会取代 [[data-warehouse]]，但在同一应用既需要低延迟的单条记录更新、又需要大规模 analytical scan 时很有用 — 例如 fraud detection。
