---
title: AgroTech Robotics Challenge
hide:
  - navigation
---

# AgroTech Robotics Challenge

**A national robotics and artificial intelligence competition on
Unitree Go2 and Unitree G1 platforms.**
{ .lead }

Participants build algorithms for agro-monitoring and crop sorting:
first in a simulator on their own laptop, then on robots in the
NEWUU laboratory. The competition is organized by the New Uzbekistan University
Engineering School.

[Quick start](quickstart.md){ .md-button .md-button--primary }
[Learning materials](learn.md){ .md-button }
[Registration](registration.md){ .md-button }

[Russian version :material-translate:](/){ .md-button }

---

## What awaits you

<div class="grid cards" markdown>

-   :material-dog:{ .lg .middle } **Track 1 — Autonomous scout**

    ---

    The quadruped **Unitree Go2** moves through crop rows, finds diseased
    “plants” and ripe fruit, builds a map, and prepares a report.

    [:octicons-arrow-right-24: Navigation, SLAM, computer vision](tracks/go2.md)

-   :material-robot-industrial:{ .lg .middle } **Track 2 — Agro sorter**

    ---

    The humanoid **Unitree G1** with anthropomorphic hands recognizes artificial
    fruit, grasps them with a pinch or power grip, and sorts them into quality trays.

    [:octicons-arrow-right-24: Manipulation, grasp, teleoperation](tracks/g1.md)

-   :material-stairs-up:{ .lg .middle } **Three stages from simple to complex**

    ---

    The qualifier runs entirely in simulation; the semifinal and final take place
    on real robots in the NEWUU laboratory, with teleoperation in the final.

    [:octicons-arrow-right-24: Season format](stages.md)

-   :material-package-variant-closed:{ .lg .middle } **Ready-made Starter Kit**

    ---

    A Python framework, a container with the full environment, and pretrained models.
    You write the algorithm, not drivers and build scripts.

    [:octicons-arrow-right-24: What's in the kit](starter-kit.md)

</div>

---

## Why agriculture

Agriculture is a domain where autonomous robots deliver immediate value: row
patrols, early plant disease diagnosis, harvest collection and sorting.
Competition tasks are built around **practical agro scenarios**, not abstract
test fields, so team solutions have value beyond the contest.

!!! info "Where the competition takes place"

    All onsite stages are held **in the NEWUU robotics laboratory** on the
    university campus. Field trips with robots to farms, orchards, or greenhouses
    **are not planned**. The arena uses artificial beds, plant mock-ups, and
    **artificial fruit** — a teaching setup for agro tasks in controlled
    conditions, not work with live crops.

## Entry barrier is intentionally low

!!! tip "No robot or GPU required to start"

    The first stage runs entirely in the simulator. A laptop with Docker is
    enough — Linux, Windows, and macOS are supported, including Apple Silicon
    machines. A discrete GPU is not required: the simulator runs on the CPU and
    opens directly in the browser.

Organizers provide a ready-made framework, an environment container, and basic
examples for both tracks that work out of the box. The participant's job is to
improve the algorithm, not spend two weeks fighting dependency installation.

## Sim-to-real without rewriting code

The key engineering decision of the competition: the simulator and the real
robot exchange **the same messages** over a shared DDS bus. The difference between
running on a laptop and in the NEWUU laboratory comes down to two connection
parameters.

=== "Simulation"

    ```python
    robot = Go2(sim=True)   # domain_id = 1, interface "lo"
    ```

=== "Real robot"

    ```python
    robot = Go2(sim=False, iface="enp3s0")   # domain_id = 0
    ```

Code debugged in simulation transfers to hardware without logic changes. Details
and the full list of pinned versions are in the [Stack](stack.md) section.

## Next steps

- [x] Competition concept and technology stack published
- [x] Draft [rules](rules.md) published
- [x] [Registration](registration.md) and [learning materials](learn.md) pages
- [ ] Rules, calendar, and scoring weights approved
- [ ] Replace Google Form placeholder in `docs/en/registration.md`
- [ ] Starter Kit release and team registration opening
- [ ] Qualifier stage start

!!! info "Dates to be confirmed"

    The season calendar will be published on this site together with the rules.
    To receive the Starter Kit and start date first, contact the organizers:
    [robotics@newuu.uz](mailto:robotics@newuu.uz?subject=AgroTech%20Robotics%20Challenge).
