from __future__ import annotations

import shutil
import uuid
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from app.extraction.pdf import index_pdf
from app.models import DrawingReviewProject
from app.services.projects import load_project, save_project


app = FastAPI(title="Clark Dietz Drawing Review", version="0.1.0")

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/projects")
async def create_project(file: UploadFile = File(...)) -> DrawingReviewProject:
    filename = file.filename or "drawing-set.pdf"
    if not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF drawing sets are supported.")

    project_id = str(uuid.uuid4())
    target = UPLOAD_DIR / f"{project_id}.pdf"

    with target.open("wb") as output:
        shutil.copyfileobj(file.file, output)

    try:
        sheets = index_pdf(target)
    except Exception as exc:
        target.unlink(missing_ok=True)
        raise HTTPException(status_code=400, detail=f"Unable to read PDF: {exc}") from exc

    project = DrawingReviewProject(
        project_id=project_id,
        name=Path(filename).stem,
        source_filename=filename,
        sheets=sheets,
    )
    save_project(project)
    return project


@app.get("/api/projects/{project_id}")
def get_project(project_id: str) -> DrawingReviewProject:
    try:
        return load_project(project_id)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Project not found.") from exc


@app.get("/")
def index() -> FileResponse:
    return FileResponse("web/index.html")
