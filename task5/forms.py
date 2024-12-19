from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8)]
    )
    repeat_password = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8)]
    )
    age = forms.IntegerField(
        label='Введите свой возраст',
        validators=[MinValueValidator(18)]
    )

