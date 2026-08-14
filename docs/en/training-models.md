# Training models

Instructions for the **organizing committee** and teams that fine-tune the detector
on their own dataset. Base `agro_yolo` weights ship in the Starter Kit; Go2
locomotion policy is prepared by organizers only.

Students who only improve the algorithm on top of ready-made weights need the
[Learning materials](learn.md#computer-vision) section.

---

## agro_yolo (YOLOv8)

### 1. Environment

On a GPU workstation or DGX Spark:

```bash
python -m venv .venv-train && source .venv-train/bin/activate
pip install -r training/requirements.txt
```

### 2. Dataset

Annotations in YOLO format. Folder structure and classes — in
[`training/datasets/README.md`](https://github.com/NewUU-engineering/unitree-contest/blob/main/training/datasets/README.md).

Briefly:

```
training/datasets/agro/
├── images/train, images/val
└── labels/train, labels/val   # .txt with the same name as the image
```

Classes: `powdery_mildew`, `leaf_rust`, `healthy_leaf`, `ripe_apple`,
`unripe_apple`, `ripe_tomato`, `defect_fruit`.

Photos are taken **in the NEWUU laboratory** with artificial fruit and plant
mock-ups.

### 3. Training

```bash
python training/agro_yolo/train.py \
    --epochs 100 \
    --batch 16 \
    --device cuda:0
```

The script saves the best weights to `models/agro_yolo.pt`.

Parameters:

| Flag | Default | Description |
|------|--------------|----------|
| `--data` | `training/agro_yolo/dataset.yaml` | dataset config |
| `--model` | `yolov8n.pt` | base model (n/s/m) |
| `--epochs` | `100` | number of epochs |
| `--export-dir` | `models/` | where to put `agro_yolo.pt` |

### 4. Validation

```bash
python training/agro_yolo/validate.py
python training/agro_yolo/predict.py training/datasets/agro/images/val
```

### 5. Using in AgroKit

```bash
export AGRO_MODELS_DIR=/path/to/models
python examples/go2_scout.py
```

In Docker:

```bash
docker run --rm -it \
    -v "$PWD/models:/workspace/models" \
    -v "$PWD/solution:/workspace/solution" \
    ghcr.io/newuu-engineering/agrokit:latest \
    python3 /workspace/examples/go2_scout.py
```

`go2.vision.detect(model="agro_yolo")` and `g1.vision.detect(...)` automatically
load `agro_yolo.pt` if the file exists. Without weights — a deterministic demo set
(useful for CI and mock mode).

---

## Go2 locomotion policy (organizers only)

Participants **do not train** walking. The organizing committee prepares the
`cmd_vel` → `LowCmd` policy in Isaac Lab and packages it for `go2.nav`.

Detailed checklist:

- [`training/go2_locomotion/README.md`](https://github.com/NewUU-engineering/unitree-contest/blob/main/training/go2_locomotion/README.md)

Export:

```bash
python training/go2_locomotion/export_policy.py \
    --checkpoint path/to/policy.pt \
    --out models/go2_locomotion
```

AgroKit integration — after finalizing Go2 hardware configuration (EDU vs Pro/Air).

---

## Where the code lives

| Repository path | Purpose |
|--------------------|------------|
| `training/agro_yolo/train.py` | YOLO training |
| `training/agro_yolo/validate.py` | val metrics |
| `training/agro_yolo/predict.py` | visual check |
| `training/go2_locomotion/` | Go2 policy |
| `models/` | ready weights (not in git) |

Full description — [`training/README.md`](https://github.com/NewUU-engineering/unitree-contest/blob/main/training/README.md).
