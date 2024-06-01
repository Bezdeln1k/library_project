from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Дополнительная информация'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'first_name', 'last_name','reader_card_display', 'email', 'phone', 'address', 'is_active')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name','profile__reader_card', 'email', 'profile__phone', 'profile__address')

    def phone(self, obj):
        return obj.profile.phone

    def address(self, obj):
        return obj.profile.address

    def reader_card_display(self, obj):
        return obj.profile.reader_card
    reader_card_display.admin_order_field = 'profile__reader_card'  # Позволяет сортировку по полю reader_card
    reader_card_display.short_description = 'Номер чит. билета'

    # Настройка заголовков методов
    def get_queryset(self, request):
        # Оптимизация запроса с предварительной загрузкой профилей
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('profile')
        return queryset

admin.site.unregister(User)
admin.site.register(User, UserAdmin)