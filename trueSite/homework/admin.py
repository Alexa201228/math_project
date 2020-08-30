from django.contrib import admin

from .models import homework

@admin.register(homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme')
    search_fields = ('title', 'theme')
    list_per_page = 10