# Создадим формы для регистрации, входа в систему и запроса на продление книги

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import BorrowedBook
from .models import UserProfile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, 
        required=True, 
        label='Логин:', 
        help_text='В качестве логина укажите идентификатор (номер) читательского билета регистрируемого читателя',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=254, 
        label='Электронная почта:',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        label='Имя:',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        label='Фамилия:',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'id_phone',
            'type': 'tel',
            'pattern': r'\+7[0-9]{3}[0-9]{3}[0-9]{4}',
            'placeholder': '+71234567890'}),
        max_length=15, 
        required=True, 
        label='Телефон:')
    address = forms.CharField(
        max_length=255, 
        required=True, 
        label='Адрес проживания (населенный пункт, улица, дом, кв.):',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    reader_card = forms.IntegerField(
        required=True, 
        label='Номер читательского билета:',
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Пароль:',
        help_text='В качестве пароля укажите фамилию читателя русскими буквами в нижнем регистре',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password],
        strip=False
    )
    password2 = forms.CharField(
        label='Подтверждение пароля:',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Введите тот же пароль еще раз для подтверждения',
        strip=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','phone', 'address', 'reader_card', 'password1', 'password2')

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError('Пароль должен содержать минимум 8 символов.')
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                reader_card=self.cleaned_data['reader_card']
            )
        return user


class RenewBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = []

# `SignUpForm` расширяет стандартную форму создания пользователя `UserCreationForm` в Django, добавляя поле email.
# `RenewBookForm` используется для обновления статуса запроса на продление книги. 
# Эти формы будут использоваться в представлениях для регистрации пользователей и подачи запросов на продление.
