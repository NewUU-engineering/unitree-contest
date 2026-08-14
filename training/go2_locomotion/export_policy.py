#!/usr/bin/env python3
"""Package a trained Go2 locomotion checkpoint for AgroKit deployment."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import yaml

DEFAULT_METADATA = {
    "robot": "unitree_go2",
    "control_hz": 50,
    "obs_dim": 48,
    "action_dim": 12,
    "input_names": ["obs"],
    "output_names": ["actions"],
    "notes": "Fill obs/action dims after training. Wire into agrokit.go2.nav separately.",
}


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True, help="Trained .pt or .onnx")
    parser.add_argument(
        "--out",
        type=Path,
        default=root / "models" / "go2_locomotion",
        help="Output directory for AgroKit bundle",
    )
    parser.add_argument(
        "--metadata",
        type=Path,
        help="Optional YAML with obs/action dimensions and control rate",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.checkpoint.exists():
        print(f"Checkpoint not found: {args.checkpoint}", file=sys.stderr)
        return 1

    args.out.mkdir(parents=True, exist_ok=True)
    suffix = args.checkpoint.suffix.lower()
    if suffix == ".onnx":
        dest_name = "policy.onnx"
    else:
        dest_name = "policy.pt"

    dest = args.out / dest_name
    shutil.copy2(args.checkpoint, dest)

    meta_path = args.out / "metadata.yaml"
    if args.metadata and args.metadata.exists():
        shutil.copy2(args.metadata, meta_path)
    elif not meta_path.exists():
        meta_path.write_text(
            yaml.dump(DEFAULT_METADATA, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    print(f"Bundled locomotion policy → {args.out}")
    print(f"  weights: {dest.name}")
    print(f"  metadata: {meta_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
