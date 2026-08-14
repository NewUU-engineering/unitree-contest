# Track 1 — Unitree Go2

## “Autonomous field and orchard scout”

**Focus:** navigation, computer vision, map building, autonomous patrolling.

The quadruped robot replaces an agronomist on regular rounds: it moves through crop
rows, inspects plants, records problem areas, and delivers a ready report with
coordinates. Robot locomotion is not part of the competition — you do not need to
teach it to walk; the [Starter Kit](../starter-kit.md) includes a ready locomotion
controller that accepts velocity commands.

---

## Stage 1 — Simulation

**Environment:** virtual orchard and greenhouse with plant rows.

**Task:** move through crop rows, detect diseased plants and ripe fruit using YOLO
and OpenCV, output coordinates of findings.

**Result:** navigation script and detection module producing a structured list of
objects with map positions.

What matters at this stage:

- complete the route without hitting plants or getting stuck at row end;
- distinguish diseased from healthy plants and ripe from unripe fruit;
- correctly map detections from image to map coordinates;
- avoid false positives — they are penalized as much as misses.

---

## Stage 2 — Real Go2

**Location:** training arena in the NEWUU laboratory — artificial beds, plant mock-ups
with agro-disease markers, and **artificial fruit** on stands.

**Task:** autonomously follow the route, assess “plant” condition, generate a farmer
report.

Physics is added to the algorithm: uneven floor, paw slip, laboratory lighting and
glare on props, lidar and camera noise. A detector trained only on simulator renders
will almost certainly lose accuracy — prepare to fine-tune on arena photos and test
under different lighting.

!!! tip "Tip"

    Make the report both machine-readable and human-readable: JSON for the judging
    script and a brief summary for the agronomist. Report quality is part of the
    score.

---

## Stage 3 — Final

**Task:** time-limited patrolling with dynamic obstacles and transmission of found
object coordinates to a central server.

Conditions change during the run: obstacles appear on the route that were not present
when the map was built. The robot must avoid them without losing localization or
falling behind schedule. Found objects are sent to the server as they are detected,
not in one batch at the end.

---

## What the Starter Kit provides

```python title="go2_scout.py"
from agrokit.go2 import Go2

go2 = Go2(sim=True)

for row in go2.field.rows:
    go2.nav.follow_row(row, speed=0.4)          # (1)!

    for det in go2.vision.detect(model="agro_yolo"):
        if det.label in ("powdery_mildew", "leaf_rust"):
            go2.report.add_finding(det.label, go2.nav.pose, det.score)

go2.report.export("field_report.json")
```

1.  Under the hood Nav2 plans the trajectory, and the locomotion controller turns
    velocity commands into leg motion. The same call works on the real robot.

Available modules:

| Module | Purpose |
|---|---|
| `go2.nav` | Move to point, follow row, obstacle avoidance, current pose |
| `go2.vision` | Camera frames, run detector, map detection to coordinates |
| `go2.map` | Build and load map, field row layout |
| `go2.report` | Accumulate findings and export JSON report |

Full description — in [Starter Kit](../starter-kit.md).

---

## Useful skills

Required: confident Python.
Helpful: ROS 2 and Nav2, OpenCV, training and fine-tuning YOLO-family detectors,
SLAM basics and point cloud work.
