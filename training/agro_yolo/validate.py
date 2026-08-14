#!/usr/bin/env python3
"""Validate agro_yolo on a held-out split and print metrics."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--weights",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "models" / "agro_yolo.pt",
    )
    parser.add_argument("--data", type=Path, default=here / "dataset.yaml")
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--device", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.weights.exists():
        print(f"Weights not found: {args.weights}", file=sys.stderr)
        return 1

    try:
        from ultralytics import YOLO
    except ImportError:
        print("Install training deps: pip install -r training/requirements.txt", file=sys.stderr)
        return 1

    yolo = YOLO(str(args.weights))
    val_kwargs = {"data": str(args.data.resolve()), "imgsz": args.imgsz}
    if args.device:
        val_kwargs["device"] = args.device

    metrics = yolo.val(**val_kwargs)
    print(metrics)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
