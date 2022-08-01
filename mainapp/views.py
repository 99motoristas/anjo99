from django.shortcuts import render
from django.http import HttpResponse
from .models import Grupo

# Create your views here.

def index(request):
    #grupos = Grupo.objects.filter(numero_de_participantes<150)
    grupos = Grupo.objects.filter(numero_de_participantes__lte=120).order_by('numero_de_participantes')
    return render(request, 'mainapp/index.html', {'grupos': grupos})

def increase_counter(request, group_id):
    group = Grupo.objects.get(pk=group_id)
    group.numero_de_participantes = group.numero_de_participantes + 1
    group.save()
    return HttpResponse(group.link)
