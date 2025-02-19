from django.contrib.auth.models import AbstractUser
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE, related_name="weather")
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city.name}: {self.temperature}°C, {self.description}"

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    city = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username