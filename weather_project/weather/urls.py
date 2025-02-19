from django.urls import path
from .views import WeatherAPIView, CityCreateView, UserProfileView, CityListView, RegisterAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather'),  # Получение погоды по городу пользователя
    path('cities/add/', CityCreateView.as_view(), name='add_city'),  # Добавление города (только для менеджеров)
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),  # Получение информации о пользователе
    path('cities/', CityListView.as_view(), name='city_list'),  # Список всех городов
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
