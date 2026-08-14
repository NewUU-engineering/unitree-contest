from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

# All tests run without DDS / Unitree SDK.
os.environ.setdefault("AGROKIT_MOCK", "1")

REPO_ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("AGRO_SCENES_DIR", str(REPO_ROOT / "scenes"))


def test_go2_scout_produces_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from agrokit.go2 import Go2

    go2 = Go2(mock=True)
    assert len(go2.field.rows) >= 1

    for row in go2.field.rows:
        go2.nav.follow_row(row, speed=0.4)
        for det in go2.vision.detect():
            if det.label in {"powdery_mildew", "leaf_rust"}:
                go2.report.add_finding(det.label, go2.nav.pose, det.score)

    report_path = tmp_path / "field_report.json"
    go2.report.export(report_path)

    data = json.loads(report_path.read_text())
    assert len(data["findings"]) >= 1


def test_g1_hand_gestures():
    from agrokit.g1.hand import HandController

    hand = HandController(mock=True)
    for gesture in ("OPEN", "PINCH", "POWER_GRIP"):
        hand.set_gesture(gesture, side="right")


def test_g1_arm_workspace():
    from agrokit.g1 import G1

    g1 = G1(mock=True)
    g1.arm.move_to_point(0.40, 0.0, 0.80)
    g1.hand.set_gesture("PINCH")
    g1.arm.move_to_point(*g1.trays["A"])
    g1.hand.set_gesture("OPEN")


def test_field_scene_loaded():
    from agrokit.go2.field import load_field

    field = load_field("orchard_qualifier")
    assert field.name == "orchard_qualifier"
    assert len(field.rows) == 3


def test_judge_scores():
    from agrokit.judge.cli import run_solution

    script = REPO_ROOT / "examples" / "go2_scout.py"
    report = script.parent / "field_report.json"
    report.unlink(missing_ok=True)

    assert run_solution(script, "orchard_qualifier") == 0
    assert report.exists()
    report.unlink(missing_ok=True)
