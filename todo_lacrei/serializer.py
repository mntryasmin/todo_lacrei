from rest_framework import serializers
from todo_lacrei.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'titulo', 'descricao', 'prioridade']