---
title: "Chapter 1. Trade-Offs in Data Systems Architecture"
type: source
source_count: 1
last_updated: 2026-06-22
tags: [chapter-summary, data-systems, trade-offs]
---

# Chapter 1. Trade-Offs in Data Systems Architecture

来源：[[designing-data-intensive-applications]] · 原文：[`raw/chapter1/01.md`](../../raw/chapter1/01.md)

## 摘要

本章提出全书的核心主题：data systems 中没有放之四海而皆准的解法，只有 trade-offs。本章定义了后续章节会反复使用的基础术语，并对比了几种影响深远的架构选择。

## 关键收获

- 当 data management 成为应用开发的主要挑战时，我们称这个应用为 **data-intensive application**；相对地，**compute-intensive** 系统的主要挑战是并行化超大计算量。
- data-intensive application 通常由几类标准组件拼装而成：[[database]]、[[cache]]、[[search-index]]、[[stream-processing]]、[[batch-processing]]。
- 存在一条清晰的分界线：[[operational-system]]（OLTP，数据被创建和修改）与 [[analytical-system]]（OLAP，数据被读取和聚合以支持决策）。
- **data warehouse** 通过 [[extract-transform-load|ETL]]（或 ELT）接收 operational 数据的只读副本；**data lake** 则以灵活格式存储原始文件，供 data scientist 和 ML 使用。
- **system of record** 保存数据的权威版本；**derived data system** 可由前者重建（cache、index、materialized view、ML model 等）。
- 本章对比了 **cloud service** 与 **self-hosting**、[[distributed-system]] 与 single-node system，并列出各自适用场景。
- **cloud-native** 架构利用 managed service、[[object-storage]] 以及 **separation of storage and compute**（disaggregation）。
- [[microservices]] 与 [[serverless]]（FaaS）改变了系统的分解方式和计费模式，但也带来集成与运维复杂度。
- data system 的设计不仅受技术目标驱动，也受法律与社会约束：GDPR、CCPA 以及 **data minimization** 原则都会带来真实的 engineering 挑战。

## 本章引入的主要概念

- [[data-intensive-application]]
- [[operational-system]] / [[online-transaction-processing|OLTP]]
- [[analytical-system]] / [[online-analytical-processing|OLAP]]
- [[data-warehouse]]
- [[extract-transform-load|ETL]]
- [[data-lake]]
- [[system-of-record]]
- [[derived-data-system]]
- [[cloud-native]]
- [[separation-of-storage-and-compute]]
- [[microservices]]
- [[serverless]]
- [[distributed-system]]
- [[data-minimization]]

## 提到的系统与工具

- Operational/OLTP：[[mysql]]、[[postgresql]]、[[mongodb]]、AWS Aurora、Azure SQL DB Hyperscale、Google Cloud Spanner
- Analytical/OLAP：Teradata、[[clickhouse]]、[[spark]]、[[snowflake]]、Google BigQuery、Azure Synapse Analytics
- Real-time analytics：Pinot、Druid、[[clickhouse]]
- Data integration：Fivetran、Singer、Airbyte
- Cloud storage：[[amazon-s3]]、Azure Blob Storage、Cloudflare R2、Amazon EBS
- Orchestration：[[kubernetes]]
- Single-node analytical：[[duckdb]]、SQLite、KùzuDB
- Observability：OpenTelemetry、Zipkin、Jaeger
- ML deployment：TFX、Kubeflow、MLflow
- API 标准：OpenAPI、gRPC

## 待后续章节展开的线索

- 第 2 章将深入 [[reliability]]、[[scalability]]、[[maintainability]]。
- 第 4 章会探讨 operational 与 analytical 系统如何使用截然不同的内部存储布局。
- 第 9 章会详细讨论 distributed system 的 failure mode。
- 第 14 章会回到伦理、偏见与法律合规。
