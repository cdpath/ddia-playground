# DDIA Playgrounds

本目录存放 *Designing Data-Intensive Applications* 的**可运行示例**（playground）。

每个 playground 都是一个 Jupyter Notebook，用来把书中的抽象概念转成可执行的代码，帮助你建立直觉、观察参数影响，并亲手验证不同方案之间的权衡。

> **注意**：这些 notebook 不是生产 benchmark，也不是真实系统的复现。它们展示的是**问题产生的机制**和**权衡结构**。关于真实大规模系统下的延迟、并发、故障等细节，仍需要参考书中案例、论文和生产环境数据。

## 运行方式

本项目使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境。

### 安装依赖

```bash
uv sync
```

### 本地运行 Jupyter

```bash
uv run jupyter notebook playgrounds/
```

### 在 Zed 中运行

直接用 Zed 打开 `playgrounds/**/*.py` 文件，把光标放在某个 `# %%` cell 内，按 `ctrl-shift-enter` 执行。Zed REPL 需要本地 Python kernel，`uv sync` 已经安装好 `ipykernel`。

### 直接运行脚本

```bash
uv run python playgrounds/ch03-data-models/01-n-plus-one.py
```

所有 notebook 优先使用 Python 标准库，因此不需要安装额外依赖即可运行大部分示例。

### Google Colab / Binder

每个 notebook 顶部会提供运行链接（未来补充）。

## 目录

### Chapter 3 — Data Models and Query Languages

- [01-n-plus-one](ch03-data-models/01-n-plus-one.ipynb) — N+1 query problem：ORM 的陷阱、JOIN 与 batch loading 的对比
- [01-n-plus-one.py](ch03-data-models/01-n-plus-one.py) — 同上，Zed / Jupyter / VS Code 兼容的 `# %%` cell 格式

### Chapter 4 — Storage and Retrieval

- [01-lsm-vs-btree](ch04-storage-and-retrieval/01-lsm-vs-btree.ipynb) — LSM-tree vs B-tree：存储引擎的读写权衡、写放大与读放大
- [01-lsm-vs-btree.py](ch04-storage-and-retrieval/01-lsm-vs-btree.py) — 同上，Zed / Jupyter / VS Code 兼容的 `# %%` cell 格式

## 相关 Wiki 页面

- [Wiki 首页](../wiki/index.md)
- [Chapter 3 源总结](../wiki/sources/chapter-03.md)
- [Chapter 4 源总结](../wiki/sources/chapter-04.md)
- [Object-Relational Mapping](../wiki/concepts/object-relational-mapping.md)
- [Impedance Mismatch](../wiki/concepts/impedance-mismatch.md)
- [Join](../wiki/concepts/join.md)
- [Storage Engine](../wiki/concepts/storage-engine.md)
- [LSM-Tree](../wiki/concepts/lsm-tree.md)
- [B-Tree](../wiki/concepts/b-tree.md)

在 Obsidian 中打开本仓库时，也可以直接使用 `[[wiki-index]]`、`[[chapter-03]]`、`[[chapter-04]]`、`[[object-relational-mapping]]` 等内部链接导航。
