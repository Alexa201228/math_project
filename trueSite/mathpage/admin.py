from django.contrib import admin
from .models import MathPage
from dal import autocomplete
from django import forms

@admin.register(MathPage)
class MathAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', 'slug')
    prepopulated_fields = {'slug': ('theme',)}
    list_filter = ('theme', )
    list_per_page = 10
    search_fields = ['theme', 'title']
