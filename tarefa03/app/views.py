from django.shortcuts import render

def index(request):
    return render(request, 'usuarios.html')

def usuarios(request):
    lista_usuarios = [
        {"nome": "Matheus", "matricula": "1234", "idade": 12, "cidade": "spp"},
        {"nome": "Joo", "matricula": "1672", "idade": 12, "cidade": "spp"},
        {"nome": "Maia", "matricula": "1673", "idade": 12, "cidade": "spp"},
        {"nome": "Anna", "matricula": "1674", "idade": 12, "cidade": "spp"},
        {"nome": "Pedro", "matricula": "1675", "idade": 12, "cidade": "spp"},
    ]

    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "usuarios.html", context)
