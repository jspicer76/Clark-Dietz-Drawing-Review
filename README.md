# Clark Dietz Drawing Review

Prototype drawing-review engine for civil engineering plan sets.

Initial focus: wastewater collection systems containing gravity sewer, force mains, and lift stations.

## Prototype workflow

PDF Upload → Sheet Index → Sheet Classification → Infrastructure Extraction → Quantity Takeoff → Evidence / Confidence → Reviewer Verification → Findings → Export

## Design principles

- Extract first; review second.
- Every extracted quantity or finding retains drawing evidence.
- Deterministic drawing information wins over AI estimates where practical.
- AI-generated interpretations remain review candidates until accepted by an engineer.
- The prototype stays decoupled from Clark-Dietz-QAQC, but uses integration-friendly IDs and export contracts.

## Local development

Backend:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

## Version 0.1 target

Upload a wastewater PDF and produce a reviewable project inventory with sheet-level evidence for:

- gravity sewer
- force mains
- manholes
- lift stations

The initial scaffold does not yet claim production-grade PDF interpretation or engineering QA/QC.
