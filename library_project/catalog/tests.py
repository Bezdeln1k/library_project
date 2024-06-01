# Напишем простые тесты для моделей Book и BorrowedBook в Django

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book, BorrowedBook
from datetime import date

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Test Book", author="Author Name", publication_year=2020)

    def test_string_representation(self):
        self.assertEqual(str(self.book), "Test Book by Author Name, 2020")

class BorrowedBookModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.book = Book.objects.create(title="Test Book", author="Author Name", publication_year=2020)
        self.borrowed_book = BorrowedBook.objects.create(
            book=self.book,
            borrower=self.user,
            return_date=date.today(),
            renewal_requested=False
        )

    def test_string_representation(self):
        expected_string = f"{self.book.title} borrowed by {self.user.username} due on {self.borrowed_book.return_date}"
        self.assertEqual(str(self.borrowed_book), expected_string)

    def test_renewal_status(self):
        self.assertFalse(self.borrowed_book.renewal_requested)

# Эти тесты проверяют правильность строкового представления моделей и корректность значений полей.
# В тестах для BorrowedBook мы также проверяем начальное состояние поля renewal_requested.
