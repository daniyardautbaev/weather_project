from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, City

class CustomUserCreationForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'city']  # Добавьте password1 и password2