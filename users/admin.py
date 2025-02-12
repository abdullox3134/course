from django.contrib import admin
from .models import CustomUser, Profile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'lastname', 'full_name', 'is_staff', 'is_superuser')  # 'full_name' qo'shildi
    search_fields = ('phone', 'name', 'lastname')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
