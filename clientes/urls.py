from django.urls import path
from .views import lista_cliente, cadastro_cliente, pedido_cliente, produto, lista_produtos


urlpatterns = [   
    path('listaclie/', lista_cliente, name="lista_clientes"),
    path('listaprod/',lista_produtos, name="lista_produtos" ),
    # o name será utilizado como um apelido da minha url la no meu html
    path('cadastro/', cadastro_cliente, name="cadastro_cliente"),
    path('pedido/', pedido_cliente, name="pedido_cliente"),
    path('produto/', produto, name='cadastro_produto'),
]