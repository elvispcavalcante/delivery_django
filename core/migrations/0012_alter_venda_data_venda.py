# Generated by Django 4.1.2 on 2022-11-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_venda_forma_da_venda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_venda',
            field=models.DateTimeField(),
        ),
    ]
