from django.urls import path
from .views import lista_produtos, cadastra_produto, atualiza_produto, delete_produto

urlpatterns = [
    path('produto/', lista_produtos, name='lista_produtos'),
    path('cadastra_produto/', cadastra_produto, name='cadastra_produto'),
    path('atualiza_produto/<int:id>/', atualiza_produto, name='atualiza_produto'),
    path('delete_produto/<int:id>/', delete_produto, name='delete_produto'),
]
