# Chapter 4 Playgrounds: Storage and Retrieval

本目录存放 *Designing Data-Intensive Applications* 第 4 章《Storage and Retrieval》相关的交互式 playground。

## Notebooks

| # | 文件 | 主题 | 对应概念 |
|---|------|------|----------|
| 01 | [01-lsm-vs-btree.ipynb](01-lsm-vs-btree.ipynb) / [01-lsm-vs-btree.py](01-lsm-vs-btree.py) | LSM-tree vs B-tree 的读写权衡 | [lsm-tree](../../wiki/concepts/lsm-tree.md)、[b-tree](../../wiki/concepts/b-tree.md)、[write-amplification](../../wiki/concepts/write-amplification.md)、[read-amplification](../../wiki/concepts/read-amplification.md)、[bloom-filter](../../wiki/concepts/bloom-filter.md) |

## 如何运行

- **Jupyter**：`uv run jupyter notebook 01-lsm-vs-btree.ipynb`
- **Zed REPL**：打开 `01-lsm-vs-btree.py`，使用 `# %%` 作为 cell 分隔符。
- **纯 Python**：`uv run python3 01-lsm-vs-btree.py`

所有代码只依赖 Python 标准库。
