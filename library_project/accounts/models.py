from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    reader_card = models.IntegerField(blank=True, null=True, verbose_name='Номер читательского билета')

    class Meta:
        verbose_name = ('Дополнительные данные читателя')
        verbose_name_plural = ('Читатели')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Чит.билет № {self.reader_card}"
