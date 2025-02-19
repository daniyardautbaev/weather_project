Weather Project

Это Django-приложение предоставляет REST API для получения информации о погоде в выбранных городах. Приложение использует базу данных PostgreSQL для хранения данных и интегрируется с внешним API OpenWeatherMap для получения актуальной информации о погоде.

Запуск проекта

Клонирование репозитория
git clone https://github.com/daniyardautbaev/weather_project.git
cd weather_project
Создание и активация виртуального окружения
python3 -m venv venv
source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
Установка зависимостей
pip install -r requirements.txt
Настройка переменных окружения
Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

SECRET_KEY=django-insecure--mtbh^&d+$^k7w=n2kf^_&i_qawc_b070&-rg2z$*kdri4y!9a
DB_NAME=weather_db
DB_USER=weather_user
DB_PASSWORD=Daniyar
DB_HOST=localhost
DB_PORT=5432
OPENWEATHER_API_KEY=0006ef2e7c518c7926e0ecb960a6bf7a
Применение миграций и создание суперпользователя
python manage.py migrate
python manage.py createsuperuser
Запуск сервера разработки
python manage.py runserver
Описание API

Регистрация пользователя
URL: /register/
Метод: POST
Описание: Регистрирует нового пользователя с указанием города.
Параметры:
username (string): Имя пользователя
password (string): Пароль
city (integer): ID города, выбранного пользователем
Пример запроса:
{
  "username": "user1",
  "password": "securepassword",
  "city": 1
}
Пример ответа:
{
  "message": "Регистрация прошла успешно"
}
Получение токена
URL: /api/token/
Метод: POST
Описание: Получение JWT токена для аутентификации.
Параметры:
username (string): Имя пользователя
password (string): Пароль
Пример запроса:
{
  "username": "user1",
  "password": "securepassword"
}
Пример ответа:
{
  "access": "access_token",
  "refresh": "refresh_token"
}
Получение погоды для города пользователя
URL: /weather/
Метод: GET
Описание: Возвращает информацию о погоде для города, указанного пользователем при регистрации.
Заголовки:
Authorization: Bearer access_token
Пример ответа:
{
  "city": {
    "id": 1,
    "name": "Almaty"
  },
  "temperature": 25.5,
  "description": "ясно",
  "updated_at": "2025-02-19T14:00:00Z"
}
Добавление нового города (только для менеджеров)
URL: /cities/add/
Метод: POST
Описание: Добавляет новый город в базу данных.
Заголовки:
Authorization: Bearer access_token
Параметры:
name (string): Название города
Пример запроса:
{
  "name": "Astana"
}
Пример ответа:
{
  "id": 2,
  "name": "Astana"
}
Список всех городов
URL: /cities/
Метод: GET
Описание: Возвращает список всех городов, доступных в базе данных.
Пример ответа:
[
  {
    "id": 1,
    "name": "Almaty"
  },
  {
    "id": 2,
    "name": "Astana"
  }
]
Профиль пользователя
URL: /user/profile/
Метод: GET
Описание: Возвращает информацию о текущем пользователе.
Заголовки:
Authorization: Bearer access_token