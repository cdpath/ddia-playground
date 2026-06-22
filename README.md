# ddia-playground

本仓库围绕 *Designing Data-Intensive Applications*（DDIA，第 2 版）构建，包含两部分内容：

1. **Wiki**（`wiki/`）：LLM 维护的持久化知识网络，按 source / concept / entity / synthesis 组织。
2. **Playgrounds**（`playgrounds/`）：可运行的 Jupyter Notebook，把书中概念转成可执行代码，帮助建立直觉。

## 快速导航

- [Wiki 索引](wiki/index.md)
- [Playground 说明与目录](playgrounds/README.md)

## 运行 Playground

本项目使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境和依赖。

### 安装依赖

```bash
uv sync
```

### Jupyter / GitHub

`playgrounds/**/*.ipynb` 可在 Jupyter 或 GitHub 预览中直接查看和运行。

```bash
uv run jupyter notebook playgrounds/
```

### Zed

`playgrounds/**/*.py` 使用 `# %%` cell 分隔符，支持 Zed 的 REPL。把光标放在某个 cell 内，按 `ctrl-shift-enter` 即可执行该块。`uv sync` 已经安装了 `ipykernel`，Zed 应能自动检测到这个 kernel。

大部分 notebook 只依赖 Python 标准库，无需额外安装包即可运行。
