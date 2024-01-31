from django.contrib import admin
from .models import Todo

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created')
    list_filter = ('completed', 'created')
    search_fields = ('title', 'description')



admin.site.register(Todo, TaskAdmin)
