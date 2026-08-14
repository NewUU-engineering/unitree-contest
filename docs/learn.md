# Обучающие материалы

Путь для студентов: от нуля до рабочего решения в AgroKit. Материалы
разделены по темам — проходите блоки по порядку или выборочно, если тема уже
знакома.

[Быстрый старт](quickstart.md){ .md-button .md-button--primary }
[Starter Kit](starter-kit.md){ .md-button }

---

## Маршрут на 4 недели

| Неделя | Цель | Действия |
|--------|------|----------|
| 1 | Окружение | Docker, `go2_scout.py` / `g1_sorting.py` в mock, чтение [Starter Kit](starter-kit.md) |
| 2 | Свой алгоритм | Код в `solution/`, фильтрация детекций, отчёт JSON, прогон `agrokit-judge` |
| 3 | Компьютерное зрение | Дообучение или fine-tune `agro_yolo`, см. [Обучение моделей](training-models.md) |
| 4 | Sim-to-real | Калибровка, тесты на полигоне NEWUU, подготовка к полуфиналу |

!!! tip "Mock-режим"

    Без робота и без GPU: `AGROKIT_MOCK=1 python examples/go2_scout.py` — все
    модули печатают действия в консоль, тесты проходят локально.

---

## AgroKit — с чем вы работаете

### Архитектура

```
solution/main.py          ← ваш код
    ↓
agrokit.go2 / agrokit.g1  ← высокоуровневый API
    ↓
Unitree SDK + DDS         ← связь с симулятором или роботом
```

Один и тот же код в симуляции и на железе — меняются только `sim=True/False`
и сетевой интерфейс. Подробнее: [Стек](stack.md#правила-безопасности).

### Модули по трекам

=== "Go2 — скаут"

    | Модуль | Задача |
    |--------|--------|
    | `go2.nav` | движение, `follow_row`, `goto` |
    | `go2.vision` | кадр, `detect("agro_yolo")` |
    | `go2.report` | находки → JSON |
    | `go2.field` | ряды из YAML-сцены |

    Пример: [`examples/go2_scout.py`](https://github.com/NewUU-engineering/unitree-contest/blob/main/examples/go2_scout.py)

=== "G1 — сортировщик"

    | Модуль | Задача |
    |--------|--------|
    | `g1.arm` | `move_to_point(x, y, z)` |
    | `g1.hand` | пресеты `PINCH`, `POWER_GRIP`, `OPEN` |
    | `g1.vision` | те же детекции, что у Go2 |
    | `g1.trays` | координаты лотков A / B / C |

    Пример: [`examples/g1_sorting.py`](https://github.com/NewUU-engineering/unitree-contest/blob/main/examples/g1_sorting.py)

### Судейский прогон

```bash
agrokit-judge run solution/main.py --scene orchard_qualifier
```

Сцены лежат в `scenes/*.yaml`. Зерно случайности фиксируется организаторами —
результат должен воспроизводиться.

### Репозиторий и Docker

- Клон: [github.com/NewUU-engineering/unitree-contest](https://github.com/NewUU-engineering/unitree-contest)
- Решение монтируется в `/workspace/solution`
- Образ: `ghcr.io/newuu-engineering/agrokit:latest`

---

## Python

Минимум для старта:

- функции, классы, `dataclass`;
- `pathlib`, работа с JSON;
- виртуальное окружение и `pip install -e agrokit`.

Полезные ресурсы:

- [Official Python Tutorial (RU)](https://docs.python.org/3/tutorial/index.html)
- [Real Python](https://realpython.com/) — статьи по темам
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)

---

## ROS 2 и навигация

Go2 использует паттерны ROS 2 (Nav2, `cmd_vel`), но в Starter Kit они уже
обёрнуты в `go2.nav`. Для углубления:

| Ресурс | Ссылка |
|--------|--------|
| ROS 2 Humble docs | [docs.ros.org/humble](https://docs.ros.org/en/humble/index.html) |
| Nav2 | [navigation.ros.org](https://navigation.ros.org/) |
| Unitree ROS2 (Go2) | [unitree_ros2](https://github.com/unitreerobotics/unitree_ros2) |

Видео:

- [ROS 2 — официальный канал Open Robotics](https://www.youtube.com/@OpenRoboticsOrg)
- [Programming with ROS 2 (The Construct)](https://www.youtube.com/playlist?list=PLl0b7nXGaLH8iX_3qZEpZf-sBBz0-Awnf)

---

## Компьютерное зрение

Задачи соревнования — детекция болезней и плодов через **YOLO**.

1. Понять формат `Detection` в AgroKit (`label`, `score`, `x`, `y`, `z`, `grade`).
2. Запустить demo: `go2.vision.detect("agro_yolo")` без весов.
3. Дообучить модель на своих снимках — [Обучение моделей](training-models.md).

| Ресурс | Ссылка |
|--------|--------|
| Ultralytics YOLOv8 docs | [docs.ultralytics.com](https://docs.ultralytics.com/) |
| OpenCV Python | [docs.opencv.org](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) |
| CVAT (разметка) | [cvat.ai](https://www.cvat.ai/) |

Видео:

- [Ultralytics — YOLOv8 official](https://www.youtube.com/watch?v=UN5H7rJ5BpE)
- [Train YOLOv8 on custom dataset](https://www.youtube.com/watch?v=wuZtUMEiKWY)

---

## Unitree и симуляция

| Ресурс | Ссылка |
|--------|--------|
| Unitree SDK2 Python | [unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python) |
| unitree_mujoco (сим) | [unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco) |
| Unitree RL Lab | [unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab) |
| Inspire Hand (G1) | см. [трек G1 — кисть](tracks/g1.md#управление-кистью) |

YouTube — официальный канал и обзоры платформ:

- [Unitree Robotics](https://www.youtube.com/@unitree-robotics)
- [Unitree Go2 — product overview](https://www.unitree.com/go2)

MuJoCo в нашем Docker открывается через **noVNC** на порту 6080 — см.
[Быстрый старт](quickstart.md).

---

## Манипуляция и G1

- Обратная кинематика — `g1.arm.move_to_point`; в v0.1 это интерполяция, не
  полноценный IK-сolver.
- Схват — только **позиционный**; подбирайте пресет и скорость под
  искусственные плоды на столе.

| Ресурс | Ссылка |
|--------|--------|
| LeRobot (imitation learning) | [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot) |
| Modern Robotics (теория) | [modernrobotics.northwestern.edu](http://modernrobotics.northwestern.edu/) |

Телеоперация на финале — **Teleoperation Kit** Unitree; материалы появятся
ближе к третьему этапу.

---

## Видео от NEWUU *(скоро)*

Оргкомитет готовит короткие ролики:

- [ ] Обзор соревнования и треков
- [ ] Docker + первый запуск за 10 минут
- [ ] Разбор `go2_scout.py` построчно
- [ ] Разбор `g1_sorting.py` и пресетов кисти
- [ ] Прогон `agrokit-judge` и разбор отчёта

Ссылки будут добавлены на эту страницу после публикации на
[YouTube-канале NEWUU](https://www.youtube.com/@newuu-robotics) *(замените на
фактический канал)*.

---

## Что читать дальше

1. [Выбрать трек](tracks/index.md)
2. [Этапы соревнования](stages.md)
3. [Оценка решений](scoring.md) — что судьи смотрят в коде и на прогоне
4. [FAQ](faq.md)
5. [Регистрация](registration.md)

Вопросы: [robotics@newuu.uz](mailto:robotics@newuu.uz)
