from django.contrib import admin
from .models import MathPage

@admin.register(MathPage)
class MathAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'slug')
    search_fields = ('title', 'theme')
    prepopulated_fields = {'slug': ('theme',)}
    list_filter = ('theme', )
    autocomplete_fields = ['theme']
    list_per_page = 10
