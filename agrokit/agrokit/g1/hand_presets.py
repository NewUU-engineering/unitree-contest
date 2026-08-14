from __future__ import annotations

from enum import IntEnum
from typing import Literal

Side = Literal["right", "left", "both"]

# Official Inspire hand joint order on DDS (unitree_go MotorCmds_, 12 motors).
# q in [0, 1]: 0 = closed, 1 = open (Unitree G1 Inspire DFX docs).


class InspireJointIndex(IntEnum):
    RIGHT_PINKY = 0
    RIGHT_RING = 1
    RIGHT_MIDDLE = 2
    RIGHT_INDEX = 3
    RIGHT_THUMB_BEND = 4
    RIGHT_THUMB_ROTATION = 5
    LEFT_PINKY = 6
    LEFT_RING = 7
    LEFT_MIDDLE = 8
    LEFT_INDEX = 9
    LEFT_THUMB_BEND = 10
    LEFT_THUMB_ROTATION = 11


# Per-hand presets: (pinky, ring, middle, index, thumb_bend, thumb_rotation)
_GESTURES: dict[str, tuple[float, float, float, float, float, float]] = {
    "OPEN": (1.0, 1.0, 1.0, 1.0, 1.0, 0.8),
    "PINCH": (0.85, 0.85, 0.85, 0.15, 0.20, 0.6),
    "POWER_GRIP": (0.05, 0.05, 0.05, 0.05, 0.05, 0.5),
}

_RIGHT_INDICES = tuple(range(0, 6))
_LEFT_INDICES = tuple(range(6, 12))
