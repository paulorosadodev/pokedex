from django.shortcuts import render, redirect
from django.views import View
from .models import Pokemon

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class AddView(View):
    def get(self, request): 
        return render(request, 'adicionar.html')
    
    def post(self, request):
        name = request.POST.get("nome")
        tipo1 = request.POST.get("tipo1")
        tipo2 = request.POST.get("tipo2")
        hp = request.POST.get("hp")
        altura = request.POST.get("altura")
        peso = request.POST.get("peso")
        urlImagem = request.POST.get("imagem")
        descricao = request.POST.get("descricao")

        pokemon = Pokemon(
            nome=name,
            tipo1 = tipo1,
            tipo2 = tipo2,
            hp = hp,
            altura = altura,
            peso = peso,
            descricao = descricao,
            imagem = urlImagem
        )

        pokemon.save()

        return redirect('aplicacao:home')
        
