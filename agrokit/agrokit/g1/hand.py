from __future__ import annotations

import time
from typing import Any

from agrokit.dds import _SDK_READY
from agrokit.g1.hand_presets import (
    _GESTURES,
    _LEFT_INDICES,
    _RIGHT_INDICES,
    Side,
)

try:
    from unitree_sdk2py.core.channel import ChannelPublisher, ChannelSubscriber
    from unitree_sdk2py.idl.default import unitree_go_msg_dds__MotorCmd_
    from unitree_sdk2py.idl.unitree_go.msg.dds_ import MotorCmds_, MotorStates_
except ImportError:  # pragma: no cover
    ChannelPublisher = None  # type: ignore[misc, assignment]
    ChannelSubscriber = None  # type: ignore[misc, assignment]
    MotorCmds_ = None  # type: ignore[misc, assignment]
    MotorStates_ = None  # type: ignore[misc, assignment]
    unitree_go_msg_dds__MotorCmd_ = None  # type: ignore[misc, assignment]

TOPIC_CMD = "rt/inspire/cmd"
TOPIC_STATE = "rt/inspire/state"


class HandController:
    """High-level Inspire hand control via DDS presets."""

    def __init__(self, *, mock: bool = False) -> None:
        self._mock = mock or not _SDK_READY
        self._publisher = None
        self._subscriber = None
        self._msg: Any = None

        if not self._mock:
            self._publisher = ChannelPublisher(TOPIC_CMD, MotorCmds_)
            self._publisher.Init()
            self._subscriber = ChannelSubscriber(TOPIC_STATE, MotorStates_)
            self._subscriber.Init()
            self._msg = MotorCmds_()
            self._msg.cmds = [
                unitree_go_msg_dds__MotorCmd_() for _ in range(12)
            ]
            self.set_gesture("OPEN", side="both")

    def set_gesture(
        self,
        name: str,
        *,
        side: Side = "right",
        speed: float = 1.0,
    ) -> None:
        preset = _GESTURES.get(name.upper())
        if preset is None:
            raise ValueError(f"Unknown gesture {name!r}. Use: {', '.join(_GESTURES)}")

        speed = max(0.05, min(speed, 1.0))
        if self._mock:
            print(f"[agrokit.g1.hand] gesture={name} side={side} speed={speed:.2f}")
            time.sleep(0.15 / speed)
            return

        assert self._msg is not None
        if side in ("right", "both"):
            self._apply_preset(_RIGHT_INDICES, preset)
        if side in ("left", "both"):
            self._apply_preset(_LEFT_INDICES, preset)

        self._publisher.Write(self._msg)
        time.sleep(0.2 / speed)

    def set_joints(
        self,
        values: list[float],
        *,
        side: Side = "right",
    ) -> None:
        if len(values) != 6:
            raise ValueError("Expected 6 joint values for one hand")

        if self._mock:
            print(f"[agrokit.g1.hand] set_joints side={side} values={values}")
            return

        indices = _RIGHT_INDICES if side == "right" else _LEFT_INDICES
        self._apply_preset(indices, tuple(values))
        self._publisher.Write(self._msg)

    def state(self, *, side: Side = "right") -> list[float]:
        if self._mock:
            return [1.0] * 6

        msg = self._subscriber.Read()
        if msg is None:
            return [0.0] * 6

        indices = _RIGHT_INDICES if side == "right" else _LEFT_INDICES
        return [float(msg.states[i].q) for i in indices]

    def _apply_preset(
        self,
        indices: tuple[int, ...],
        preset: tuple[float, float, float, float, float, float],
    ) -> None:
        for joint_idx, value in zip(indices, preset):
            self._msg.cmds[joint_idx].q = float(value)
