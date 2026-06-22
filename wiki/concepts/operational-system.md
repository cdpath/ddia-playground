---
title: "Operational system"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [data-systems, oltp, fundamentals]
---

# Operational system

**Operational system** 指由 backend service 和数据基础设施组成的系统，数据在其中被创建和修改，通常是对用户行为的响应。

主要特征：

- application code 既读取也写入数据
- 典型用户是 web 或 mobile app 的终端用户
- 查询通常由应用预先定义好
- 负载由大量小查询组成
- 数据代表某一时刻的最新状态

operational system 与 [[online-transaction-processing|OLTP]] 联系紧密，但 operational 更强调系统在企业中的角色，而非具体的访问模式。与之相对的是 [[analytical-system]]，后者为分析师和 data scientist 提供只读的 derived 数据副本。
