from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'home.html')

def escrever(request):
    if request.method == "GET":
        pessoa = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoa': pessoa })
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')  
        tags = request.POST.getlist('tags') 
        pessoas = request.POST.getlist('pessoas')   
        texto = request.POST.get('texto')  
        
        return HttpResponse(f'{titulo} - {tags} - {pessoas} - {texto}')  # Usando f-string para formatar a resposta

def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')  
        foto = request.FILES.get('foto') 
        
        pessoa = Pessoa(
            name=nome,  
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')

