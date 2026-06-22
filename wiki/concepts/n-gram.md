---
title: "N-Gram"
type: concept
source_count: 1
last_updated: 2026-06-22
tags: [search, text-processing, information-retrieval]
---

# N-Gram

**N-gram** 是指长度为 n 的连续子串。例如字符串 `hello` 的 trigram（n=3）为 `hel`、`ell`、`llo`。

## 说明

在数据库和搜索引擎中，n-gram 可用于构建 [[inverted-index]]：对文本中所有 n-gram 建立倒排索引，就能搜索任意长度不少于 n 的子串。

N-gram 索引的优点：

- 支持子串搜索。
- 可以支持正则表达式查询（把正则拆成 n-gram 约束）。

缺点：

- 索引体积大。
- 比基于词的倒排索引产生更多 false positive，需要后过滤。

PostgreSQL 的 pg_trgm 扩展就是基于 trigram 实现模糊搜索和正则索引。

## 相关

- [[full-text-search]]
- [[inverted-index]]
- [[search-index]]
- [[chapter-04]]
