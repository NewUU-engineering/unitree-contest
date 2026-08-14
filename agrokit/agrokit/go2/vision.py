from __future__ import annotations

import os
from pathlib import Path

import cv2
import numpy as np

from agrokit.types import Detection


# Demo detections (table/workspace coordinates valid for G1 arm and Go2 map demo).
_DEMO_DETECTIONS = (
    Detection("powdery_mildew", 0.82, 0.45, 0.10, 0.80),
    Detection("ripe_apple", 0.91, 0.40, -0.08, 0.82, grade="A"),
    Detection("leaf_rust", 0.76, 0.38, 0.12, 0.79),
)


class VisionModule:
    """Camera frames and object detection."""

    def __init__(self, *, mock: bool = False) -> None:
        self._mock = mock
        self._model_cache: dict[str, object] = {}

    def frame(self) -> np.ndarray:
        if not self._mock:
            # Robot camera integration will land in a future release.
            pass
        return self._demo_frame()

    def _demo_frame(self) -> np.ndarray:
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(
            img,
            "AgroKit demo camera",
            (40, 240),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (180, 220, 180),
            2,
            cv2.LINE_AA,
        )
        return img

    def detect(self, model: str = "agro_yolo") -> list[Detection]:
        _ = self._load_model(model)
        # Until agro_yolo weights ship, return deterministic demo set.
        return list(_DEMO_DETECTIONS)

    def to_map(self, detection: Detection) -> tuple[float, float]:
        return detection.x, detection.y

    def pose_of(self, detection: Detection) -> tuple[float, float, float]:
        return detection.x, detection.y, detection.z

    def _load_model(self, model: str) -> object | None:
        if model in self._model_cache:
            return self._model_cache[model]

        weights = Path(os.environ.get("AGRO_MODELS_DIR", "/workspace/models")) / f"{model}.pt"
        if weights.exists():
            try:
                from ultralytics import YOLO

                self._model_cache[model] = YOLO(str(weights))
                return self._model_cache[model]
            except ImportError:
                print("[agrokit.vision] ultralytics not installed, using demo detections")

        self._model_cache[model] = None
        return None
