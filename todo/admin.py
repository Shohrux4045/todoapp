from django.contrib import admin
from .models import Todo,Category

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created')
    list_filter = ('completed', 'created')
    search_fields = ('title', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)

admin.site.register(Todo, TaskAdmin)
admin.site.register(Category, CategoryAdmin)