from django.urls import path
from . import views
from .views import ClientesDetail




urlpatterns = [   

    # urls de listagens 
    path('menu/', views.menu, name="menu"),
    path('listapedidos/', views.visualizarPedido, name="listapedidos"),
    path('listaclientes/', views.lista_cliente, name="lista_cliente"),
    path('listaprodutos/',views.lista_produtos, name="lista_produtos" ),
    path('listaestoque/', views.lista_estoque, name="lista_estoque"),
    
    # url clientesList Teste
    path('clientes/', views.ClientesList.as_view()),
   
        
    # o name será utilizado como um apelido da minha url la no meu html
    path('cadastro/', views.cadastro_cliente, name="cadastro_cliente"),
    path('produto/', views.produto, name="cadastro_produto"),
    path('estoque/', views.estoque, name="cadastro_estoque"),
    path('pedido/', views.pedido_cliente, name="pedido_cliente"),
    
    # urls atualização de cadastro existente
    path('updatecliente/<int:cli_id>/', views.clientes_update, name="clientes_update"),
    path('updateproduto/<int:pr_id>/', views.produto_update, name="produto_update"),
    path('deletecliente/<int:cli_id>/', views.cliente_delete, name="cliente_delete"),
    path('deleteproduto/<int:pr_id>/', views.produto_delete, name="produto_delete"),

    # url clientesList Teste
    path('detail/<int:pk>/', ClientesDetail.as_view(), name='clientes_cbv'),
    
]