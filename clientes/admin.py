from django.contrib import admin
from .models import Clientes, Pedidos, Produtos, Item_Pedido, Estoque

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Pedidos)
admin.site.register(Produtos)
admin.site.register(Item_Pedido)
admin.site.register(Estoque)
