"""
URL configuration for Desenrola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views_recomendacoes
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),
    path("recomendacoes/", views_recomendacoes.recomendacoes, name="recomendacoes"),
    path('perfil/', views.meu_perfil_view, name='meu_perfil'),
    path('perfil/editar/', views.editar_perfil_view, name='editar_perfil'),
    path('perfil/<str:username>/', views.perfil_publico, name='perfil_publico'),
    path('sessoes/', views.sessoes_view, name='sessoes'),
    path('404/', views.erro404, name='erro404'),
    path('denunciar/', views.reportar, name='reportar'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]
