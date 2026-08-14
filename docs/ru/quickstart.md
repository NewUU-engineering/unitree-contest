# Быстрый старт

Путь от чистой машины до первого запущенного робота в симуляторе. Первая сборка
образа занимает 10–20 минут; последующие запуски — секунды.

---

## Что понадобится

- **Docker** — Linux, Windows или macOS, включая Apple Silicon.
- Около **8 ГБ** свободного места на диске.
- Браузер.

Видеокарта не нужна: симулятор работает на процессоре, графика отдаётся в
браузер через noVNC.

??? tip "Установка Docker"

    - **Windows и macOS** — [Docker Desktop](https://www.docker.com/products/docker-desktop/).
    - **Linux** — [официальная инструкция](https://docs.docker.com/engine/install/).

---

## Шаг 1. Собрать и запустить окружение

Из корня репозитория:

```bash
docker compose up --build
```

Или без compose:

```bash
docker build -t ghcr.io/newuu-engineering/agrokit:latest -f docker/Dockerfile .
docker run --rm -it -p 6080:6080 \
    -v "$PWD/solution:/workspace/solution" \
    ghcr.io/newuu-engineering/agrokit:latest
```

Контейнер поднимает:

- **unitree_mujoco** — симулятор Unitree (DDS domain 1, `lo`);
- **AgroKit** — Python-фреймворк и примеры;
- **noVNC** — рабочий стол в браузере на порту 6080.

Переменные окружения:

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `AGRO_ROBOT` | `go2` | Робот в симуляторе: `go2` или `g1` |
| `AGRO_START_SIM` | `1` | Запускать симулятор при старте |
| `AGRO_START_DESKTOP` | `1` | Запускать noVNC |

Пример для трека G1:

```bash
AGRO_ROBOT=g1 docker compose up --build
```

---

## Шаг 2. Открыть симулятор

Перейдите в браузере: **[http://localhost:6080](http://localhost:6080)**.

В окне noVNC должен появиться MuJoCo с загруженным роботом. Если окно пустое —
подождите 10–15 секунд после старта контейнера.

---

## Шаг 3. Запустить пример

В **новом терминале** на хосте:

```bash
docker compose exec agrokit bash
```

=== "Трек 1 — Go2"

    ```bash
    python3 /workspace/examples/go2_scout.py
    ```

    Скрипт пройдёт по межрядьям, найдёт болезни растений и сохранит
    `field_report.json` в текущей директории.

=== "Трек 2 — G1"

    ```bash
    python3 /workspace/examples/g1_sorting.py
    ```

    Демонстрация сортировки: распознавание, захват щипком, раскладка по лоткам.

---

## Шаг 4. Написать своё решение

```bash
cp examples/go2_scout.py solution/main.py
```

Папка `solution/` пробрасывается в `/workspace/solution` — редактируйте файл
на хосте, запускайте внутри контейнера.

---

## Шаг 5. Проверить себя судейским скриптом

```bash
agrokit-judge run /workspace/solution/main.py --scene orchard_qualifier
```

Скрипт выполняет решение в mock-режиме (без реального DDS) и выводит
предварительную разбивку баллов.

---

## Локальная разработка без Docker

Если нужно править AgroKit на хосте без Unitree SDK:

```bash
cd agrokit && pip install -e .
AGROKIT_MOCK=1 AGRO_SCENES_DIR=../scenes python ../examples/go2_scout.py
```

Полный симулятор и DDS доступны только внутри контейнера.

---

## Что дальше

- [Starter Kit](starter-kit.md) — описание API
- [Go2](tracks/go2.md) · [G1](tracks/g1.md) — задачи треков
- [FAQ](faq.md) — частые проблемы
