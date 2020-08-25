from django.contrib import admin
from .models import MathPage, Theme

@admin.register(MathPage)
class MathAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'slug')
    prepopulated_fields = {'slug': ('theme',)}
    list_filter = ('theme', )
    list_per_page = 10
    autocomplete_fields = ['theme']

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    search_fields = ['thema']




