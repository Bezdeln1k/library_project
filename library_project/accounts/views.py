from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, RenewBookForm
from catalog.models import BorrowedBook
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from .models import UserProfile

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('borrowed-books')
        else:
            return render(request, 'registration/login.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'registration/login.html')

# `SignUpView` - представление, использующее Django классы для создания новых пользователей.
# `login_view` - функция входа в систему.

@login_required
def borrowed_books_view(request):
    borrowed_books = BorrowedBook.objects.filter(borrower=request.user)
    all_borrowed_books = BorrowedBook.objects.filter(borrower=request.user).order_by('-borrowed_date')
    forms = {book.id: RenewBookForm(instance=book) for book in borrowed_books}
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'borrowed_books': borrowed_books,
        'all_borrowed_books': all_borrowed_books,
        'forms': forms,
        'user': request.user,
        'profile': user_profile
    }
    return render(request, 'borrowed_books.html', context)
    #return render(request, 'borrowed_books.html', {'all_borrowed_books': all_borrowed_books})
    #return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books, 'forms': forms})

@login_required
def renew_book_view(request, pk):
    book = BorrowedBook.objects.get(pk=pk)
    if request.method == 'POST':
        if book.can_renew():
            book.return_date += timedelta(days=7)
            book.renewal_count += 1  # Увеличиваем счетчик продлений
            book.save()
        else:
            messages.error(request, "Вы уже продлили срок возврата этой книги.")
    return redirect('borrowed-books')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Указываем, куда перенаправлять после выхода

    def dispatch(self, request, *args, **kwargs):
        """Разрешить выход из системы с использованием GET запроса."""
        if request.method.lower() == 'get':
            return self.logout(request)
        return super().dispatch(request, *args, **kwargs)

    def logout(self, request):
        """Выполнение выхода и перенаправление."""
        auth_logout(request)
        # Используем атрибут next_page для перенаправления
        return HttpResponseRedirect(self.next_page)




# `borrowed_books_view` - представление списка книг, взятых пользователем.
# `renew_book_view` - представление для подачи запроса на продление книги.