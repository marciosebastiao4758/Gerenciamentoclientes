from django.forms import ModelForm
from .models import Produto


class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco']
