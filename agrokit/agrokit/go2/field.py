from __future__ import annotations

import os
from pathlib import Path

import yaml

from agrokit.types import Field, FieldRow


def _default_field() -> Field:
    rows = tuple(
        FieldRow(
            row_id=f"row_{idx}",
            waypoints=((0.0, idx * 1.5), (8.0, idx * 1.5)),
        )
        for idx in range(1, 4)
    )
    return Field(name="default_orchard", rows=rows)


def load_field(scene: str | None = None) -> Field:
    scene_name = scene or os.environ.get("AGRO_SCENE", "orchard_qualifier")
    scenes_dir = Path(os.environ.get("AGRO_SCENES_DIR", "/workspace/scenes"))
    scene_path = scenes_dir / f"{scene_name}.yaml"

    if not scene_path.exists():
        return _default_field()

    data = yaml.safe_load(scene_path.read_text())
    rows = tuple(
        FieldRow(
            row_id=row["id"],
            waypoints=tuple(tuple(pt) for pt in row["waypoints"]),
        )
        for row in data.get("rows", [])
    )
    return Field(name=data.get("name", scene_name), rows=rows)
