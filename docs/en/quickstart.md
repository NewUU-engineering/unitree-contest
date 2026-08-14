# Quick start

The path from a clean machine to the first robot running in the simulator. The
first image build takes 10–20 minutes; subsequent launches take seconds.

---

## What you need

- **Docker** — Linux, Windows, or macOS, including Apple Silicon.
- About **8 GB** of free disk space.
- A browser.

No GPU is required: the simulator runs on the CPU; graphics are served to the
browser via noVNC.

??? tip "Installing Docker"

    - **Windows and macOS** — [Docker Desktop](https://www.docker.com/products/docker-desktop/).
    - **Linux** — [official installation guide](https://docs.docker.com/engine/install/).

---

## Step 1. Build and start the environment

From the repository root:

```bash
docker compose up --build
```

Or without compose:

```bash
docker build -t ghcr.io/newuu-engineering/agrokit:latest -f docker/Dockerfile .
docker run --rm -it -p 6080:6080 \
    -v "$PWD/solution:/workspace/solution" \
    ghcr.io/newuu-engineering/agrokit:latest
```

The container starts:

- **unitree_mujoco** — Unitree simulator (DDS domain 1, `lo`);
- **AgroKit** — Python framework and examples;
- **noVNC** — desktop in the browser on port 6080.

Environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `AGRO_ROBOT` | `go2` | Robot in simulator: `go2` or `g1` |
| `AGRO_START_SIM` | `1` | Start simulator on launch |
| `AGRO_START_DESKTOP` | `1` | Start noVNC |

Example for the G1 track:

```bash
AGRO_ROBOT=g1 docker compose up --build
```

---

## Step 2. Open the simulator

In your browser go to: **[http://localhost:6080](http://localhost:6080)**.

The noVNC window should show MuJoCo with the robot loaded. If the window is empty —
wait 10–15 seconds after the container starts.

---

## Step 3. Run an example

In a **new terminal** on the host:

```bash
docker compose exec agrokit bash
```

=== "Track 1 — Go2"

    ```bash
    python3 /workspace/examples/go2_scout.py
    ```

    The script moves through crop rows, finds plant diseases, and saves
    `field_report.json` in the current directory.

=== "Track 2 — G1"

    ```bash
    python3 /workspace/examples/g1_sorting.py
    ```

    Sorting demo: recognition, pinch grasp, placement into trays.

---

## Step 4. Write your solution

```bash
cp examples/go2_scout.py solution/main.py
```

The `solution/` folder is mounted at `/workspace/solution` — edit the file on the
host and run it inside the container.

---

## Step 5. Self-check with the judging script

```bash
agrokit-judge run /workspace/solution/main.py --scene orchard_qualifier
```

The script runs the solution in mock mode (without real DDS) and prints a
preliminary score breakdown.

---

## Local development without Docker

If you need to edit AgroKit on the host without the Unitree SDK:

```bash
cd agrokit && pip install -e .
AGROKIT_MOCK=1 AGRO_SCENES_DIR=../scenes python ../examples/go2_scout.py
```

Full simulator and DDS are available only inside the container.

---

## What's next

- [Starter Kit](starter-kit.md) — API description
- [Go2](tracks/go2.md) · [G1](tracks/g1.md) — track tasks
- [FAQ](faq.md) — common issues
