# Claude Code Wiki Schema

This repo builds an LLM-maintained wiki from *Designing Data-Intensive Applications* (2nd ed.).
The wiki is a persistent, compounding knowledge layer that sits between the raw EPUB Markdown and your questions.

## Directory layout

```
wiki/
├── index.md          # Catalog of all wiki pages, grouped by category
├── log.md            # Append-only ingest / query / lint history
├── sources/          # One summary page per book chapter
├── concepts/         # Explanations of ideas (OLTP, replication, consensus, ...)
├── entities/         # Pages for concrete systems, tools, people (Kafka, Spanner, ...)
└── synthesis/        # Comparisons, chapter overviews, evolving thesis
```

Raw source material lives in `raw/` and is read-only. Do not edit files under `raw/`.

## Page conventions

- Filenames are kebab-case, lowercase, ending in `.md`.
- Every page starts with YAML frontmatter:

  ```yaml
  ---
  title: "Page Title"
  type: source | concept | entity | synthesis
  source_count: 1          # how many book chapters/sources inform this page
  last_updated: 2026-06-22
  tags: [tag1, tag2]
  ---
  ```

- Cross-link liberally with Obsidian-style `[[page-name]]` links.
- Use `[[page-name|display text]]` when the raw link text would be awkward.
- Prefer short, stable page names. If a concept has an acronym, create the page under the full name and use the acronym in text (`[[online-transaction-processing|OLTP]]`).

## Ingest workflow

When asked to ingest a chapter:

1. Read `raw/chapterN/NN.md`.
2. Create or update `wiki/sources/chapter-NN.md` with:
   - A concise chapter summary.
   - Key takeaways.
   - Links to new or updated concept/entity pages.
   - Open questions / threads to revisit in later chapters.
3. For each important concept introduced or significantly advanced:
   - Create `wiki/concepts/<concept>.md` if it does not exist.
   - Update existing concept pages with new nuance, examples, or cross-references.
4. For each concrete system/tool/person mentioned:
   - Create `wiki/entities/<entity>.md` if it does not exist.
   - Keep entity pages factual and brief; link to the concepts they embody.
5. Update `wiki/index.md` to list all new/updated pages.
6. Append an entry to `wiki/log.md`.

## Query workflow

When asked a question:

1. Read `wiki/index.md` to locate relevant pages.
2. Read the relevant source/concept/entity pages.
3. Synthesize an answer with citations to specific pages.
4. If the answer reveals a useful comparison or connection, offer to file it under `wiki/synthesis/`.

## Lint workflow

When asked to lint the wiki, check for:

- Broken or missing `[[...]]` links.
- Concept pages that are mentioned often but do not yet exist.
- Contradictions between source summaries or concept pages.
- Pages with stale `last_updated` dates that no longer reflect the latest sources.
- Orphan pages with no inbound links.
- Inconsistent terminology.

## Markdown style

- Use ATX headings (`#`, `##`).
- Keep paragraphs focused; use bullets for lists of examples or trade-offs.
- Quote important definitions directly from the book when useful.
- For figures and diagrams, reference the original image in `raw/` with a relative link, e.g. `![ETL diagram](../raw/chapter1/ddia_0101.png)`.
