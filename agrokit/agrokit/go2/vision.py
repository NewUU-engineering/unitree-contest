from __future__ import annotations

import os
from pathlib import Path

import cv2
import numpy as np

from agrokit.types import Detection


# Demo detections when no weights are available (mock / CI).
_DEMO_DETECTIONS = (
    Detection("powdery_mildew", 0.82, 0.45, 0.10, 0.80),
    Detection("ripe_apple", 0.91, 0.40, -0.08, 0.82, grade="A"),
    Detection("leaf_rust", 0.76, 0.38, 0.12, 0.79),
)

_GRADE_BY_LABEL = {
    "ripe_apple": "A",
    "ripe_tomato": "A",
    "unripe_apple": "C",
    "defect_fruit": "C",
}


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

    def detect(self, model: str = "agro_yolo", *, conf: float = 0.35) -> list[Detection]:
        yolo = self._load_model(model)
        if yolo is None:
            return list(_DEMO_DETECTIONS)

        frame = self.frame()
        results = yolo(frame, verbose=False, conf=conf)
        detections: list[Detection] = []

        for result in results:
            names = result.names or {}
            if result.boxes is None:
                continue
            height, width = frame.shape[:2]
            for box in result.boxes:
                cls_id = int(box.cls[0])
                label = names.get(cls_id, str(cls_id))
                score = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                cx = (x1 + x2) / 2.0 / max(width, 1)
                cy = (y1 + y2) / 2.0 / max(height, 1)
                # Approximate workspace mapping until camera calibration ships.
                x = (cx - 0.5) * 0.8
                y = (0.5 - cy) * 0.6
                z = 0.82
                grade = _GRADE_BY_LABEL.get(label, "B")
                detections.append(Detection(label, score, x, y, z, grade=grade))

        return detections

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
