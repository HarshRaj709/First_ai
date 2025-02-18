from django.contrib import admin
from .models import UserHistory

# Register your models here.
@admin.register(UserHistory)
class AdminUserHistory(admin.ModelAdmin):
    list_display = [field.name for field in UserHistory._meta.get_fields()]