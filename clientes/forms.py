from django.forms import ModelForm
from clientes.models import Clientes, Pedidos, Produtos, Estoque


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['cli_nome', 'cli_fantasia','cli_endereco','cli_numero',
        'cli_cpe','cli_cidade','cli_uf', 'cli_cpf','cli_insest','cli_fone1',
        'cli_fone2','cli_email','cli_histotrico'
        ]


class PedidosForm(ModelForm):       
    class Meta:
        model = Pedidos
        fields =['ped_nomecli','ped_enderco','ped_vluntario',
        'ped_qte','ped_vltotalitem','ped_vltotalpedido'
        ]

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['pr_descricao', 'pr_preco']


class EstoqueForm(ModelForm):
    class Meta:
        model = Estoque
        fields = [ 'est_qtd']
