# Technology stack

The competition stack follows one idea: **code written in the simulator must run
on the real robot without changes**. Everything else follows from that.

---

## Architecture

The linking layer is the DDS bus. The simulator and the real robot are equal
participants in one network and exchange identical messages, so upper layers do
not know what they are talking to.

<div class="stack" markdown>

<div class="stack__layer" markdown>
**Participant code** — `Python 3.10`
{ .stack__title }

Navigation, detection, grasp planning logic
</div>

<div class="stack__layer" markdown>
**AgroKit** — high-level API
{ .stack__title }

`go2.nav` · `go2.vision` · `g1.arm` · `g1.hand` · grasp presets · reports
</div>

<div class="stack__layer" markdown>
**ROS 2 Humble** · **Unitree SDK2**
{ .stack__title }

Nav2 · tf2 · rosbag · `unitree_sdk2_python`
</div>

<div class="stack__layer stack__layer--bus" markdown>
**CycloneDDS 0.10.2** — shared bus
{ .stack__title }

The same messages for simulator and robot
</div>

<div class="stack__targets" markdown>

<div class="stack__target" markdown>
**MuJoCo · Isaac Sim**
{ .stack__title }

stage 1
</div>

<div class="stack__target" markdown>
**Unitree Go2 · G1**
{ .stack__title }

stages 2–3
</div>

</div>

</div>

**Participant layer** — your algorithm in Python.

**AgroKit** — organizers' framework: wrappers `go2.nav`, `go2.vision`,
`g1.arm`, `g1.hand`, grasp presets, report generation, and telemetry.

**ROS 2 and Unitree SDK2** — working tools: route planning via Nav2, coordinate
transforms via tf2, run recording in rosbag for judging, low-level robot access
via SDK.

**CycloneDDS** — shared transport for everything above.

---

## Pinned versions

| Component | Version | Why |
|---|---|---|
| CycloneDDS | `0.10.2` | Matches Unitree robot firmware |
| ROS 2 | `Humble` | Unitree recommended distribution, shipped in the container |
| Python | `3.10` | Upper bound supported by `unitree_sdk2_python` |
| MuJoCo | current release | Base simulator for stage 1 |
| Isaac Sim / Isaac Lab | `6.0+` | Optional, on x86 machines with NVIDIA GPU |
| Docker image | `linux/amd64`, `linux/arm64` | Support for regular PCs and Apple Silicon |

!!! danger "Do not change the CycloneDDS version"

    It must match robot firmware. If you replace it with a newer version,
    simulation will keep working, but hardware communication in the laboratory will
    simply fail — and you will find out at the worst moment.

---

## Safety rules

Simulation and real robots are separated into different DDS domains. This is not
formality: separation physically prevents a debug script from the simulator from
moving a real robot in the next room.

| Mode | `domain_id` | Network interface |
|---|---|---|
| Simulation | `1` | `lo` (loopback) |
| Real robot | `0` | physical, e.g. `enp3s0` |

!!! warning "Switching to domain 0"

    Performed only in the NEWUU laboratory and only under judge supervision. In code
    this is an explicit flag, not the default:

    ```python
    robot = Go2(sim=False, iface="enp3s0")
    ```

### Different message types across platforms

Go2 uses IDL `unitree_go`, G1 uses `unitree_hg`. An example copied from one robot
to another will run and may not even raise an error, but data will silently not
match. AgroKit selects the correct type automatically, but when working with the
SDK directly you need to keep this in mind.

---

## Where things run

The competition is designed for three classes of machines, each with its own role.

=== "Participant laptop"

    **Stage 1.** MuJoCo simulator, ROS 2, and participant code in one container.
    No GPU required; graphics are served to the browser. Linux, Windows, and macOS
    are supported, including Apple Silicon.

=== "NVIDIA GPU workstation"

    **Optional.** Isaac Sim and Isaac Lab for teams that need more accurate physics,
    photorealistic rendering, or reinforcement learning policy training.
    Requires x86 and RTX.

=== "Organizer compute node"

    **Infrastructure.** Locomotion policy training, detector fine-tuning on the agro
    dataset, and model preparation for stage 3. Results of this work reach teams
    ready-made, inside the Starter Kit.

---

## Why MuJoCo, not Isaac Sim, for stage 1

Isaac Sim offers better visuals and accuracy but requires an NVIDIA GPU, which
excludes some teams already at the qualifier. MuJoCo runs on any CPU, starts in
seconds, and — most importantly — the official Unitree simulator build communicates
over the same DDS messages as the real robot. That is what enables code portability
without rewriting.

Isaac Sim remains available for teams with suitable hardware: participant code does
not change when switching simulators.
