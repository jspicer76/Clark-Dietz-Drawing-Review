# Architecture

## Purpose

The Drawing Review prototype converts a civil drawing set into structured, reviewable engineering information before generating QA/QC findings.

## Pipeline

1. **Ingest**
   - PDF upload
   - immutable source reference
   - project ID

2. **Sheet index**
   - page number
   - drawing/sheet number
   - title
   - discipline/type
   - confidence

3. **Extraction**
   - gravity sewer
   - force main
   - manholes
   - lift stations
   - evidence for every item

4. **Reconciliation**
   - combine repeated references
   - reconcile stationing, schedules, callouts, and geometry
   - flag conflicts instead of silently choosing

5. **Reviewer verification**
   - candidate
   - accepted
   - corrected
   - dismissed

6. **Engineering review**
   - consistency
   - completeness
   - hydraulic/design checks
   - constructability
   - standards/details
   - quantity reconciliation

7. **Export**
   - versioned JSON contract
   - future Clark-Dietz-QAQC ingestion

## Evidence rule

No extracted quantity or engineering finding should become authoritative without a traceable drawing source. Evidence can be text, drawing geometry, schedules, calculations, or later vision-assisted interpretation.

## Integration boundary

The drawing engine owns drawing comprehension and candidate findings. Clark-Dietz-QAQC should eventually own workflow, assignment, disposition, completion, and audit history.
