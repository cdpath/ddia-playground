---
title: "Microservices"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [architecture, distributed-systems]
---

# Microservices

**Microservices architecture** 将应用分解为小型、可独立部署的服务，每个服务有明确的单一职责，并由小团队负责。

## 特征

- 服务通过网络通信，通常使用 HTTP/REST 或 RPC
- 每个服务暴露 API，隐藏实现细节
- 每个服务通常拥有自己的 database；避免共享 database，因为这会把服务耦合在一起

## 优势

- 服务可独立更新，减少团队协调成本
- 每个服务可按其 workload 分配硬件资源
- 只要 API 稳定，实现变更不会影响 client

## 劣势

- 本地开发与测试需要运行依赖的服务
- 每个服务都需要部署、监控、日志、告警等基础设施
- API 演进困难，容易破坏 client
- [[distributed-system]] 的复杂度：网络故障、一致性、observability

microservices 本质上是解决"人"的问题的技术方案：让多个团队独立推进。对于团队较少的小公司，它可能是不必要的开销。

## 相关

- [[serverless]] — 另一种分解模型
- [[service-oriented-architecture|SOA]] — 前身概念
- OpenAPI、gRPC 等 API 标准
