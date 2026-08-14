# Learning materials

A path for students: from zero to a working solution in AgroKit. Materials are
grouped by topic — follow blocks in order or pick selectively if a topic is already
familiar.

[Quick start](quickstart.md){ .md-button .md-button--primary }
[Starter Kit](starter-kit.md){ .md-button }

---

## 4-week roadmap

| Week | Goal | Actions |
|--------|------|----------|
| 1 | Environment | Docker, `go2_scout.py` / `g1_sorting.py` in mock, read [Starter Kit](starter-kit.md) |
| 2 | Your algorithm | Code in `solution/`, detection filtering, JSON report, run `agrokit-judge` |
| 3 | Computer vision | Fine-tune `agro_yolo`, see [Training models](training-models.md) |
| 4 | Sim-to-real | Calibration, tests at the NEWUU arena, semifinal preparation |

!!! tip "Mock mode"

    Without a robot and without GPU: `AGROKIT_MOCK=1 python examples/go2_scout.py` —
    all modules print actions to the console; tests pass locally.

---

## AgroKit — what you work with

### Architecture

```
solution/main.py          ← your code
    ↓
agrokit.go2 / agrokit.g1  ← high-level API
    ↓
Unitree SDK + DDS         ← link to simulator or robot
```

The same code in simulation and on hardware — only `sim=True/False` and the network
interface change. Details: [Stack](stack.md#safety-rules).

### Modules by track

=== "Go2 — scout"

    | Module | Task |
    |--------|--------|
    | `go2.nav` | motion, `follow_row`, `goto` |
    | `go2.vision` | frame, `detect("agro_yolo")` |
    | `go2.report` | findings → JSON |
    | `go2.field` | rows from YAML scene |

    Example: [`examples/go2_scout.py`](https://github.com/NewUU-engineering/unitree-contest/blob/main/examples/go2_scout.py)

=== "G1 — sorter"

    | Module | Task |
    |--------|--------|
    | `g1.arm` | `move_to_point(x, y, z)` |
    | `g1.hand` | presets `PINCH`, `POWER_GRIP`, `OPEN` |
    | `g1.vision` | same detections as Go2 |
    | `g1.trays` | tray coordinates A / B / C |

    Example: [`examples/g1_sorting.py`](https://github.com/NewUU-engineering/unitree-contest/blob/main/examples/g1_sorting.py)

### Judging run

```bash
agrokit-judge run solution/main.py --scene orchard_qualifier
```

Scenes live in `scenes/*.yaml`. Random seed is fixed by organizers — the result
must be reproducible.

### Repository and Docker

- Clone: [github.com/NewUU-engineering/unitree-contest](https://github.com/NewUU-engineering/unitree-contest)
- Solution is mounted at `/workspace/solution`
- Image: `ghcr.io/newuu-engineering/agrokit:latest`

---

## Python

Minimum to get started:

- functions, classes, `dataclass`;
- `pathlib`, working with JSON;
- virtual environment and `pip install -e agrokit`.

Useful resources:

- [Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Real Python](https://realpython.com/) — topic articles
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)

---

## ROS 2 and navigation

Go2 uses ROS 2 patterns (Nav2, `cmd_vel`), but in the Starter Kit they are
wrapped in `go2.nav`. For deeper study:

| Resource | Link |
|--------|--------|
| ROS 2 Humble docs | [docs.ros.org/humble](https://docs.ros.org/en/humble/index.html) |
| Nav2 | [navigation.ros.org](https://navigation.ros.org/) |
| Unitree ROS2 (Go2) | [unitree_ros2](https://github.com/unitreerobotics/unitree_ros2) |

Videos:

- [ROS 2 — Open Robotics official channel](https://www.youtube.com/@OpenRoboticsOrg)
- [Programming with ROS 2 (The Construct)](https://www.youtube.com/playlist?list=PLl0b7nXGaLH8iX_3qZEpZf-sBBz0-Awnf)

---

## Computer vision

Competition tasks use **YOLO** for disease and fruit detection.

1. Understand the `Detection` format in AgroKit (`label`, `score`, `x`, `y`, `z`, `grade`).
2. Run the demo: `go2.vision.detect("agro_yolo")` without weights.
3. Fine-tune the model on your photos — [Training models](training-models.md).

| Resource | Link |
|--------|--------|
| Ultralytics YOLOv8 docs | [docs.ultralytics.com](https://docs.ultralytics.com/) |
| OpenCV Python | [docs.opencv.org](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) |
| CVAT (annotation) | [cvat.ai](https://www.cvat.ai/) |

Videos:

- [Ultralytics — YOLOv8 official](https://www.youtube.com/watch?v=UN5H7rJ5BpE)
- [Train YOLOv8 on custom dataset](https://www.youtube.com/watch?v=wuZtUMEiKWY)

---

## Unitree and simulation

| Resource | Link |
|--------|--------|
| Unitree SDK2 Python | [unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python) |
| unitree_mujoco (sim) | [unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco) |
| Unitree RL Lab | [unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab) |
| Inspire Hand (G1) | see [G1 track — hand](tracks/g1.md#hand-control) |

YouTube — official channel and platform overviews:

- [Unitree Robotics](https://www.youtube.com/@unitree-robotics)
- [Unitree Go2 — product overview](https://www.unitree.com/go2)

MuJoCo in our Docker opens via **noVNC** on port 6080 — see
[Quick start](quickstart.md).

---

## Manipulation and G1

- Inverse kinematics — `g1.arm.move_to_point`; in v0.1 this is interpolation, not a
  full IK solver.
- Grasp is **positional only**; choose preset and speed for artificial fruit on the
  table.

| Resource | Link |
|--------|--------|
| LeRobot (imitation learning) | [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot) |
| Modern Robotics (theory) | [modernrobotics.northwestern.edu](http://modernrobotics.northwestern.edu/) |

Teleoperation in the final uses the Unitree **Teleoperation Kit**; materials will
appear closer to stage three.

---

## Videos from NEWUU *(coming soon)*

The organizing committee is preparing short videos:

- [ ] Competition and track overview
- [ ] Docker + first launch in 10 minutes
- [ ] Line-by-line walkthrough of `go2_scout.py`
- [ ] Walkthrough of `g1_sorting.py` and hand presets
- [ ] `agrokit-judge` run and report breakdown

Links will be added to this page after publication on the
[NEWUU YouTube channel](https://www.youtube.com/@newuu-robotics) *(replace with
the actual channel)*.

---

## What to read next

1. [Choose a track](tracks/index.md)
2. [Competition stages](stages.md)
3. [Scoring](scoring.md) — what judges look for in code and runs
4. [FAQ](faq.md)
5. [Registration](registration.md)

Questions: [robotics@newuu.uz](mailto:robotics@newuu.uz)
