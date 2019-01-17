from django.contrib import admin
from .models import Clientes, Produtos, Estoque, Pedidos, Item_Pedido

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Produtos)
admin.site.register(Estoque)
admin.site.register(Item_Pedido)
admin.site.register(Pedidos)
