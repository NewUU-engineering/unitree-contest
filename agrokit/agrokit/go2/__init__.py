from __future__ import annotations

from agrokit.dds import init_dds
from agrokit.go2.field import load_field
from agrokit.go2.nav import NavController
from agrokit.go2.report import FieldReport
from agrokit.go2.vision import VisionModule
from agrokit.types import Field


class Go2:
    """Unitree Go2 quadruped — scouting track."""

    def __init__(
        self,
        *,
        sim: bool = True,
        iface: str | None = None,
        mock: bool | None = None,
        scene: str | None = None,
    ) -> None:
        import os

        if mock is None:
            mock = os.environ.get("AGROKIT_MOCK") == "1"

        self._mock = mock
        if not mock:
            init_dds(sim, iface, allow_mock=False)

        self.nav = NavController(mock=mock)
        self.vision = VisionModule(mock=mock)
        self.report = FieldReport()
        self.field: Field = load_field(scene)
