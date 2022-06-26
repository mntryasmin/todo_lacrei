from django.db import models

class Todo(models.Model) :
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=600, blank=True)
    prioridade = models.PositiveIntegerField(default=1)

    def __str__ (self):
        return self.titulo