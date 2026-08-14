from __future__ import annotations

from agrokit.dds import init_dds
from agrokit.g1.arm import ArmController
from agrokit.g1.hand import HandController
from agrokit.go2.vision import VisionModule
from agrokit.types import Point3D


DEFAULT_TRAYS: dict[str, tuple[float, float, float]] = {
    "A": (0.45, 0.25, 0.78),
    "B": (0.45, 0.0, 0.78),
    "C": (0.45, -0.25, 0.78),
}


class G1:
    """Unitree G1 humanoid — sorting track."""

    def __init__(
        self,
        *,
        sim: bool = True,
        iface: str | None = None,
        mock: bool | None = None,
    ) -> None:
        import os

        if mock is None:
            mock = os.environ.get("AGROKIT_MOCK") == "1"

        self._mock = mock
        if not mock:
            init_dds(sim, iface, allow_mock=False)

        self.arm = ArmController(mock=mock)
        self.hand = HandController(mock=mock)
        self.vision = VisionModule(mock=mock)
        self.trays: dict[str, tuple[float, float, float]] = dict(DEFAULT_TRAYS)

    def tray_point(self, grade: str) -> Point3D:
        coords = self.trays.get(grade, self.trays["C"])
        return Point3D(*coords)
