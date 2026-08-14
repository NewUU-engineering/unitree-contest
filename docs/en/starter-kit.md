# Starter Kit

**AgroKit** is the Python framework organizers provide so participants write
algorithms, not drivers. It hides motors, kinematics, network protocols, and
differences between simulator and hardware.

!!! note "v0.1 status"

    AgroKit and the Docker image are available in the repository. Basic examples
    work; Go2 locomotion policy and trained `agro_yolo` are in development.
    See [Quick start](quickstart.md).

---

## What's in the kit

- **Environment container** — simulator, ROS 2 Humble, Unitree SDK, all
  dependencies. Built for x86 and ARM.
- **`agrokit` library** — high-level API for both tracks.
- **Ready-made scenes** — virtual “orchard” for Go2 and sorting table for G1
  (laboratory analogs of agro scenarios).
- **Pretrained models** — base agro detector and locomotion controller.
- **Working examples** — minimal solutions for both tracks that run out of the box
  and serve as a starting point.
- **Judging script** — the same one used for scoring, so you can self-check before
  submission.
- **Training scripts** — the
  [`training/`](https://github.com/NewUU-engineering/unitree-contest/tree/main/training)
  directory in the repository for `agro_yolo` and (organizing committee) Go2 policy.
  Brief overview on the site:
  [Training models](training-models.md).

For students: [Learning materials](learn.md) — roadmap, links, and videos.

---

## Go2 track API

```python title="go2_scout.py"
from agrokit.go2 import Go2

go2 = Go2(sim=True)

for row in go2.field.rows:
    go2.nav.follow_row(row, speed=0.4)

    for det in go2.vision.detect(model="agro_yolo"):
        if det.label in ("powdery_mildew", "leaf_rust"):
            go2.report.add_finding(det.label, go2.nav.pose, det.score)

go2.report.export("field_report.json")
```

| Module | Main methods |
|---|---|
| `go2.nav` | `goto(x, y, yaw)`, `follow_row(row, speed)`, `stop()`, `pose` property |
| `go2.vision` | `frame()`, `detect(model)`, `to_map(detection)` |
| `go2.map` | `build()`, `load(path)`, `rows`, `obstacles` |
| `go2.report` | `add_finding(label, pose, score)`, `export(path)` |

Robot locomotion is not yours and is not scored: `nav` plans the route through
Nav2, and the built-in locomotion controller turns velocity commands into leg
motion. The same controller runs on the real robot, so behavior matches.

---

## G1 track API

```python title="g1_sorting.py"
from agrokit.g1 import G1

g1 = G1(sim=True)

for fruit in g1.vision.detect(model="agro_yolo"):
    g1.arm.move_to_point(x=fruit.x, y=fruit.y, z=fruit.z)
    g1.hand.set_gesture("PINCH", speed=0.3)
    g1.arm.move_to_point(*g1.trays[fruit.grade])
    g1.hand.set_gesture("OPEN")
```

| Module | Main methods |
|---|---|
| `g1.arm` | `move_to_point(x, y, z)`, `move_home()`, `reachable(point)` |
| `g1.hand` | `set_gesture(name, side, speed)`, `set_joints(values)`, `state()` |
| `g1.vision` | `frame()`, `detect(model)`, `pose_of(detection)` |
| `g1.trays` | Tray coordinates by quality category |

Hand control is reduced to named presets — `PINCH`, `POWER_GRIP`, `OPEN`. You do
not need to work with twelve motors and the RS485 protocol; details of how this
works internally are described in the
[G1 track section](tracks/g1.md#hand-control).

---

## Moving from simulation to hardware

The only thing that changes when moving to the NEWUU laboratory is connection
parameters. Solution logic stays the same.

=== "Simulation"

    ```python
    robot = Go2(sim=True)
    # domain_id = 1, interface "lo"
    ```

=== "Real robot"

    ```python
    robot = Go2(sim=False, iface="enp3s0")
    # domain_id = 0, physical interface
    ```

!!! warning

    The `sim=False` flag may be used only in the Organizer's laboratory under judge
    supervision. See [safety rules](stack.md#safety-rules).

---

## Solution structure

The team submits a repository of the following form:

```
solution/
├── main.py            # entry point, called by the judging script
├── perception/        # your models and image processing
├── control/           # navigation or manipulation logic
├── models/            # weights, if you fine-tuned the detector
├── requirements.txt   # additional dependencies
└── README.md          # approach description and run instructions
```

The judging script runs `main.py` in the standard container on a fixed scene. If
the solution needs extra packages, they must be listed in `requirements.txt` and
install without internet access during the run.

---

## Limitations worth knowing upfront

**Grasp is positional.** The G1 hand moves to commanded finger angles; there is no
force feedback in the base API. For soft fruit, use reduced closing speed and tune
the target position experimentally.

**The out-of-the-box detector is only a starting point.** The base model is trained
on a limited set and loses accuracy on real photos. Fine-tuning for specific
lighting conditions is expected team work.

**Runs are deterministic.** The judging script fixes the random seed so the result
is reproducible. Solutions that rely on luck in a single run will not show stable
results.
