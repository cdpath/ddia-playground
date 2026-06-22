---
title: "XML"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, formats, data-models]
---

# XML

**XML（Extensible Markup Language）** 是一种可扩展标记语言，曾被广泛用于表示层次化数据，也是 document model 的一种形式。

## 特点

- 自描述、可验证（通过 XML Schema 或 DTD）。
- 支持嵌套结构，适合 tree-shaped 数据。
- 相比 JSON，XML 更冗长，但类型和验证能力更强。

## 查询方式

- **XPath**：在 XML 文档中定位节点。
- **XQuery**：更强大的 XML 查询和转换语言，支持跨文档 join。

## 现代地位

XML database 只获得 niche adoption。不过 XML 仍在某些领域（如配置、办公文档、SOAP 消息）使用，relational database 也常提供 XML 类型支持。

## 相关

- [[document-model]]
- [[json]]
- [[chapter-03]]
