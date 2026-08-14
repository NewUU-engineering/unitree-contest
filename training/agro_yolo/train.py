#!/usr/bin/env python3
"""Train the agro_yolo detector and export weights for AgroKit."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    root = here.parent.parent

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=here / "dataset.yaml",
        help="YOLO dataset YAML (Ultralytics format)",
    )
    parser.add_argument(
        "--model",
        default="yolov8n.pt",
        help="Base checkpoint: yolov8n.pt, yolov8s.pt, … or path to .pt",
    )
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--device", default="", help="cuda:0, cpu, or empty = auto")
    parser.add_argument(
        "--project",
        type=Path,
        default=here.parent / "runs" / "agro_yolo",
        help="Ultralytics project directory",
    )
    parser.add_argument("--name", default="train", help="Run name inside project")
    parser.add_argument(
        "--export-dir",
        type=Path,
        default=root / "models",
        help="Where to copy best.pt as agro_yolo.pt for AgroKit",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume last run in project/name",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.data.exists():
        print(f"Dataset config not found: {args.data}", file=sys.stderr)
        print("See training/datasets/README.md for layout.", file=sys.stderr)
        return 1

    try:
        from ultralytics import YOLO
    except ImportError:
        print("Install training deps: pip install -r training/requirements.txt", file=sys.stderr)
        return 1

    yolo = YOLO(args.model)
    train_kwargs = {
        "data": str(args.data.resolve()),
        "epochs": args.epochs,
        "imgsz": args.imgsz,
        "batch": args.batch,
        "project": str(args.project.parent.resolve()),
        "name": args.name,
        "exist_ok": True,
    }
    if args.device:
        train_kwargs["device"] = args.device
    if args.resume:
        train_kwargs["resume"] = True

    results = yolo.train(**train_kwargs)
    save_dir = Path(results.save_dir)
    best = save_dir / "weights" / "best.pt"
    if not best.exists():
        print(f"Training finished but weights missing: {best}", file=sys.stderr)
        return 1

    args.export_dir.mkdir(parents=True, exist_ok=True)
    dest = args.export_dir / "agro_yolo.pt"
    shutil.copy2(best, dest)
    print(f"\nAgroKit weights: {dest}")
    print("In Docker: mount models/ or set AGRO_MODELS_DIR=/workspace/models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
