#!/usr/bin/env python3
"""Render a PDF to page PNGs and a contact sheet for DOCX visual QA."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pypdfium2 as pdfium
    from PIL import Image, ImageDraw
except ImportError as exc:
    raise SystemExit("pypdfium2 and Pillow are required in the active Python environment") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages-dir", type=Path)
    parser.add_argument("--contact", type=Path)
    parser.add_argument("--scale", type=float, default=1.6)
    parser.add_argument("--cols", type=int, default=5)
    parser.add_argument("--thumb-width", type=int, default=300)
    parser.add_argument("--thumb-height", type=int, default=420)
    args = parser.parse_args()

    if not args.pdf.exists():
        raise SystemExit(f"PDF not found: {args.pdf}")
    if args.cols < 1:
        raise SystemExit("--cols must be at least 1")

    stem = args.pdf.stem
    pages_dir = args.pages_dir or args.pdf.with_name(f"{stem}_pages")
    contact_path = args.contact or args.pdf.with_name(f"contact_{stem}.png")
    pages_dir.mkdir(parents=True, exist_ok=True)
    contact_path.parent.mkdir(parents=True, exist_ok=True)

    document = pdfium.PdfDocument(str(args.pdf))
    thumbs = []
    for index in range(len(document)):
        image = document[index].render(scale=args.scale).to_pil().convert("RGB")
        image.save(pages_dir / f"page-{index + 1:02d}.png")
        thumb = image.copy()
        thumb.thumbnail((args.thumb_width, args.thumb_height))
        thumbs.append((index + 1, thumb))

    cell_width = args.thumb_width + 20
    cell_height = args.thumb_height + 45
    rows = (len(thumbs) + args.cols - 1) // args.cols
    sheet = Image.new("RGB", (args.cols * cell_width, rows * cell_height), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for index, (page_number, image) in enumerate(thumbs):
        x = (index % args.cols) * cell_width
        y = (index // args.cols) * cell_height
        sheet.paste(image, (x + (cell_width - image.width) // 2, y + 30))
        draw.text((x + 8, y + 8), f"page {page_number}", fill="black")
    sheet.save(contact_path)

    print(f"PAGES {len(document)}")
    print(f"PAGE_RENDERS {pages_dir.resolve()}")
    print(f"CONTACT {contact_path.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
