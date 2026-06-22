---
title: "Serverless"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [cloud, architecture, faas]
---

# Serverless

**Serverless**，也称 **function as a service（FaaS）**，是一种部署模型：cloud provider 管理底层基础设施，根据请求自动分配和释放资源。

## 特征

- 无需显式 provisioning 或管理 server
- 按执行时间 metered billing，而非预留机器实例
- function 通常是无状态的、短生命周期的
- 首次调用时可能出现 cold start，带来 latency

## Trade-offs

- 新服务上手更简单，运维负担更小
- 执行时间受限，runtime 环境受限
- 调试与性能调优更困难，因为基础设施不透明
- 名称有误导性：代码仍然运行在 server 上，只是不是你管理的 server

serverless 是 self-hosted 软件与 fully managed cloud service 之间光谱上的一个点。它与 [[microservices]] 和 [[cloud-native]] 相关，但并不等同。
