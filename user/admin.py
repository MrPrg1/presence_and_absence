from django.contrib import admin
from .models import BaseUser

@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName', 'name', 'lastName', 'age','phone_number', 'nationalCode', 'dateOfBirth', 'degree', 'evidence', 'citizenship', 'email']