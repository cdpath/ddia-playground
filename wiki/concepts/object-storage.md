---
title: "Object storage"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [cloud, storage]
---

# Object storage

**Object storage** 是一种 cloud service，用简单 API 存储大文件（object），通常只支持基本读写操作。它隐藏底层物理机器，自动分布数据以保证持久性和扩展性。

例子包括 [[amazon-s3]]、Azure Blob Storage、Cloudflare R2。

object storage 是 [[cloud-native]] 系统的基础构建块，常用于 [[data-lake]] 和 [[separation-of-storage-and-compute|storage-compute 分离]] 的系统。
