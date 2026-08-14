# Competition stages

The season consists of three stages, arranged from simple to complex. Each
subsequent stage adds one fundamentally new source of difficulty: first the
algorithm, then physical reality, then human interaction.

Both [tracks](tracks/index.md) run all three stages in parallel and are scored
separately.

---

## Stage 1 — Qualifier

**Format:** online, simulation  ·  **Equipment:** participant's laptop

Teams develop algorithms in the provided container. No robot or laboratory access
is required at this stage.

The solution is submitted as a repository and run by the judging script on
identical scenes with a fixed random seed for all teams. This makes the result
reproducible: the team gets a stable score, not “got lucky on one run”.

!!! note "What is evaluated"

    Algorithm performance in clean conditions: correct navigation or grasping,
    detection quality, no falls or hangs, readable code.

**Stage stack:** MuJoCo, ROS 2 Humble, Docker, YOLO, OpenCV.
Optionally — Isaac Sim for teams with an NVIDIA GPU machine.

---

## Stage 2 — Semifinal

**Format:** onsite, NEWUU laboratory  ·  **Equipment:** real Unitree Go2 and G1

Teams that pass the qualifier transfer algorithms to physical robots in the
**training arena on the university campus**. Field trips to farms, orchards, or
greenhouses are not planned: the agro-monitoring scenario is reproduced in
controlled conditions — artificial beds, plant mock-ups, and artificial fruit
instead of live crops.

Thanks to the shared DDS bus, code logic stays the same — only connection
parameters change.

The main engineering challenge of this stage is the gap between model and reality:

- noise and latency of real sensors instead of ideal simulator data;
- laboratory lighting, glare on plastic and lacquered props;
- paw grip on the arena floor covering and slip;
- mass and friction of artificial objects that do not match the grasp model.

This is what separates a working robot from a polished demo, so the stage
includes time for calibration and test runs.

!!! warning "Hardware safety rules"

    Switching to the real DDS domain is performed only in the NEWUU laboratory and
    only under judge supervision. See
    [Stack: safety rules](stack.md#safety-rules).

---

## Stage 3 — Final

**Format:** public show on the NEWUU campus  ·  **Equipment:** robots, Teleoperation Kit

The final combines full autonomy with human control. The scenario adds dynamic
conditions in the same laboratory zone: obstacles appear during task execution,
time is limited, and results are sent to a central server in real time.

A separate block of the final is teleoperation. Teams use Teleoperation Kit
gloves to record demonstration datasets for grasp policy learning
(learning from demonstration) or to adjust robot actions on the fly where
autonomy falls short.

The final is held publicly, with jury scoring.

---

## Summary

| Stage | Location | What the team needs | Key difficulty |
|---|---|---|---|
| 1. Qualifier | Online, simulator | Laptop with Docker | Algorithm |
| 2. Semifinal | NEWUU laboratory | Onsite presence | Physical reality |
| 3. Final | NEWUU campus | Onsite presence | Dynamics and human in the loop |

!!! info "Dates"

    The season calendar is published together with the approved edition of the rules.
    Follow updates on this site.

The procedure for each stage, solution requirements, and robot safety rules are
defined in the [Rules](rules.md).
