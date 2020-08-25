from django.contrib import admin

from .models import MetodPage

@admin.register(MetodPage)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10
    
