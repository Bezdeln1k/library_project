from django.urls import path
from .views import CustomLogoutView, SignUpView, login_view, borrowed_books_view, renew_book_view
from catalog.views import upload_xml

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # Указание имени маршрута
    path('login/', login_view, name='login'),
    path('borrowed-books/', borrowed_books_view, name='borrowed-books'),
    path('renew-book/<int:pk>/', renew_book_view, name='renew-book'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]