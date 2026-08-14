#!/usr/bin/env bash
set -euo pipefail

export DISPLAY="${DISPLAY:-:99}"
export MUJOCO_GL="${MUJOCO_GL:-glx}"
export PYTHONPATH="/workspace/agrokit:${PYTHONPATH:-}"
export AGRO_SCENES_DIR="${AGRO_SCENES_DIR:-/workspace/scenes}"
export UNITREE_MUJOCO_DIR="${UNITREE_MUJOCO_DIR:-/opt/unitree_mujoco}"

start_desktop() {
  if [[ "${AGRO_START_DESKTOP:-1}" != "1" ]]; then
    return
  fi

  echo "[entrypoint] starting virtual desktop on ${DISPLAY}"
  Xvfb "${DISPLAY}" -screen 0 1280x720x24 &
  sleep 1
  fluxbox >/tmp/fluxbox.log 2>&1 &
  x11vnc -display "${DISPLAY}" -forever -shared -rfbport 5900 -nopw >/tmp/x11vnc.log 2>&1 &
  /opt/noVNC/utils/novnc_proxy --vnc localhost:5900 --listen 6080 >/tmp/novnc.log 2>&1 &
  echo "[entrypoint] noVNC -> http://localhost:6080"
}

start_simulator() {
  if [[ "${AGRO_START_SIM:-1}" != "1" ]]; then
    return
  fi

  python3 /docker/configure_mujoco.py
  echo "[entrypoint] starting unitree_mujoco (robot=${AGRO_ROBOT:-go2})"
  cd "${UNITREE_MUJOCO_DIR}/simulate_python"
  python3 unitree_mujoco.py >/tmp/unitree_mujoco.log 2>&1 &
}

start_desktop
start_simulator

echo "[entrypoint] workspace ready at /workspace"
echo "[entrypoint] examples: python3 /workspace/examples/go2_scout.py"
echo "[entrypoint] judge:     agrokit-judge run /workspace/solution/main.py --scene orchard_qualifier"

if [[ $# -gt 0 ]]; then
  exec "$@"
fi

exec bash -l
