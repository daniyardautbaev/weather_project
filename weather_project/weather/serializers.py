from rest_framework import serializers
from .models import WeatherData, City, CustomUser

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class WeatherDataSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = WeatherData
        fields = '__all__'

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    temperature = serializers.FloatField()
    description = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())

    class Meta:
        model = CustomUser
        fields = ['username', 'role', 'city']