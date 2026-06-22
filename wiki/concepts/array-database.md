---
title: "Array Database"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, analytics, scientific-computing]
---

# Array Database

**Array database** 专门存储大型多维数字数组（如矩阵、张量），常用于科学计算、医学影像、地理空间栅格数据、天文观测等场景。

## 例子

- [[tiledb]]：面向多维数组的存储引擎。
- NumPy / SciPy 生态（虽然更偏向内存计算）。

## 应用场景

- 地理空间栅格数据。
- 医学影像。
- 天文望远镜观测数据。

## 与 DataFrame 的关系

DataFrame 也常用于把关系数据转换为矩阵或稀疏数组，供 ML 使用。Array database 则更进一步，把多维数组作为一等存储对象。

## 相关

- [[dataframe]]
- [[numpy]]
- [[tiledb]]
- [[chapter-03]]
