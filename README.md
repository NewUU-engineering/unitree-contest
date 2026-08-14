# AgroTech Robotics Challenge

Республиканское соревнование по робототехнике и искусственному интеллекту на
платформах **Unitree Go2** и **Unitree G1**. Организатор — инженерная школа
New Uzbekistan University.

**Сайт соревнования:** https://newuu-engineering.github.io/unitree-contest/

---

## О чём соревнование

Участники разрабатывают алгоритмы для агротехнических задач — мониторинга
рядов и сортировки урожая. Очные этапы проходят **в лаборатории NEWUU** с
искусственным реквизитом; выезды на поля не планируются. Сезон состоит из
трёх этапов: от симуляции на собственном ноутбуке до работы с реальными
роботами и телеоперации в финале.

| Трек | Платформа | Фокус |
|---|---|---|
| 1 — Автономный скаут полей и садов | Unitree Go2 | Навигация, SLAM, компьютерное зрение |
| 2 — Умный агро-сортировщик | Unitree G1 | Манипуляция, схват, телеоперация |

## Репозиторий

```
agrokit/                  # Python-фреймворк Starter Kit
examples/                 # рабочие примеры Go2 и G1
scenes/                   # YAML-сцены для судейства
docker/                   # Dockerfile и скрипты запуска
solution/                 # сюда кладёт решение команда (volume)
docs/                     # сайт документации (MkDocs)
```

## Docker — быстрый старт

```bash
docker compose up --build
```

Готовый образ (после push в `main`):

```bash
docker pull ghcr.io/newuu-engineering/agrokit:latest
docker run --rm -it -p 6080:6080 \
    -v "$PWD/solution:/workspace/solution" \
    ghcr.io/newuu-engineering/agrokit:latest
```

Подробнее — [docs/quickstart.md](docs/quickstart.md) и на сайте
[Быстрый старт](https://newuu-engineering.github.io/unitree-contest/quickstart/).

## Локальная разработка AgroKit (без DDS)

```bash
cd agrokit && pip install -e .
AGROKIT_MOCK=1 AGRO_SCENES_DIR=../scenes python ../examples/go2_scout.py
```

Полный симулятор Unitree доступен только в Docker-образе.

## Локальная сборка сайта

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-docs.txt

mkdocs serve          # http://127.0.0.1:8000 с горячей перезагрузкой
mkdocs build --strict # проверка сборки, как в CI
```

## Публикация

Сайт разворачивается автоматически при пуше в `main` через GitHub Actions
(`.github/workflows/docs.yml`): `mkdocs gh-deploy` собирает сайт и публикует его
в ветку `gh-pages`. В настройках репозитория должно быть выбрано
**Settings → Pages → Source: Deploy from a branch → `gh-pages` / (root)**.

На pull request тот же workflow выполняет только `mkdocs build --strict` —
проверяет сборку и битые ссылки, ничего не публикуя.

## Обратная связь

Вопросы по соревнованию — [robotics@newuu.uz](mailto:robotics@newuu.uz).
Правки в документацию принимаются пул-реквестами.

## Лицензия

[MIT](LICENSE)
