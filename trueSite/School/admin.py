from django.contrib import admin
from .models import SchoolPage

@admin.register(SchoolPage)
class SchoolAdmin(admin.ModelAdmin):
    list_dispaly = ['title', 'theme', 'slug']
    search_fields = ['title', 'theme']
    list_per_page = 10
    list_filter = ['theme']

# Register your models here.
