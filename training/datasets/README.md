# Agro YOLO dataset layout

Organizers and teams store **local** datasets here. Image files are not committed
to git — only this README and label conventions.

## Folder structure

```
training/datasets/agro/
├── images/
│   ├── train/
│   ├── val/
│   └── test/          # optional
└── labels/
    ├── train/         # one .txt per image, same basename
    ├── val/
    └── test/
```

Each label file is YOLO format: `class_id x_center y_center width height` (normalized 0–1).

## Class IDs

| ID | Name | Track | Notes |
|----|------|-------|-------|
| 0 | `powdery_mildew` | Go2 | макет / лист с признаком болезни |
| 1 | `leaf_rust` | Go2 | |
| 2 | `healthy_leaf` | Go2 | negative class, снижает ложные срабатывания |
| 3 | `ripe_apple` | Go2, G1 | искусственный плод, grade A |
| 4 | `unripe_apple` | Go2, G1 | grade C |
| 5 | `ripe_tomato` | G1 | |
| 6 | `defect_fruit` | G1 | брак / дефект поверхности |

## Capture checklist (лаборатория NEWUU)

- несколько ракурсов: сверху, сбоку, на уровне камеры Go2;
- освещение: дневной белый, тёплый LED, боковой блик;
- фон: грядка, стол сортировки, пустой пол;
- 200+ изображений на класс для базовой модели, 500+ для соревновательного качества.

## Labeling tools

- [CVAT](https://www.cvat.ai/) — export YOLO 1.1
- [Label Studio](https://labelstud.io/)
- [Roboflow](https://roboflow.com/) — upload + export YOLOv8

After export, place files under `images/` and `labels/` as above, then run
`training/agro_yolo/train.py`.
