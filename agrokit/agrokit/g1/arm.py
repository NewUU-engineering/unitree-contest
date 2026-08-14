from __future__ import annotations

import time

from agrokit.types import Point3D


class ArmController:
    """Simplified arm interface. IK and low-level control will expand in later releases."""

    def __init__(self, *, mock: bool = False) -> None:
        self._mock = mock
        self._pose = Point3D(0.35, -0.15, 0.85)

    @property
    def pose(self) -> Point3D:
        return self._pose

    def move_home(self) -> None:
        self.move_to_point(0.35, -0.15, 0.85)

    def reachable(self, point: Point3D | tuple[float, float, float]) -> bool:
        if isinstance(point, tuple):
            x, y, z = point
        else:
            x, y, z = point.x, point.y, point.z
        # Conservative workspace box for G1 arm on sorting table.
        return 0.15 <= x <= 0.65 and -0.45 <= y <= 0.45 and 0.55 <= z <= 1.05

    def move_to_point(self, x: float, y: float, z: float) -> None:
        target = Point3D(x, y, z)
        if not self.reachable(target):
            raise ValueError(f"Target ({x}, {y}, {z}) is outside reachable workspace")

        if self._mock:
            print(f"[agrokit.g1.arm] move_to_point({x:.3f}, {y:.3f}, {z:.3f})")
            time.sleep(0.05)
            self._pose = target
            return

        start = self._pose
        steps = 10
        for step in range(1, steps + 1):
            t = step / steps
            self._pose = Point3D(
                start.x + (x - start.x) * t,
                start.y + (y - start.y) * t,
                start.z + (z - start.z) * t,
            )
            time.sleep(0.03)

        self._pose = target
