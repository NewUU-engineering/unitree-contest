from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def _score_report(report_path: Path) -> dict[str, float]:
    if not report_path.exists():
        return {"task": 0.0, "perception": 0.0, "total": 0.0}

    import json

    data = json.loads(report_path.read_text())
    findings = data.get("findings", [])
    labels = {item.get("label") for item in findings}
    expected = {"powdery_mildew", "leaf_rust", "ripe_apple"}

    task = min(len(findings) / 3.0, 1.0) * 35.0
    perception = len(labels & expected) / len(expected) * 25.0
    total = task + perception

    return {"task": task, "perception": perception, "total": total}


def run_solution(script: Path, scene: str) -> int:
    script = script.resolve()
    env = os.environ.copy()
    env["AGRO_SCENE"] = scene
    env["AGROKIT_MOCK"] = "1"
    env["PYTHONPATH"] = "/workspace/agrokit:" + env.get("PYTHONPATH", "")

    print(f"[agrokit-judge] scene={scene}")
    print(f"[agrokit-judge] running {script}")

    result = subprocess.run([sys.executable, str(script)], env=env, cwd=script.parent)
    if result.returncode != 0:
        print(f"[agrokit-judge] solution exited with code {result.returncode}")
        return result.returncode

    report_path = script.parent / "field_report.json"
    scores = _score_report(report_path)
    print("[agrokit-judge] scores:")
    for key, value in scores.items():
        print(f"  {key}: {value:.1f}")

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="agrokit-judge")
    sub = parser.add_subparsers(dest="command", required=True)

    run_parser = sub.add_parser("run", help="Run a solution against a scene")
    run_parser.add_argument("script", type=Path, help="Path to main.py")
    run_parser.add_argument("--scene", default="orchard_qualifier")

    args = parser.parse_args(argv)
    if args.command == "run":
        return run_solution(args.script, args.scene)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
