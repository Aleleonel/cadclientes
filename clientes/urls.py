from django.urls import path
from .views import lista_cliente, cadastro_cliente, pedido_cliente, produto, lista_produtos, estoque, lista_estoque



urlpatterns = [   
    path('listaclientes/', lista_cliente, name="lista_clientes"),
    path('listaprodutos/',lista_produtos, name="lista_produtos" ),
    path('listaestoque/', lista_estoque, name="lista_estoque"),
    # o name será utilizado como um apelido da minha url la no meu html
    path('cadastro/', cadastro_cliente, name="cadastro_cliente"),
    path('pedido/', pedido_cliente, name="pedido_cliente"),
    path('produto/', produto, name="cadastro_produto"),
    path('estoque/', estoque, name="cadastro_estoque"),
]