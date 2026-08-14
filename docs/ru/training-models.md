# Обучение моделей

Инструкция для **оргкомитета** и команд, которые дообучают детектор под свой
датасет. Базовые веса `agro_yolo` поставляются в Starter Kit; политика
локомoции Go2 готовится только организаторами.

Студентам, которые только улучшают алгоритм поверх готовых весов, достаточно
раздела [Обучающие материалы](learn.md#компьютерное-зрение).

---

## agro_yolo (YOLOv8)

### 1. Окружение

На GPU-станции или DGX Spark:

```bash
python -m venv .venv-train && source .venv-train/bin/activate
pip install -r training/requirements.txt
```

### 2. Датасет

Разметка в формате YOLO. Структура папок и классы — в
[`training/datasets/README.md`](https://github.com/NewUU-engineering/unitree-contest/blob/main/training/datasets/README.md).

Кратко:

```
training/datasets/agro/
├── images/train, images/val
└── labels/train, labels/val   # .txt с тем же именем, что у изображения
```

Классы: `powdery_mildew`, `leaf_rust`, `healthy_leaf`, `ripe_apple`,
`unripe_apple`, `ripe_tomato`, `defect_fruit`.

Снимки — **в лаборатории NEWUU** с искусственными плодами и макетами растений.

### 3. Обучение

```bash
python training/agro_yolo/train.py \
    --epochs 100 \
    --batch 16 \
    --device cuda:0
```

Скрипт сохраняет лучшие веса в `models/agro_yolo.pt`.

Параметры:

| Флаг | По умолчанию | Описание |
|------|--------------|----------|
| `--data` | `training/agro_yolo/dataset.yaml` | конфиг датасета |
| `--model` | `yolov8n.pt` | базовая модель (n/s/m) |
| `--epochs` | `100` | число эпох |
| `--export-dir` | `models/` | куда положить `agro_yolo.pt` |

### 4. Проверка

```bash
python training/agro_yolo/validate.py
python training/agro_yolo/predict.py training/datasets/agro/images/val
```

### 5. Использование в AgroKit

```bash
export AGRO_MODELS_DIR=/path/to/models
python examples/go2_scout.py
```

В Docker:

```bash
docker run --rm -it \
    -v "$PWD/models:/workspace/models" \
    -v "$PWD/solution:/workspace/solution" \
    ghcr.io/newuu-engineering/agrokit:latest \
    python3 /workspace/examples/go2_scout.py
```

`go2.vision.detect(model="agro_yolo")` и `g1.vision.detect(...)` автоматически
загружают `agro_yolo.pt`, если файл есть. Без весов — детерминированный demo-набор
(удобно для CI и mock-режима).

---

## Политика локомоции Go2 (только организаторы)

Участники **не обучают** ходьбу. Оргкомитет готовит политику `cmd_vel` →
`LowCmd` в Isaac Lab и упаковывает её для `go2.nav`.

Подробный чеклист:

- [`training/go2_locomotion/README.md`](https://github.com/NewUU-engineering/unitree-contest/blob/main/training/go2_locomotion/README.md)

Экспорт:

```bash
python training/go2_locomotion/export_policy.py \
    --checkpoint path/to/policy.pt \
    --out models/go2_locomotion
```

Интеграция в AgroKit — после финализации комплектации Go2 (EDU vs Pro/Air).

---

## Где лежит код

| Путь в репозитории | Назначение |
|--------------------|------------|
| `training/agro_yolo/train.py` | обучение YOLO |
| `training/agro_yolo/validate.py` | метрики на val |
| `training/agro_yolo/predict.py` | визуальная проверка |
| `training/go2_locomotion/` | политика Go2 |
| `models/` | готовые веса (не в git) |

Полное описание — [`training/README.md`](https://github.com/NewUU-engineering/unitree-contest/blob/main/training/README.md).
