---
title: "Data lake"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, analytics, storage]
---

# Data lake

**Data lake** 是一个集中式仓库，保存任何可能对分析有用的数据的副本，数据通过 ETL 从 operational system 流入。与 [[data-warehouse]] 不同，data lake 以文件形式存储数据，不强加特定的文件格式、数据模型或 schema。

## 特征

- 可包含结构化、半结构化和非结构化数据
- 常见文件格式包括 [[avro]]、[[parquet]]、纯文本、图像、视频、传感器数据、ML feature vector 等
- 通常比 relational storage 更便宜，因为它可以使用商品化的 [[object-storage]]
- 常作为 operational system 与 data warehouse 之间的中间站，保存 operational system 产生的原始数据，由不同消费者按需转换

## Sushi principle

"raw data is better" — 保持数据处于 operational system 产生的原始形态，让每个下游消费者决定如何转换。

## 相关概念

- [[data-warehouse]] — 强加 relational schema，针对 SQL analytics 优化
- [[extract-transform-load|ETL]] / data pipeline — 数据如何进入 lake
