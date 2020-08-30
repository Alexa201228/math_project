from django.contrib import admin

from .models import StudentsWorks

@admin.register(StudentsWorks)
class WorksAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ('title',)
    list_per_page = 10

