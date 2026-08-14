from __future__ import annotations

import math
import time

from agrokit.types import FieldRow, Pose2D


class NavController:
    """Row following and goto — locomotion policy integration comes later."""

    def __init__(self, *, mock: bool = False) -> None:
        self._mock = mock
        self._pose = Pose2D(0.0, 0.0, 0.0)
        self._sport = None

        if not mock:
            try:
                from unitree_sdk2py.go2.sport.sport_client import SportClient

                self._sport = SportClient()
                self._sport.SetTimeout(10.0)
                self._sport.Init()
            except Exception as exc:  # pragma: no cover
                print(f"[agrokit.go2.nav] SportClient unavailable ({exc}), using mock motion")

    @property
    def pose(self) -> Pose2D:
        return self._pose

    def stop(self) -> None:
        if self._sport is not None:
            self._sport.StopMove()
        print("[agrokit.go2.nav] stop")

    def goto(self, x: float, y: float, yaw: float = 0.0, *, speed: float = 0.4) -> None:
        self._move_towards(Pose2D(x, y, yaw), speed=speed)

    def follow_row(self, row: FieldRow, *, speed: float = 0.4) -> None:
        if len(row.waypoints) < 2:
            raise ValueError(f"Row {row.row_id} must have at least two waypoints")

        print(f"[agrokit.go2.nav] follow_row({row.row_id}, speed={speed})")
        for waypoint in row.waypoints[1:]:
            self.goto(waypoint[0], waypoint[1], speed=speed)

    def _move_towards(self, target: Pose2D, *, speed: float) -> None:
        dx = target.x - self._pose.x
        dy = target.y - self._pose.y
        dist = math.hypot(dx, dy)
        if dist < 1e-3:
            self._pose = Pose2D(target.x, target.y, target.yaw)
            return

        if self._mock:
            print(f"[agrokit.go2.nav] goto({target.x:.2f}, {target.y:.2f})")
            self._pose = Pose2D(target.x, target.y, target.yaw)
            time.sleep(0.05)
            return

        if self._sport is not None:
            vx = speed * dx / dist
            vy = speed * dy / dist
            self._sport.Move(vx, vy, 0.0)

        start = self._pose
        steps = max(3, int(dist / max(speed, 0.1)))
        for step in range(1, steps + 1):
            t = step / steps
            self._pose = Pose2D(
                start.x + dx * t,
                start.y + dy * t,
                math.atan2(dy, dx),
            )
            time.sleep(0.05)

        if self._sport is not None:
            self._sport.StopMove()

        self._pose = Pose2D(target.x, target.y, target.yaw)
