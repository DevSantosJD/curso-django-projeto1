from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')# teste página raiz home 

def contato(request):
    return HttpResponse('contato (11) 97070-7070') #test de retorno

def sobre(request):
    return HttpResponse('Desenvolvedor Back-end Python Django') #teste de retorno com um toque de humor
