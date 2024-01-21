from django.shortcuts import render, redirect
from .models import Apostila, ViewApostila
from django.contrib.messages import constants
from django.contrib import messages, auth

def adicionar_apostilas(request):
    if request.method == 'GET':
        return render(request, 'adicionar_apostilas.html')

def adicionar_apostilas(request):
    if request.method == 'GET':
        apostilas = Apostila.objects.filter(user=request.user)
        return render(request, 'adicionar_apostilas.html', {'apostilas': apostilas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES['arquivo']

        apostila = Apostila(user=request.user, titulo=titulo, arquivo=arquivo)
        apostila.save()
        messages.add_message(
            request, constants.SUCCESS, 'Apostila adicionada com sucesso.'
        )

        views_totais = ViewApostila.objects.filter(apostila__user = request.user).count()
        return redirect('/apostilas/adicionar_apostilas/')        

def apostila(request, id):
    apostila = Apostila.objects.get(id=id)
    view = ViewApostila(
        ip=request.META['REMOTE_ADDR'],
        apostila=apostila
    )
    view.save()
    views_unicas = ViewApostila.objects.filter(apostila=apostila).values('ip').distinct().count()
    views_totais = ViewApostila.objects.filter(apostila=apostila).count()
    return render(request, 'apostila.html', {'apostila': apostila, 'views_unicas': views_unicas, 'views_totais': views_totais})
