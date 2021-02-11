from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import FormPessoa
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "index.html")


@login_required
def pessoa(request):
    termo_pesquisa = request.GET.get("Pesquisa", None)
    if termo_pesquisa:
        pessoas = Pessoa.objects.all()
        pessoas = pessoas.filter(primeiro_nome=termo_pesquisa)
    else:
        pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})


@login_required
def cadastra_pesssoa(request):
    form = FormPessoa(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, 'cadastra_pessoa.html', {'form': form})


@login_required
def atualiza_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = FormPessoa(request.POST or None, request.FILES or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, 'cadastra_pessoa.html', {'form': form})


@login_required
def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'delete_confirme.html', {'pessoa': pessoa})
