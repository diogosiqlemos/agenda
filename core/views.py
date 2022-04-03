from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.

def local_evento(request, titulo_evento):
    evento1 = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>O local do/a {} é {}.</h1>'.format(titulo_evento, evento1.local))

def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

