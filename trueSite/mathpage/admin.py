from django.contrib import admin
from .models import MathPage, Themes

@admin.register(MathPage)
class MathAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('theme',)}
    list_filter = ('theme', )
    list_per_page = 10
    autocomplete_fields = ['theme']


@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    search_fields = ('theme','title')


