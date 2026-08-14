# Go2 locomotion policy (organizers)

Organizers train a **velocity-tracking policy** that maps high-level
`cmd_vel` (vx, vy, vyaw) to Unitree `LowCmd` joint targets. Participants receive
the exported policy inside Starter Kit; they do not train locomotion themselves.

## Prerequisites

- NVIDIA GPU workstation or **DGX Spark**
- [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) 2.x with Unitree Go2 asset
- CycloneDDS **0.10.2** on deployment machine (same as robot firmware)

## Recommended workflow

1. **Scene** — flat terrain + optional roughness curriculum; match lab floor friction
   after measurement on NEWUU polygon.
2. **Observations** — base linear/angular velocity, projected gravity, joint pos/vel,
   last action; optional height scan later.
3. **Actions** — target joint positions or torques per Unitree low-level API.
4. **Reward** — track commanded vx/vy/vyaw, penalize energy, falls, and foot slip.
5. **Sim-to-real** — domain randomization on mass, friction, sensor delay; fine-tune
   on real Go2 only if platform is **Go2 EDU** with low-level access.

> **Go2 EDU vs Pro/Air:** low-level `LowCmd` policies apply only to **EDU**. On
> Pro/Air use Sport API (`Move`) — AgroKit `go2.nav` already falls back to
> SportClient when available.

## Export for AgroKit

After training, export the policy to ONNX or TorchScript and place it under
`models/go2_locomotion/`:

```
models/go2_locomotion/
├── policy.onnx          # preferred runtime
├── policy.pt            # optional TorchScript fallback
└── metadata.yaml        # obs/action dims, control frequency
```

Run the packaging helper (creates `metadata.yaml` template if missing):

```bash
python training/go2_locomotion/export_policy.py \
    --checkpoint path/to/policy.pt \
    --out models/go2_locomotion
```

Integration into `agrokit.go2.nav` will load this bundle in a future AgroKit
release once the EDU/Pro decision is finalized.

## References

- [Unitree RL Lab](https://github.com/unitreerobotics/unitree_rl_lab) — reference
  Isaac Lab environments for Unitree robots
- [Isaac Lab documentation](https://isaac-sim.github.io/IsaacLab/main/index.html)
- AgroKit issue tracker / org channel for policy format questions
