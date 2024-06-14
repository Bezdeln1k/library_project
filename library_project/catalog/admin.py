# Настроим административный интерфейс для моделей Book и BorrowedBook в Django

from django.contrib import admin
from .models import Book, BorrowedBook
from django import forms
from accounts.models import UserProfile

def make_available(modeladmin, request, queryset):
    queryset.update(is_available=True)

make_available.short_description = "Отметить выбранные книги как «В наличии»"

def make_unavailable(modeladmin, request, queryset):
    queryset.update(is_available=False)
                
make_unavailable.short_description = "Убрать отметку «В наличии»"

def make_returned(modeladmin, request, queryset):
    queryset.update(is_returned=True)

make_returned.short_description = "Отметить как «Возвращенные»"

class BorrowedBookAdminForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = '__all__'
        widgets = {
            # 'borrower': forms.Select(attrs={'size': '20'}), 
            'borrower_info': forms.TextInput(attrs={'size': '20'}), 
            'reader_card_display': forms.TextInput(attrs={'size': '20'}),
            'borrowed_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'})
        }

class BookAdmin(admin.ModelAdmin):
    actions = [make_available, make_unavailable]
    list_display = ('title', 'author', 'inventory_number', 'isbn', 'publication_year', 'is_available')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

class BorrowedBookAdmin(admin.ModelAdmin):
    form = BorrowedBookAdminForm
    actions = [make_returned]
    list_display = ('book', 'borrower', 'borrower_info', 'reader_card_display', 'borrowed_date', 'return_date', 'renewal_count', 'is_returned')
    list_filter = ('is_returned', 'return_date')
    search_fields = ('book__title', 'borrower__username', 'borrower__first_name', 'borrower__last_name', 'borrower__profile__reader_card')

    def borrower_info(self, obj):
        return f"{obj.borrower.first_name} {obj.borrower.last_name}"
    borrower_info.short_description = 'Имя и фамилия'
    borrower_info.admin_order_field = 'borrower__first_name'  # Добавляем сортировку по имени

    def reader_card_display(self, obj):
        return obj.borrower.profile.reader_card
    reader_card_display.short_description = 'Номер чит. билета'
    reader_card_display.admin_order_field = 'borrower__profile__reader_card'  # Добавляем сортировку по номеру читательского билета

    def borrower_display(self, obj):
        profile = UserProfile.objects.get(user=obj.borrower)
        return f"{obj.borrower.username} ({profile.user.first_name} {profile.user.last_name} - {profile.reader_card})"
    borrower_display.short_description = "Читатель"


admin.site.register(Book, BookAdmin)
admin.site.register(BorrowedBook, BorrowedBookAdmin)

# Эти настройки администратора позволяют управлять каталогом книг и выданными книгами в админ-панели Django.
# `list_display` настраивает колонки, которые будут отображаться в списке объектов модели.
# `list_filter` и `search_fields` добавляют возможности фильтрации и поиска по указанным полям.