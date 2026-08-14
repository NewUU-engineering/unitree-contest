# Обучение моделей для AgroTech Robotics Challenge

Скрипты для **организаторов** и продвинутых команд, которые дообучают
`agro_yolo` под свой датасет. Политика локомоции Go2 — только для оргкомитета.

## Быстрый старт (agro_yolo)

```bash
python -m venv .venv-train && source .venv-train/bin/activate
pip install -r training/requirements.txt

# 1. Положить размеченный датасет (см. training/datasets/README.md)
# 2. Обучить
python training/agro_yolo/train.py --epochs 100 --device cuda:0

# 3. Проверить
python training/agro_yolo/validate.py

# 4. Посмотреть предсказания
python training/agro_yolo/predict.py training/datasets/agro/images/val
```

Веса попадают в `models/agro_yolo.pt`. AgroKit подхватывает их через
`AGRO_MODELS_DIR` (по умолчанию `/workspace/models` в Docker).

## Структура

| Путь | Назначение |
|------|------------|
| `training/agro_yolo/` | YOLOv8 train / val / predict |
| `training/datasets/` | Локальные датасеты (не в git) |
| `training/go2_locomotion/` | Экспорт политики Isaac Lab → AgroKit |
| `training/runs/` | Логи Ultralytics (gitignore) |
| `models/` | Готовые веса для Starter Kit |

## Docker

Обучение лучше запускать **на GPU-станции**, не в образе участника. После
обучения смонтируйте `models/` в контейнер:

```bash
docker run --rm -it \
    -v "$PWD/models:/workspace/models" \
    -v "$PWD/solution:/workspace/solution" \
    ghcr.io/newuu-engineering/agrokit:latest \
    python3 /workspace/examples/go2_scout.py
```

## Документация на сайте

- [Обучающие материалы](../docs/ru/learn.md) — с чего начать студентам
- [Обучение моделей](../docs/ru/training-models.md) — краткая инструкция на сайте
