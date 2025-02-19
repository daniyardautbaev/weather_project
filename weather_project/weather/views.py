import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.utils.timezone import now
from django.conf import settings
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import City, WeatherData, CustomUser
from .serializers import WeatherDataSerializer, CitySerializer, UserSerializer
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            user.city = city
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Регистрация прошла успешно"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeatherAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_weather_from_api(self, city_name):
        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def get(self, request):
        user = request.user
        if not user.city:
            return Response({"error": "Город не указан у пользователя"}, status=400)

        city = user.city
        weather = WeatherData.objects.filter(city=city).first()
        if weather and (now() - weather.updated_at).seconds < 600:
            return Response(WeatherDataSerializer(weather).data)

        api_data = self.get_weather_from_api(city.name)
        if not api_data:
            return Response({"error": "Ошибка при запросе погоды"}, status=500)

        weather, _ = WeatherData.objects.update_or_create(
            city=city,
            defaults={
                "temperature": api_data["main"]["temp"],
                "description": api_data["weather"][0]["description"],
                "updated_at": now(),
            },
        )
        return Response(WeatherDataSerializer(weather).data)

class CityCreateView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'manager':
            return Response({"error": "Доступ запрещён, только менеджеры могут добавлять города"}, status=403)
        serializer.save()

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]