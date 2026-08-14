# AgroTech Robotics Challenge — dev/simulation environment
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    CYCLONEDDS_HOME=/opt/cyclonedds \
    UNITREE_MUJOCO_DIR=/opt/unitree_mujoco \
    AGRO_SCENES_DIR=/workspace/scenes \
    AGRO_MODELS_DIR=/workspace/models \
    AGRO_ROBOT=go2 \
    AGRO_START_SIM=1 \
    AGRO_START_DESKTOP=1 \
    DISPLAY=:99 \
    PYTHONUNBUFFERED=1

# --- system packages ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    build-essential \
    ca-certificates \
    cmake \
    curl \
    fluxbox \
    git \
    libgl1-mesa-dri \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgl1 \
    mesa-utils \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    x11vnc \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# --- CycloneDDS 0.10.2 (must match robot firmware) ---
RUN git clone --depth 1 --branch releases/0.10.x https://github.com/eclipse-cyclonedds/cyclonedds.git /tmp/cyclonedds \
    && cmake -S /tmp/cyclonedds -B /tmp/cyclonedds/build \
        -DCMAKE_INSTALL_PREFIX="${CYCLONEDDS_HOME}" \
        -DBUILD_EXAMPLES=OFF \
    && cmake --build /tmp/cyclonedds/build --target install -j"$(nproc)" \
    && rm -rf /tmp/cyclonedds

# --- noVNC for browser GUI ---
RUN git clone --depth 1 https://github.com/novnc/noVNC.git /opt/noVNC \
    && git clone --depth 1 https://github.com/novnc/websockify /opt/noVNC/utils/websockify

# --- Python robotics stack ---
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir \
        mujoco \
        numpy \
        opencv-python-headless \
        pyyaml \
        pygame

ENV CYCLONEDDS_HOME="${CYCLONEDDS_HOME}"
RUN git clone --depth 1 https://github.com/unitreerobotics/unitree_sdk2_python.git /tmp/unitree_sdk2_python \
    && pip3 install --no-cache-dir /tmp/unitree_sdk2_python \
    && rm -rf /tmp/unitree_sdk2_python

# --- MuJoCo simulator with Unitree robot models ---
RUN git clone --depth 1 https://github.com/unitreerobotics/unitree_mujoco.git "${UNITREE_MUJOCO_DIR}"

# --- AgroKit ---
WORKDIR /workspace
COPY agrokit /workspace/agrokit
COPY examples /workspace/examples
COPY scenes /workspace/scenes
RUN pip3 install --no-cache-dir -e /workspace/agrokit

COPY docker/configure_mujoco.py /docker/configure_mujoco.py
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN mkdir -p /workspace/solution /workspace/models

EXPOSE 6080

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash", "-l"]
