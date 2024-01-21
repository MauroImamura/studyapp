from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('entrar/', views.entrar, name='login'),
    path('sair/', views.sair, name='logout'),
]