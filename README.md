# 🌤 Weather Project

Это **Django-приложение**, которое предоставляет **REST API** для получения информации о погоде в выбранных городах.  
Приложение использует базу данных **PostgreSQL** для хранения данных и интегрируется с **OpenWeatherMap API** для получения актуальной информации о погоде.

## 🚀 Запуск проекта  

### 🔹 Клонирование репозитория
```bash
git clone https://github.com/daniyardautbaev/weather_project.git
cd weather_project
🔹 Создание и активация виртуального окружения
python3 -m venv venv
source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
🔹 Установка зависимостей
pip install -r requirements.txt
🔹 Настройка переменных окружения
Создай файл .env в корневой директории проекта и добавь туда:

SECRET_KEY=django-insecure--mthb^&d+$^K7w=n2kf^_&i_qawc_b070&-rg2z$*kdri4y!9a
DB_NAME=weather_db
DB_USER=weather_user
DB_PASSWORD=Daniyar
DB_HOST=localhost
DB_PORT=5432
OPENWEATHER_API_KEY=0006ef2e7c518c7926e0ecb960a6bf7a
🔹 Применение миграций и создание суперпользователя
python manage.py migrate
python manage.py createsuperuser
🔹 Запуск сервера разработки
python manage.py runserver
🌍 API Описание

🔹 Регистрация пользователя
URL: /register/
Метод: POST
Описание: Регистрирует нового пользователя с указанием города.
Параметры:
{
  "username": "user1",
  "password": "securepassword",
  "city": 1
}
Пример ответа:
{ "message": "Регистрация прошла успешно" }
🔹 Получение токена (JWT)
URL: /api/token/
Метод: POST
Описание: Получение JWT-токена для аутентификации.
Параметры:
{
  "username": "user1",
  "password": "securepassword"
}
Пример ответа:
{ "access": "access_token", "refresh": "refresh_token" }
🔹 Получение погоды
URL: /weather/
Метод: GET
Описание: Возвращает информацию о погоде для города, указанного пользователем при регистрации.
Заголовки: Authorization: Bearer access_token
Пример ответа:
{
  "city": { "id": 1, "name": "Almaty" },
  "temperature": 25.5,
  "description": "ясно",
  "updated_at": "2025-02-19T14:00:00Z"
}
🔹 Добавление нового города (только для менеджеров)
URL: /cities/add/
Метод: POST
Описание: Добавляет новый город в базу данных.
Заголовки: Authorization: Bearer access_token
Параметры:
{ "name": "Astana" }
Пример ответа:
{ "id": 2, "name": "Astana" }
🔹 Список городов
URL: /cities/
Метод: GET
Описание: Возвращает список всех городов, доступных в базе данных.
Пример ответа:
[
  { "id": 1, "name": "Almaty" },
  { "id": 2, "name": "Astana" }
]
🔹 Профиль пользователя
URL: /user/profile/
Метод: GET
Описание: Возвращает информацию о текущем пользователе.
Заголовки: Authorization: Bearer access_token
