http://51.250.110.184
# yamdb_final
# [![yamdb_workflow](https://github.com/ZakonGyka/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/ZakonGyka/yamdb_final/actions/workflows/yamdb_workflow.yml)
## Описание
Проект API для работы с приложением YAMDB.                
Документация к API: /redoc
## Технологии
- Python
- DRF
- PosgreSQL
- Docker
## Установка
- Склонировать репозиторий
- В файле docker-compose.yaml заменить в web image на build для создания локального образа
- Создать образ проекта: 
```Python
docker build -t <логин dockerhub>/<имя проекта> .
```
- Проверить, что:
    - образ проекта создается
    - контейнер создается
- Запустить сборку проекта:
```Python
docker-compose up
```
- Проверить, что проект запустился
- Создать файл .env  в директории infra/, указать следующие переменные:
  - DB_ENGINE=django.db.backends.postgresql
  - DB_NAME= # название БД\ POSTGRES_USER= # ваше имя пользователя
  - POSTGRES_PASSWORD= # пароль для доступа к БД
  - DB_HOST=db
  - DB_PORT=5432\
- Отправить созданный образ на docker.hub
- Заменить файле docker-compose.yaml заменить в web build на image для использования образа с репозитория docker.hub
- Настроить сервер (пример Linux/Ubunta):
  - обновите индекс пакетов: $ sudo apt update 
  - установите обновления: $ sudo apt upgrade -y
  - установите python, venv, git: $ sudo apt install python3-pip python3-venv git -y
  - Копируйте файл docker-compose.yaml на сервер
  - Копируйте файл nginx/default.conf на сервер
  - Клонируйте проект на сервер
- Запустите docker-compose up
- Примените миграции командой: $ sudo docker-compose exec web python manage.py migrate
- Создайте учетную запись администратора: $ sudo docker-compose exec web python manage.py createsuperuser
- Соберите статику командой: $ docker-compose exec web python manage.py collectstatic --no-input
## Авторы
- https://github.com/ZakonGyka
- https://github.com/spambox84

MIT License

Copyright (c) [2022] [Zakon_Gyka]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
