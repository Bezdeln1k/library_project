# Давайте напишем модели для приложения catalog в Django

from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    author = models.CharField(max_length=200, verbose_name='Автор')
    publication_year = models.IntegerField(verbose_name='Год публикации')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.title} - {self.author}, {self.publication_year}"

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Читатель')
    borrowed_date = models.DateField(auto_now_add=True, verbose_name='Дата заимствования')
    return_date = models.DateField(verbose_name='Дата возврата')
    # renewal_requested = models.BooleanField(default=False)
    renewal_count = models.IntegerField(default=0, verbose_name='Книга продлена (1-да, 0-нет)')  # Поле для отслеживания количества продлений
    is_returned = models.BooleanField(default=False, verbose_name='Возвращена')

    class Meta:
        verbose_name = 'Заимствованную книгу'
        verbose_name_plural = 'Заимствованные книги'
    
    def can_renew(self):
        return self.renewal_count < 1  # Разрешить продление, если оно было меньше 1 раза

    def __str__(self):
        return f"{self.book.title} - {self.borrower.username}. Вернуть до {self.return_date}"
    

# Эти модели обеспечивают основу для управления каталогом книг и их заимствованием.
# Модель `Book` содержит информацию о книгах в библиотеке.
# Модель `BorrowedBook` относится к записям о заимствовании книг читателями, включая статус запроса на продление.