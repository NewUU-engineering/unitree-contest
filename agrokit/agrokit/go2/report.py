from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from agrokit.types import Pose2D


@dataclass
class Finding:
    label: str
    pose: Pose2D
    score: float


@dataclass
class FieldReport:
    findings: list[Finding] = field(default_factory=list)

    def add_finding(self, label: str, pose: Pose2D, score: float) -> None:
        self.findings.append(Finding(label=label, pose=pose, score=score))

    def export(self, path: str | Path) -> None:
        payload = {
            "findings": [
                {
                    "label": item.label,
                    "score": item.score,
                    "pose": asdict(item.pose),
                }
                for item in self.findings
            ]
        }
        Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False))
        print(f"[agrokit.go2.report] exported {len(self.findings)} findings -> {path}")
