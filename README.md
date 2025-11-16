# API-сервис для вопросов и ответов — question_answer_app

## Тестовое задание на FastAPI с использованием PostgreSQL, SQLAlchemy, Alembic и Docker.
## Проект включает API для управления вопросами и ответами.

# Стек технологий
+ FastAPI
+ PostgreSQL (Docker)
+ SQLAlchemy 2.0
+ Alembic
+ Docker & Docker Compose
+ Pydantic v2

# 1) Клонирование репозитория:
```python
git clone https://github.com/Maksim-Borisov7/question_answer_app
```

# 2) переходим в папку командой:
```python 
cd question_answer_app 
```

# 3) Настройка переменных окружения
+ Создайте файл .env в корне проекта
+ Скопируйте содержимое папки .env.example в .env

# 4) Запуск проекта через Docker
```python 
docker compose up -d
```
# 5) После запуска контейнеров примените миграции Alembic:
```python 
docker exec -it question_answer_app alembic upgrade head
```
# 6) Запуск тестов - pytest внутри контейнера app:
```python 
docker exec -it question_answer_app pytest
```
# 7) После запуска приложение доступно по адресу:
http://localhost:8000/docs

# 8) Остановка контейнеров
```python 
docker compose down
```