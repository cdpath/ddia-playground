---
title: "Data minimization"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [privacy, ethics, law]
---

# Data minimization

**Data minimization**（德语称为 *Datensparsamkeit*）指组织只应收集和保留真正需要的个人数据，而不是投机性地存储大量数据。

## 为什么重要

- 降低数据泄露后的法律责任和声誉损失
- 降低 GDPR、CCPA 等隐私法规下的法律风险
- 可减少 storage 成本，但主要动机是风险降低
- 符合 GDPR 要求：个人数据只能为特定、明确的目的收集，不得用于其他目的，保存时间不得超过必要期限

## Engineering 张力

- 许多 data system 依赖 immutable、append-only log，删除中间数据变得复杂
- ML training data 等 derived dataset 也需要在删除个人数据时一并考虑
- "big data" 思维（先存下所有数据再说）与 minimization 相冲突

data minimization 属于更广泛的命题：data system 设计不仅受技术需求驱动，也受法律与社会约束。第 14 章会更深入地讨论伦理与合规。
