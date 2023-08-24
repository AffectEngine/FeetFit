from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'address']
	list_filter = ['date_of_birth']
	search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address']
