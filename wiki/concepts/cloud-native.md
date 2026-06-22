---
title: "Cloud native"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [cloud, architecture, data-systems]
---

# Cloud native

**Cloud native** 描述一种为利用 cloud service 而设计的架构，而不是简单地把 self-hosted 软件搬到 virtual machine 上。

## 核心思想

- 在低级 managed service 之上构建更高级的服务
- 使用 [[object-storage]]（如 [[amazon-s3]]）存放持久文件，而非本地磁盘
- 将 storage 与 compute 分离，使两者可独立扩展
- 将 compute instance 视为 ephemeral，而非长期运行的 server
- 采用 metered billing 和 autoscaling

## 优势

- 相同硬件下性能更好
- 故障恢复更快
- 可随负载弹性伸缩
- 支持更大数据集

## 例子

Cloud-native database 包括 Snowflake、Google BigQuery、AWS Aurora、Google Cloud Spanner。它们常与 [[mysql]]、[[postgresql]]、[[mongodb]] 等 self-hosted 系统对比。
