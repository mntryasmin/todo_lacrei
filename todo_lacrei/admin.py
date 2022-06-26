from django.contrib import admin
from todo_lacrei.models import Todo

class Todo_admin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'prioridade',)
    list_display_links = ('id', 'titulo',)
    search_fields = ('titulo',)

admin.site.register(Todo, Todo_admin)