#!/usr/bin/env python3
"""Run agro_yolo on images or a webcam and save annotated previews."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--weights",
        type=Path,
        default=root / "models" / "agro_yolo.pt",
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=str(root / "training" / "datasets" / "agro" / "images" / "val"),
        help="Image, folder, or 0 for webcam",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=root / "training" / "runs" / "predict",
    )
    parser.add_argument("--conf", type=float, default=0.35)
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
    predict_kwargs = {
        "source": args.source,
        "conf": args.conf,
        "save": True,
        "project": str(args.out.parent),
        "name": args.out.name,
        "exist_ok": True,
    }
    if args.device:
        predict_kwargs["device"] = args.device

    yolo.predict(**predict_kwargs)
    print(f"Saved under {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
