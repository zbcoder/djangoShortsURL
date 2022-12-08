from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль должен быть больше 8 символов и не должен быть простым',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

