# Generated by Django 4.1.2 on 2022-10-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_detalhesvenda_detalhevenda_entregador_loja'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(choices=[('Em atendimento', 'Em atendimento'), ('Entrega', 'Entrega'), ('Finalizado', 'Finalizado')], default='Em atendimento', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venda',
            name='forma_da_venda',
            field=models.CharField(choices=[('1', 'Presencial'), ('2', 'Whatsapp'), ('3', 'Ifood'), ('4', 'UberEats'), ('5', 'Telefone'), ('6', 'Instagram'), ('7', 'Facebook')], max_length=60),
        ),
        migrations.AlterField(
            model_name='venda',
            name='forma_pagamento',
            field=models.CharField(choices=[('1', 'Dinheiro'), ('2', 'PIX'), ('3', 'Cartão de Crédito - Visa'), ('4', 'Cartão de Crédito - Master'), ('5', 'Cartão de Crédito - Elo'), ('6', 'Cartão de Crédito - Outros'), ('7', 'Débito')], max_length=60),
        ),
    ]