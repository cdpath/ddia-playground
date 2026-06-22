---
title: "X (Twitter)"
type: entity
source_count: 1
last_updated: 2026-06-22
tags: [social-network, case-study, data-intensive]
---

# X (Twitter)

X（前身为 Twitter）是社交媒体平台，本章用它作为大规模 data-intensive system 的案例。

## 本章数据

- 5 亿 posts/天，平均约 5,800 posts/秒。
- 峰值可达 150,000 posts/秒。
- 平均用户关注 200 人、被 200 人关注；少数 celebrity 拥有上亿 follower。

## 与本章概念的关系

X/Twitter 的 home timeline 展示了如何用 [[materialized-view]] 与 [[fan-out]] 在高 read 负载下保持 performance，以及如何处理普通用户与 celebrity 的极端差异。

## 相关

- [[materialized-view]]
- [[fan-out]]
- [[cache]]
- [[scalability]]
