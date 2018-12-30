from django.shortcuts import render, redirect
from .models import Clientes, Pedidos, Produtos, Estoque
from .forms import ClientesForm, PedidosForm, ProdutosForm, EstoqueForm


def cadastro_cliente(request):
    form = ClientesForm(request.POST, None)

    if form.is_valid():
        form.save()
        return redirect('clientes/lista_cliente')
    return render(request, 'clientes/clientes_form.html', {'form':form})

def lista_cliente(request):
    listaclientes = Clientes.objects.all()
    return render(request, 'clientes/clientes.html', {"listaclientes": listaclientes})


def pedido_cliente(request):
    form = PedidosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(request, self)
    return render(request, 'clientes/pedidos_form.html', {'form':form})

def produto(request):
    form = ProdutosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'clientes/produtos_form.html', {'form':form})

def lista_produtos(request):
    listaprodutos = Produtos.objects.all()
    return render(request, 'clientes/produtos.html', {"listaprodutos": listaprodutos})

def estoque(request):
    form = EstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request, self)
    return render(request, 'clientes/estoque_form.html', {'form':form})

def lista_estoque(request):
    listaestoque = Estoque.objects.all()
    return render(request, 'clientes/estoque.html', {"listaestoque":listaestoque})





