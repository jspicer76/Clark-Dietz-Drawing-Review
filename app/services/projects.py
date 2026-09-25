from __future__ import annotations

import json
from pathlib import Path

from app.models import DrawingReviewProject


DATA_DIR = Path("data/projects")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_project(project: DrawingReviewProject) -> None:
    path = DATA_DIR / f"{project.project_id}.json"
    path.write_text(project.model_dump_json(indent=2), encoding="utf-8")


def load_project(project_id: str) -> DrawingReviewProject:
    path = DATA_DIR / f"{project_id}.json"
    if not path.exists():
        raise FileNotFoundError(project_id)
    return DrawingReviewProject.model_validate(json.loads(path.read_text(encoding="utf-8")))
