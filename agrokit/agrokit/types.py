from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Pose2D:
    x: float
    y: float
    yaw: float = 0.0


@dataclass(frozen=True)
class Point3D:
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Detection:
    label: str
    score: float
    x: float
    y: float
    z: float = 0.0
    grade: str = "A"


@dataclass(frozen=True)
class FieldRow:
    row_id: str
    waypoints: tuple[tuple[float, float], ...]


@dataclass(frozen=True)
class Field:
    name: str
    rows: tuple[FieldRow, ...]
