from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Clientes, Produtos, Estoque, Pedidos, Item_Pedido
from .forms import ClientesForm, ProdutosForm, EstoqueForm, PedidosForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

@login_required
def lista_cliente(request):
    id = request.GET.get('id', None)
    nome = request.GET.get('nome', None)
    
    #checkbox = request.GET.get('status', None)
    #if checkbox == 'on':
    #listaclientes = Clientes.objects.filter(ativo=True)

    if id or nome:
        listaclientes = Clientes.objects.filter(cli_id__icontains=id) | Clientes.objects.filter(cli_nome__icontains=nome)
    else:
        listaclientes = Clientes.objects.all()
    return render(request, 'clientes/clientes.html', {"listaclientes": listaclientes})

@login_required
def cadastro_cliente(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_cliente')
    return render(request, 'clientes/clientes_form.html', {'form':form})

@login_required
def produto(request):
    form = ProdutosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'clientes/produtos_form.html', {'form':form})

@login_required
def lista_produtos(request):
    listaprodutos = Produtos.objects.all()
    return render(request, 'clientes/produtos.html', {"listaprodutos": listaprodutos})


@login_required
def estoque(request):
    form = EstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(request, self)
    return render(request, 'clientes/estoque_form.html', {'form':form})

@login_required
def lista_estoque(request):
    listaestoque = Estoque.objects.all()
    return render(request, 'clientes/estoque.html', {"listaestoque":listaestoque})

@login_required
def clientes_update(request, cli_id):
    cliente = get_object_or_404(Clientes, pk=cli_id)
    form = ClientesForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_cliente')

    return render(request,'clientes/clientes_form.html', {'form':form})

@login_required
def produto_update(request, pr_id):
    produto = get_object_or_404(Produtos, pk=pr_id)
    form = ProdutosForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'clientes/produtos_form.html', {'form':form})

@login_required   
def cliente_delete(request, cli_id):
    cliente = get_object_or_404(Clientes, pk=cli_id)
    #form = ClientesForm(request.POST or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_cliente')
    return render(request, 'clientes/cliente_delete.confirm.html', {'cliente':cliente})

@login_required
def produto_delete(request, pr_id):
    produto = get_object_or_404(Produtos, pk=pr_id)
    form = ProdutosForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'clientes/produto_delete.confirm.html', {'form':form})

def menu(request):
    return render(request, 'clientes/menu.html')

@login_required
def pedido_cliente(request):
    form = PedidosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listapedidos')
    return render(request, 'clientes/pedidos_form.html', {'form':form})

@login_required
def visualizarPedido(request):
    pedido = Pedidos.objects.all()
    return render(request, 'clientes/verPed.html', {'pedido':pedido})

# TODO: Tratar desta função mais tarde
@login_required
def visualizarItensPedido():
    itens = Item_Pedido.objects.all()
    return render(request, 'clientes/verPed.html', {'itens':itens})

class ClientesList(ListView):
    model = Clientes
    
class ClientesDetail(DetailView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']= timezone.now()
        return context

    



    





