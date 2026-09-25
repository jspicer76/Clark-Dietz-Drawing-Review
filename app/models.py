from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Confidence(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class ReviewState(str, Enum):
    candidate = "candidate"
    accepted = "accepted"
    corrected = "corrected"
    dismissed = "dismissed"


class Sheet(BaseModel):
    sheet_id: str
    page_number: int = Field(ge=1)
    sheet_number: str | None = None
    title: str | None = None
    classification: str = "unclassified"
    confidence: Confidence = Confidence.low


class Evidence(BaseModel):
    sheet_id: str
    page_number: int = Field(ge=1)
    source_type: Literal["text", "geometry", "schedule", "vision", "calculation"]
    excerpt: str | None = None
    bbox: tuple[float, float, float, float] | None = None


class InfrastructureItem(BaseModel):
    item_id: str
    category: Literal["gravity_sewer", "force_main", "manhole", "lift_station", "other"]
    subtype: str | None = None
    size: str | None = None
    material: str | None = None
    quantity: float | None = None
    unit: str | None = None
    label: str | None = None
    confidence: Confidence = Confidence.low
    review_state: ReviewState = ReviewState.candidate
    evidence: list[Evidence] = Field(default_factory=list)


class Finding(BaseModel):
    finding_id: str
    title: str
    category: str
    severity: Literal["info", "review", "potential_issue"] = "review"
    description: str
    review_state: ReviewState = ReviewState.candidate
    evidence: list[Evidence] = Field(default_factory=list)


class DrawingReviewProject(BaseModel):
    project_id: str
    name: str
    source_filename: str
    sheets: list[Sheet] = Field(default_factory=list)
    inventory: list[InfrastructureItem] = Field(default_factory=list)
    findings: list[Finding] = Field(default_factory=list)
