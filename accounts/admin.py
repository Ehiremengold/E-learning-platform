from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser']
    list_filter = ['email', 'username']
    readonly_fields = ['email', 'username', 'password']
    search_fields = ['email', 'username']


admin.site.register(Account, AccountAdmin)
