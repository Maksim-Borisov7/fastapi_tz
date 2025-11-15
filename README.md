# API-сервис для вопросов и ответов: fastapi_tz
# Тестовое задание на fastapi с использованием postgresql
# Этапы запуска проекта
# 1) Клонируем репозиторий с проектом: 
#  git clone https://github.com/Maksim-Borisov7/fastapi_tz
#  И переходим в папку: cd fastapi_tz
# 2) Запуск проекта: Создайте файл .env
#  Скопируйте содержимое .env.example в .env
#  docker compose up -d
# 3) В браузере ссылка на swagger: http://localhost:5050/docs
# В ручке "/questions/{id}/answers/" есть поле user_id, 
# 4) Проверка работы PostgreSQL: psql -h localhost -p 5433 -U <USER> -d <DB_NAME>
# 5) Остановка проекта: docker compose down
