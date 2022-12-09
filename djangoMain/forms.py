from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class CustomUserChangeForm(forms.ModelForm):
    
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы, кроме: @, /, _',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите Email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email')