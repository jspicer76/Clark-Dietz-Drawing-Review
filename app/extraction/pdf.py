from __future__ import annotations

import re
from pathlib import Path

import fitz

from app.models import Confidence, Sheet


SHEET_NUMBER_RE = re.compile(r"\b([A-Z]{1,3}[-.]?\d{2,4})\b", re.IGNORECASE)


def index_pdf(path: Path) -> list[Sheet]:
    """Create a conservative first-pass sheet index from a PDF.

    This intentionally performs text-based indexing only. Sheet classification,
    infrastructure extraction, geometry, and vision analysis are separate stages.
    """
    doc = fitz.open(path)
    sheets: list[Sheet] = []

    for idx, page in enumerate(doc):
        text = page.get_text("text") or ""
        normalized = " ".join(text.split())
        match = SHEET_NUMBER_RE.search(normalized)
        sheet_number = match.group(1).upper() if match else None

        sheets.append(
            Sheet(
                sheet_id=f"sheet-{idx + 1:04d}",
                page_number=idx + 1,
                sheet_number=sheet_number,
                title=None,
                classification="unclassified",
                confidence=Confidence.medium if sheet_number else Confidence.low,
            )
        )

    return sheets
