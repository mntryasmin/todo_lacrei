from rest_framework import viewsets
from todo_lacrei.models import Todo
from todo_lacrei.serializer import TodoSerializer
from rest_framework.filters import OrderingFilter

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['prioridade']