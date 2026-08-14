from __future__ import annotations

import os
from dataclasses import dataclass

_SDK_READY = False
_SDK_ERROR: str | None = None

try:
    from unitree_sdk2py.core.channel import ChannelFactoryInitialize

    _SDK_READY = True
except ImportError as exc:  # pragma: no cover - depends on host env
    _SDK_ERROR = str(exc)


@dataclass(frozen=True)
class DdsConfig:
    sim: bool
    domain_id: int
    interface: str


def resolve_dds_config(sim: bool, iface: str | None = None) -> DdsConfig:
    if sim:
        return DdsConfig(sim=True, domain_id=1, interface="lo")
    return DdsConfig(
        sim=False,
        domain_id=0,
        interface=iface or os.environ.get("AGRO_ROBOT_IFACE", "eth0"),
    )


def init_dds(sim: bool, iface: str | None = None, *, allow_mock: bool = True) -> DdsConfig:
    """Initialize CycloneDDS channel factory (domain 1 + lo for simulation)."""
    config = resolve_dds_config(sim, iface)

    if not _SDK_READY:
        if allow_mock or os.environ.get("AGROKIT_MOCK_DDS") == "1":
            return config
        raise RuntimeError(
            "unitree_sdk2_python is not installed. "
            f"Import error: {_SDK_ERROR}"
        )

    ChannelFactoryInitialize(config.domain_id, config.interface)
    return config
