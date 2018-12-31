from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Pedidos, Produtos, Estoque
from .forms import ClientesForm, PedidosForm, ProdutosForm, EstoqueForm

def lista_cliente(request):
    listaclientes = Clientes.objects.all()
    return render(request, 'clientes/clientes.html', {"listaclientes": listaclientes})

def cadastro_cliente(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_cliente')
    return render(request, 'clientes/clientes_form.html', {'form':form})


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

def clientes_update(request, cli_id):
    cliente = get_object_or_404(Clientes, pk=cli_id)
    form = ClientesForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_cliente')

    return render(request,'clientes/clientes_form.html', {'form':form})

def produto_update(request, pr_id):
    produto = get_object_or_404(Produtos, pk=pr_id)
    form = ProdutosForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'clientes/produtos_form.html', {'form':form})
    
def cliente_delete(request, cli_id):
    cliente = get_object_or_404(Clientes, pk=cli_id)
    #form = ClientesForm(request.POST or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_cliente')
    return render(request, 'clientes/cliente_delete.confirm.html', {'cliente':cliente})


def produto_delete(request, pr_id):
    produto = get_object_or_404(Produtos, pk=pr_id)
    form = ProdutosForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'clientes/produto_delete.confirm.html', {'form':form})

    



    





