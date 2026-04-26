# Mini API TODO

Минимальный REST API для управления задачами (TODO), построенный на **FastAPI**

## Структура проекта

```
src/
├── main.py                    # Точка входа приложения
├── controllers/
│   └── tasks/
│       └── route.py          # REST endpoints для задач
├── services/
│   └── tasks_service.py      # Бизнес-логика задач
├── repositories/
│   └── tasks/
│       ├── base_repository.py    # Абстракция репозитория с задачами
│       └── in_memory_repository.py  # Реализация в памяти
├── schemas/
│   ├── base.py               # Базовые Pydantic модели
│   ├── exceptions.py         # Кастомные исключения
│   └── tasks.py              # Схемы для задач
├── core/
│   ├── config.py             # Конфигурация приложения
│   ├── database.py           # In-memory база данных
│   └── logger.py             # Логирование
├── dependencies.py           # Dependency injection функции
└── middlewares.py            # HTTP middleware (логирование запросов)
```

## Быстрый старт

### Установка зависимостей

```bash
pip install -e .
```

### Запуск приложения

```bash
python src/main.py
```

Приложение будет доступно по адресу: **http://localhost:8000** (с дефолтными переменными окружения)

## Архитектура

### Слои приложения

1. **Controllers** — HTTP endpoints, валидация входных параметров
2. **Services** — бизнес-логика, обработка данных
3. **Repositories** — абстракция доступа к данным
4. **Core** — конфигурация, логирование, база данных

## Конфигурация

Переменные окружения находятся в `.env.template`:

```env
HOST=0.0.0.0
PORT=8000
RELOAD=true
```

Скопируйте `.env.template` в `.env` и отредактируйте при необходимости.
