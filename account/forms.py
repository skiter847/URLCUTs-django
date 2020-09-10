from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
        labels = {
            "username": 'Имя пользователя',
        }

    def clean_password2(self) -> dict:
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')

        return cd


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользывателя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self) -> dict:
        cd = self.cleaned_data
        user = authenticate(request=self.request, username=cd['username'], password=cd['password'])
        if user is None:
            raise forms.ValidationError('Неверный логин или пароль')

        cd.update({'user': user})

        return cd
