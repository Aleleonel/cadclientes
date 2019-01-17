from django.db import models

# Create your models clientes here.

class Clientes(models.Model):
    cli_id = models.AutoField(primary_key=True, unique=True)
    cli_nome = models.CharField(max_length=50)
    cli_fantasia = models.CharField(max_length=50, blank=True)
    cli_dtcad = models.DateField(auto_now=True)
    cli_endereco = models.CharField(max_length=100)
    cli_numero = models.CharField(max_length=5)
    cli_cpe = models.CharField(max_length=8)
    cli_cidade = models.CharField(max_length=30)
    cli_uf = models.CharField(max_length=2)
    cli_cpf = models.CharField(max_length=11, unique=True, blank=True)
    cli_insest = models.CharField(max_length=11, blank=True)
    cli_fone1 = models.CharField(max_length=11, blank=True)
    cli_fone2 = models.CharField(max_length=11, blank=True)
    cli_email = models.CharField(max_length=30)
    cli_histotrico = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.cli_nome+ '-' +self.cli_fantasia


class Pedidos(models.Model):
    ped_id = models.AutoField(primary_key=True, unique=True)
    ped_dt = models.DateField(auto_now=True)
    ped_nomecli = models.CharField(max_length=50)
    ped_enderco = models.CharField(max_length =100)
    ped_qte = models.PositiveIntegerField(default=0)
    ped_vluntario = models.FloatField(default=0)
    ped_vltotalitem = models.FloatField(default=0)
    ped_vltotalpedido = models.FloatField(default=0)
    cli_id = models.ForeignKey('Clientes', on_delete=models.CASCADE)

    def __str__(self):
        return self.ped_nomecli

class Item_Pedido(models.Model):
    ped_id = models.ForeignKey('Pedidos', on_delete=models.CASCADE)
    pr_id = models.ForeignKey('Produtos', on_delete=models.CASCADE)
    it_descricao = models.CharField(max_length=256)
    it_qtd =models.PositiveIntegerField(default=0)
    it_valor = models.FloatField(default=0)

    def __str__(self):
        return self.it_descricao

class Produtos(models.Model):
    pr_id = models.AutoField(primary_key=True, unique=True)
    pr_descricao = models.CharField(max_length=256)
    pr_preco = models.FloatField(default=0)

    def __str__(self):
        return self.pr_descricao


class Estoque(models.Model):
    est_id = models.AutoField(primary_key=True, unique=True)
    est_qtd = models.PositiveIntegerField(default=0)
    pr_id = models.ForeignKey('Produtos', on_delete=models.CASCADE)



"""lass Veiculo(models.Model):
nome = models.CharField(_('nome'), max_length=50, unique=True)
valor = models.DecimalField(_(u'preço'), max_digits=8, decimal_places=2)
kit = models.ForeignKey("Kit", verbose_name=u'kit de fábrica')

class Kit(models.Model):
    kit = models.CharField(max_length=50)
    acessorios = models.ManyToManyField('Acessorio', blank=True, null=True)

class Acessorio(models.Model):
    nome = models.CharField(_(u'accessório'), max_length=50)
    valor = models.DecimalField(_(u'preço'), max_digits=8, decimal_places=2)
    quantidade = models.PositiveIntegerField()

class Pedido(TimeStampedModel):
    customer = models.ForeignKey("Customer", verbose_name='cliente')
    employee = models.ForeignKey("Employee", verbose_name=u'funcionário')
    veiculo = models.ForeignKey("Veiculo", verbose_name=u'veículo')
    kit_optional = models.ForeignKey("Kit", verbose_name='kit opcional')
    dealership = models.ForeignKey(
        "Dealership", verbose_name=u'concessionária')
    kiosk = models.ForeignKey("Kiosk", verbose_name='quiosque')
    status = models.CharField(max_length=2, choices=status_list, default='p')"""
    

















