---
title: "Query Compilation"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [query-execution, performance, analytics]
---

# Query Compilation

**Query compilation** 是数据库把 SQL 查询编译成可执行机器码（通常是 LLVM IR）的技术。相比逐行解释执行，编译执行能显著降低 CPU 开销，提升分析查询性能。

## 说明

复杂分析查询被分解为多个 operator（如 filter、project、aggregate、join）。在传统解释执行中，每个 operator 每行都要查询一个表示查询计划的数据结构，函数调用和分支预测开销大。

Query compilation 的思路是：针对具体查询生成专门的代码，把多个 operator 融合成紧凑的内层循环，减少函数调用和分支，提高指令流水线和 SIMD 利用率。

## 优点

- 减少解释开销。
- 利于 CPU 指令流水线和分支预测。
- 可以针对具体查询做特化优化。

## 与 vectorized processing 的对比

- **Query compilation**：把查询编译成机器码，按行迭代处理。
- **[[vectorized-processing]]**：保持解释执行框架，但一次处理一批列数据。

两者在实践中都广泛使用，也常结合使用。

## 相关

- [[vectorized-processing]]
- [[column-oriented-storage]]
- [[data-warehouse]]
- [[online-analytical-processing|OLAP]]
- [[query-language]]
- [[chapter-04]]
