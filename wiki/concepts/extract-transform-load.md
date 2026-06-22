---
title: "Extract–transform–load (ETL)"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-pipelines, integration, analytics]
---

# Extract–transform–load (ETL)

**ETL** 是将数据从 operational system 迁移到 analytical system（如 [[data-warehouse]] 或 [[data-lake]]）的过程。

## 三个步骤

1. **Extract** — 从 operational database 或外部 API 读取数据
2. **Transform** — 清洗、规范化、重塑成 analysis-friendly 的 schema
3. **Load** — 将转换后的数据写入目标系统

## 常见变体

- **ELT** — 先加载，再在目标系统内部转换，常用于 target warehouse 算力充足时
- **Reverse ETL** — 将 analytical system 的输出（如 ML model 分数、feature 值）推回 operational system
- **Data pipeline** — 任何周期性的数据移动与处理流程的泛称

ETL 是连接 [[operational-system]] 与 [[analytical-system]] 的关键集成点。
