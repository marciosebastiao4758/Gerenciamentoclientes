from django.shortcuts import render, redirect
from .models import Produto
from .forms import FormProduto
from django.contrib.auth.decorators import login_required


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


@login_required
def cadastra_produto(request):
    form = FormProduto(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'cadastra_produto.html', {'form': form})


@login_required
def atualiza_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = FormProduto(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'cadastra_produto.html', {'form': form})


@login_required
def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produto')
    return render(request, 'delete_confirme.html', {'produto': produto})
