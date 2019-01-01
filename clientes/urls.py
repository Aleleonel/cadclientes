from django.urls import path
from .views import lista_cliente
from .views import cadastro_cliente
from .views import pedido_cliente
from .views import produto
from .views import lista_produtos
from .views import estoque
from .views import lista_estoque
from .views import clientes_update
from .views import produto_update
from .views import cliente_delete
from .views import produto_delete
from .views import menu


urlpatterns = [   

    path('menu/', menu, name="menu"),
    path('listaclientes/', lista_cliente, name="lista_cliente"),
    path('listaprodutos/',lista_produtos, name="lista_produtos" ),
    path('listaestoque/', lista_estoque, name="lista_estoque"),
    
    # o name será utilizado como um apelido da minha url la no meu html
    path('cadastro/', cadastro_cliente, name="cadastro_cliente"),
    path('pedido/', pedido_cliente, name="pedido_cliente"),
    path('produto/', produto, name="cadastro_produto"),
    path('estoque/', estoque, name="cadastro_estoque"),
    # urls atualização de cadastro existente
    path('updatecliente/<int:cli_id>/', clientes_update, name="clientes_update"),
    path('updateproduto/<int:pr_id>/', produto_update, name="produto_update"),
    path('deletecliente/<int:cli_id>/', cliente_delete, name="cliente_delete"),
    path('deleteproduto/<int:pr_id>/', produto_delete, name="produto_delete"),

]