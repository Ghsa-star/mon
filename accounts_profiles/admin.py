from django.contrib import admin
from .models import AccountProfile

@admin.register(AccountProfile)
class AccountProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
