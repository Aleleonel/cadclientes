# Generated by Django 2.0 on 2018-12-27 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cli_nome', models.CharField(max_length=50)),
                ('cli_fantasia', models.CharField(blank=True, max_length=50)),
                ('cli_dtcad', models.DateField(auto_now=True)),
                ('cli_endereco', models.CharField(max_length=100)),
                ('cli_numero', models.CharField(max_length=5)),
                ('cli_cpe', models.CharField(max_length=8)),
                ('cli_cidade', models.CharField(max_length=30)),
                ('cli_uf', models.CharField(max_length=2)),
                ('cli_cpf', models.CharField(blank=True, max_length=11, unique=True)),
                ('cli_insest', models.CharField(blank=True, max_length=11, unique=True)),
                ('cli_fone1', models.CharField(blank=True, max_length=11)),
                ('cli_fone2', models.CharField(blank=True, max_length=11)),
                ('cli_email', models.CharField(max_length=30)),
                ('cli_histotrico', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('est_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('est_qtd', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('it_descricao', models.CharField(max_length=256)),
                ('it_qtd', models.PositiveIntegerField(default=0)),
                ('it_valor', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('ped_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ped_dt', models.DateField(auto_now=True)),
                ('ped_nomecli', models.CharField(max_length=50)),
                ('ped_enderco', models.CharField(max_length=100)),
                ('ped_qte', models.PositiveIntegerField(default=0)),
                ('ped_vluntario', models.FloatField(default=0)),
                ('ped_vltotalitem', models.FloatField(default=0)),
                ('ped_vltotalpedido', models.FloatField(default=0)),
                ('cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('pr_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('pr_descricao', models.CharField(max_length=256)),
                ('pr_preco', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='item_pedido',
            name='ped_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Pedidos'),
        ),
        migrations.AddField(
            model_name='item_pedido',
            name='pr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Produtos'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='pr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Produtos'),
        ),
    ]
