# Competition tracks

The competition runs in two parallel tracks, separated by platform. A team chooses
one track for the entire season and completes all three stages in it. Tracks are
scored separately; winners are determined in each.

<div class="grid cards" markdown>

-   :material-dog:{ .lg .middle } **Track 1 — Unitree Go2**

    ---

    **“Autonomous field and orchard scout”**

    The quadruped robot patrols rows (in simulation — an “orchard”, on the arena —
    artificial beds in the laboratory), finds plant diseases and ripe fruit, builds
    a map, and reports coordinates of findings.

    *Navigation · SLAM · computer vision · route planning*

    [:octicons-arrow-right-24: Go to track](go2.md)

-   :material-robot-industrial:{ .lg .middle } **Track 2 — Unitree G1**

    ---

    **“Smart agro sorter”**

    The humanoid with anthropomorphic hands recognizes **artificial** fruit, grasps
    them with a suitable grip, and sorts them into quality trays.

    *Manipulation · inverse kinematics · grasp · teleoperation*

    [:octicons-arrow-right-24: Go to track](g1.md)

</div>

## How to choose

Tracks require different engineering skills, and neither is “easy” — difficulty is
simply different in nature.

| | Track 1 — Go2 | Track 2 — G1 |
|---|---|---|
| Main challenge | Robot moves in space | Robot interacts with objects |
| Core task | Perception and path planning | Kinematics and object contact |
| Most code | Image processing, navigation | Trajectory planning, grasp |
| Cost of error | Robot deviates from route | Robot drops object |
| Good fit if your team has | CV and ROS 2 experience | Interest in manipulation and policy learning |

!!! tip "Not sure — start with Go2"

    The Go2 track offers a smoother learning curve: the basic example drives through
    a row immediately and can be improved gradually. In the G1 track, the first
    successful grasp takes a bit more preparation, but then opens work with
    learning from demonstrations.
