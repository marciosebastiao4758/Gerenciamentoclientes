"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from clientes.views import pessoa, cadastra_pesssoa, atualiza_pessoa, delete_pessoa

urlpatterns = [
    path('pessoa/', pessoa, name='lista_pessoas'),
    path('cadastra_pessoa/', cadastra_pesssoa, name='cadastra_pessoa'),
    path('atualiza_pessoa/<int:id>', atualiza_pessoa, name='atualiza_pessoa'),
    path('delete_pessoa/<int:id>', delete_pessoa, name='delete_pessoa'),
]
