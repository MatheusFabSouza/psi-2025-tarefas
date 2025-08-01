from django.db import models

class Tarefa(models.Model):
    em_andamento = "em andamento"
    concluida    = "finalizada"
    pendente     = "pendente"

    STATUS_CHOICES = [
        (em_andamento, "em andamento"),
        (concluida,    "finalizada"),
        (pendente,     "pendente"),
    ]

    nome   = models.CharField("nome",   max_length=200)
    status = models.CharField("status", choices=STATUS_CHOICES, default=pendente)
    prazo  = models.DateField("prazo")

    def __str__(self):
        return self.nome
