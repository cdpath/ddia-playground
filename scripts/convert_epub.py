#!/usr/bin/env python3
"""Convert an epub into per-chapter markdown with images alongside.

Actual book chapters are detected from "Chapter N." headings and placed in
chapterN/{NN}.md. Frontmatter/backmatter are grouped into their own dirs.
"""

import os
import re
import shutil
from pathlib import Path

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter


REPO_ROOT = Path(__file__).resolve().parent.parent
EPUB_FILE = REPO_ROOT / "Designing.Data-Intensive.Applications.2nd.2026.2.epub"
OUT_DIR = REPO_ROOT / "raw"


def detect_chapter_number(soup: BeautifulSoup) -> int | None:
    """Return chapter number if the document starts a numbered chapter."""
    pattern = re.compile(r"chapter\s*(\d+)", re.IGNORECASE)
    for tag in soup.find_all(["h1", "h2"]):
        text = tag.get_text(strip=True)
        m = pattern.search(text)
        if m:
            return int(m.group(1))
    return None


def extract_title(soup: BeautifulSoup) -> str | None:
    for tag in soup.find_all(["h1", "h2"]):
        text = tag.get_text(strip=True)
        if text:
            return text
    return None


def unique_image_path(target_dir: Path, media_name: str) -> Path:
    image_path = target_dir / media_name
    counter = 1
    while image_path.exists():
        stem = Path(media_name).stem
        suffix = Path(media_name).suffix
        image_path = target_dir / f"{stem}_{counter}{suffix}"
        counter += 1
    return image_path


_MARKER_RE = re.compile(r"^(\d+)(?:_\d+)?\.(png|jpg|jpeg|gif)$", re.IGNORECASE)


def circled_number(n: int) -> str:
    """Return a Unicode circled number, falling back to (n) if out of range."""
    if 1 <= n <= 20:
        return chr(0x245F + n)
    return f"({n})"


def is_number_marker(media_name: str, image_bytes: bytes) -> int | None:
    """If image is a simple numbered marker, return its number; else None."""
    m = _MARKER_RE.match(media_name)
    if not m:
        return None
    # These marker glyphs are tiny PNGs (a few hundred bytes).
    if len(image_bytes) > 1000:
        return None
    return int(m.group(1))


def convert_document(soup: BeautifulSoup, item_by_href: dict, doc_name: str,
                     target_dir: Path) -> str:
    """Extract images into target_dir, rewrite src, and return markdown."""
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue
        resolved = os.path.normpath(
            os.path.join(os.path.dirname(doc_name), src)
        ).replace("\\", "/")
        image_item = item_by_href.get(resolved)
        if not image_item:
            continue

        media_name = Path(resolved).name
        ext = Path(media_name).suffix.lower()
        if ext not in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}:
            ext = ".png"
            media_name = Path(media_name).stem + ext

        content = image_item.get_content()
        marker_num = is_number_marker(media_name, content)
        if marker_num is not None:
            # Replace the inline marker image with a circled number.
            span = soup.new_string(circled_number(marker_num))
            img.replace_with(span)
            continue

        image_path = unique_image_path(target_dir, media_name)
        image_path.write_bytes(content)
        img["src"] = image_path.name

    body = soup.find("body") or soup
    md = MarkdownConverter(heading_style="ATX").convert(str(body))
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md


def main():
    shutil.rmtree(OUT_DIR, ignore_errors=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    book = epub.read_epub(EPUB_FILE)

    item_by_href = {}
    for item in book.get_items():
        if item.get_name():
            item_by_href[item.get_name()] = item

    spine_ids = [sid for sid, _ in book.spine]
    docs = []
    for sid in spine_ids:
        item = book.get_item_with_id(sid)
        if item and item.get_type() == ebooklib.ITEM_DOCUMENT:
            docs.append(item)

    frontmatter_parts = []
    backmatter_parts = []
    first_chapter_seen = False

    for doc in docs:
        soup = BeautifulSoup(doc.get_content(), "html.parser")
        for tag in soup.find_all(["script", "style"]):
            tag.decompose()

        chapter_num = detect_chapter_number(soup)
        title = extract_title(soup)

        if chapter_num is not None:
            first_chapter_seen = True
            target_dir = OUT_DIR / f"chapter{chapter_num}"
            target_dir.mkdir(parents=True, exist_ok=True)
            md = convert_document(soup, item_by_href, doc.get_name(), target_dir)
            md_path = target_dir / f"{chapter_num:02d}.md"
            md_path.write_text(md, encoding="utf-8")
            print(f"Wrote {md_path} ({title or 'no title'})")
        else:
            section = backmatter_parts if first_chapter_seen else frontmatter_parts
            section.append((title, soup, doc.get_name()))

    # Write merged frontmatter and backmatter
    def write_section(parts, section_name):
        if not parts:
            return
        sec_dir = OUT_DIR / section_name
        sec_dir.mkdir(parents=True, exist_ok=True)

        md_parts = []
        for title, soup, doc_name in parts:
            md = convert_document(soup, item_by_href, doc_name, sec_dir)
            if title:
                md = f"# {title}\n\n{md}"
            md_parts.append(md)

        md_path = sec_dir / f"{section_name}.md"
        md_path.write_text("\n\n---\n\n".join(md_parts), encoding="utf-8")
        print(f"Wrote {md_path}")

    write_section(frontmatter_parts, "frontmatter")
    write_section(backmatter_parts, "backmatter")

    print(f"\nDone. Output in ./{OUT_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
