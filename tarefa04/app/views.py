from django.shortcuts import render
from datetime import date
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all().order_by('prazo')
    hoje    = date.today()
    context = {
        'tarefas': tarefas,
        'hoje': hoje,
    }
    return render(request, 'index.html', context)

