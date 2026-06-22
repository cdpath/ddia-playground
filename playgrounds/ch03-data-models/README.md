# Chapter 3 — Data Models and Query Languages

本章讨论数据模型与查询语言：关系模型、文档模型、图模型、DataFrame、事件溯源（Event Sourcing）、CQRS 等，以及它们背后的设计权衡。

本目录下的 playground 专注于把本章概念变成可运行代码。

## 运行

```bash
# Jupyter
uv run jupyter notebook playgrounds/ch03-data-models/01-n-plus-one.ipynb

# Zed REPL（打开 .py 文件，按 ctrl-shift-enter 执行 cell）
# 或直接运行
uv run python playgrounds/ch03-data-models/01-n-plus-one.py
```

## Notebooks

| Notebook | 对应概念 | 说明 |
|---|---|---|
| [01-n-plus-one](01-n-plus-one.ipynb) | [[object-relational-mapping\|ORM]]、[[impedance-mismatch]]、[[join]] | 展示 N+1 查询问题：ORM 的 lazy-loading loop 会先查 N 条记录，再为每条记录发起一次关联查询，而手写 SQL 可以通过一次 JOIN 避免。 |
| [01-n-plus-one.py](01-n-plus-one.py) | 同上 | Zed / Jupyter / VS Code 兼容的 `# %%` cell 格式，可在编辑器内按 cell 执行。 |

## 相关 Wiki 页面

- [Chapter 3 源总结](../../wiki/sources/chapter-03.md)
- [Data Model](../../wiki/concepts/data-model.md)
- [Relational Model](../../wiki/concepts/relational-model.md)
- [Document Model](../../wiki/concepts/document-model.md)
- [Graph Data Model](../../wiki/concepts/graph-data-model.md)
- [Query Language](../../wiki/concepts/query-language.md)
- [Normalization](../../wiki/concepts/normalization.md)
- [Denormalization](../../wiki/concepts/denormalization.md)
- [Event Sourcing](../../wiki/concepts/event-sourcing.md)
- [CQRS](../../wiki/concepts/cqrs.md)

> 在 GitHub 上，内部链接 `[[...]]` 不会渲染；请直接查看 `wiki/` 目录下的对应文件，或在 Obsidian 中打开本仓库。
