from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.utils import timezone

# ------- MODEL USUÁRIO -------
class Usuario(AbstractUser):
    cpf = CPFField(masked=True)


# ------- MODEL LOJA -------
class Loja(models.Model):
    nome = models.CharField(max_length=150)
    razao_social = models.CharField(max_length=150)
    cnpj = CNPJField(masked=True)
    endereco = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome + ' - ' + str(self.cnpj)

    class Meta:
        ordering = ['nome']

    """
    def save(self, *args, **kwargs):
        # Para salvar, atualizar os campos de DateTimeField
        if not self.id:
            self.data_criacao = timezone.now()
        self.data_modificacao = timezone.now()
        return super(Loja, self).save(*args, **kwargs)
    """


# ------- MODEL ENTREGADORES -------
class Entregador(models.Model):
    nome = models.CharField(max_length=120)
    cpf = CPFField(masked=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)
    chave_pix = models.CharField(max_length=80)
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome + ' - ' + str(self.cpf)

    class Meta:
        ordering = ['nome']


# ------- MODEL CATEGORIA -------
class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ['categoria']


# ------- MODEL PRODUTOS -------
class Produto(models.Model):
    produto = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto + ' - ' + self.categoria.categoria + ' - ' + str(self.preco)

    class Meta:
        ordering = ['produto']


# ------- MODEL CLIENTES -------
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = CPFField(masked=True, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=25, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome + ' - ' + str(self.cpf)

    class Meta:
        ordering = ['nome']


FORMA_PAGAMENTO_CHOICES = (
    ('Dinheiro', 'Dinheiro'),
    ('Pix', 'PIX'),
    ('Cartão de Crédito - Visa', 'Cartão de Crédito - Visa'),
    ('Cartão de Crédito - Master', 'Cartão de Crédito - Master'),
    ('Cartão de Crédito - Elo', 'Cartão de Crédito - Elo'),
    ('Cartão de Crédito - Outros', 'Cartão de Crédito - Outros'),
    ('Débito', 'Débito')
)

FORMA_VENDA_CHOICES = (
    ('Presencial', 'Presencial'),
    ('Whatsapp', 'Whatsapp'),
    ('Ifood', 'Ifood'),
    ('Ubereats', 'UberEats'),
    ('Telefone', 'Telefone'),
    ('Instagram', 'Instagram'),
    ('Facebook', 'Facebook')
)

STATUS_CHOICES = (
    ('Em atendimento', 'Em atendimento'),
    ('Entrega', 'Entrega'),
    ('Finalizado', 'Finalizado'),
)


# ------- MODEL VENDAS -------
class Venda(models.Model):
    data_venda = models.DateTimeField(editable=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=60, choices=FORMA_PAGAMENTO_CHOICES)
    forma_da_venda = models.CharField(max_length=60, choices=FORMA_VENDA_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(timezone.localtime(self.data_venda).strftime('%d/%m/%Y')) + ' - ' + self.cliente.nome + ' - ' \
               + str(self.cliente.cpf)

    class Meta:
        ordering = ['data_venda']


# ------- MODEL DETALHES VENDAS -------
class DetalheVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.venda.id) + ' - ' + self.produto.produto + ' - ' + str(self.preco)

    class Meta:
        ordering = ['venda']


# ------- MODEL ENTREGAS -------
class Entrega(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(editable=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.venda.id) + ' - ' + self.entregador.nome

    class Meta:
        ordering = ['venda']

