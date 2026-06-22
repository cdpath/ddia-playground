# Agent Notes

## Generating Markdown from the EPUB

The source EPUB (`Designing.Data-Intensive.Applications.2nd.2026.2.epub`) is converted to per-chapter Markdown with images extracted alongside.

Run the conversion script from the repo root:

```bash
python3 scripts/convert_epub.py
```

### Prerequisites

Install Python dependencies (already installed in this environment):

```bash
python3 -m pip install ebooklib markdownify beautifulsoup4 lxml
```

### Output Layout

The script writes to `./raw/`:

```
raw/
├── frontmatter/
│   ├── frontmatter.md   # Cover, praise, title page, dedication, preface
│   └── cover.png
├── chapter1/
│   ├── 01.md
│   └── ddia_0101.png
├── chapter2/
│   ├── 02.md
│   └── ...
...
├── chapter14/
│   ├── 14.md
│   └── ...
└── backmatter/
    └── backmatter.md    # Glossary, index, about the authors, colophon
```

- Real book chapters are detected by `Chapter N.` headings and placed in `chapterN/{NN}.md`.
- Frontmatter and backmatter are merged into their own directories.
- Images referenced by a chapter live in the same directory as that chapter's `.md` file.

### Special Handling

- Small inline marker images like `1.png`, `1_1.png`, `3_1.png` (circled numbers) are replaced with Unicode characters (`①`, `②`, `③`, …) in the Markdown and are not emitted as separate image files.

## Maintaining the LLM Wiki

The `raw/` directory is treated as **read-only source material**. On top of it we maintain an LLM-generated wiki under `wiki/` — a persistent, interlinked knowledge layer rather than a one-off summary.

### Wiki structure

```
wiki/
├── index.md          # Catalog of all pages
├── log.md            # Append-only history of ingests and queries
├── sources/          # One summary page per book chapter
├── concepts/         # Concept pages (OLTP, data warehouse, consensus, ...)
├── entities/         # Concrete systems, tools, people (Kafka, S3, ...)
└── synthesis/        # Comparisons, overviews, analyses
```

### What goes where

- `sources/` — **summaries** of the raw chapters, not the original text. Each page captures the chapter’s key takeaways, important concepts/entities introduced, and open threads for later chapters.
- `concepts/` — explanations of ideas. Created or updated whenever a source introduces or significantly advances a concept.
- `entities/` — pages for specific systems, tools, organizations, or people mentioned in the book.
- `synthesis/` — higher-level pages such as comparisons, evolving thesis, or answers to complex questions that are worth filing back into the wiki.

### Ingest workflow

When processing a new chapter:

1. Before reading the new raw chapter, search existing `wiki/sources/` and `wiki/concepts/` pages for forward references to this chapter (e.g., “本书第 N 章会详细讨论…”, “将在第 N 章展开”, “详见第 N 章”). Keep a list of pages likely to need backfill.
2. Read the raw chapter from `raw/chapterN/NN.md`.
3. Create or update `wiki/sources/chapter-NN.md` with a concise summary, key takeaways, and links to relevant concept/entity pages.
4. For each important concept introduced or advanced, create or update `wiki/concepts/<concept>.md`.
5. For each concrete system/tool/person mentioned, create or update `wiki/entities/<entity>.md`.
6. Revisit the forward-reference list from step 1. Backfill any pages whose promises are now fulfilled, and update or remove placeholder sentences in those pages.
7. Update `wiki/index.md` to list all new/updated pages.
8. Append an entry to `wiki/log.md`.

### Conventions

- Pages use YAML frontmatter (`title`, `type`, `source_count`, `last_updated`, `tags`).
- Cross-links use Obsidian-style `[[page-name]]`.
- Filenames are kebab-case and lowercase.
- **Language:** wiki content is written in **Chinese**, but technical terms, system names, and acronyms stay in English. For example: "一个 **data-intensive application** 由 [[database]]、[[cache]]、[[search-index]] 等组件组成。" Keep terms such as OLTP, OLAP, ETL, HTAP, FaaS, GDPR, microservices, serverless, cloud-native, data warehouse, data lake, system of record, derived data, data minimization, and system names (MySQL, PostgreSQL, Snowflake, S3, etc.) untranslated.
- **Forward references:** When a source summary or concept page says a topic will be discussed in a later chapter, treat it as a promise. When that later chapter is ingested, backfill the referenced page and update or remove the placeholder sentence. Use the source summary’s “Open threads” section to make these promises explicit.

### Translation traps

When translating or paraphrasing English source material into Chinese for the wiki and playgrounds, preserve the **agency** and **causality** of the original. English technical writing often describes tools, frameworks, or systems as the actors that *cause* or *generate* behavior. Do not silently rewrite these sentences to make the human developer the actor.

- **Preserve who generates what.**  
  - Misleading: "ORM 的 lazy-loading 可能会让你不自觉地写出这样的代码：……"  
    This implies the developer writes the N+1 queries by hand.  
  - Better: "ORM 的 lazy-loading 机制可能会在你不知不觉中生成这样的查询：……"  
    This correctly attributes the generated queries to the ORM.

- **Distinguish "makes it easy to X" from "causes you to X".**  
  English phrases like "makes it easy to accidentally write..." describe an affordance or risk, not an accusation. Chinese renderings such as "让你不自觉地..." can shift blame/intentionality to the reader. Use "容易导致..." or "可能自动生成..." instead.

- **Watch for subject-verb reordering.**  
  Chinese often drops the explicit subject, which can make a tool-generated action sound like a user action. When in doubt, keep the tool/system as the explicit subject.

If a translated sentence would change who is doing the action, flag it and rephrase.

See `CLAUDE.md` for the full schema, page templates, and detailed workflows.
