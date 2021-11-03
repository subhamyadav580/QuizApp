from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from account.models import Account


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_teacher", "is_student")
    list_editable = ("is_teacher", "is_student",)

admin.site.register(Account, UserAdmin)