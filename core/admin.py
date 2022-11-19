from django.contrib import admin
from .models import Usuario, Loja, Entregador, Categoria, Produto, Cliente, Venda, DetalheVenda, Entrega
from django.contrib.auth.admin import UserAdmin

# Informações do Usuário para colocar na Administração
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Dados Pessoais", {'fields': ('cpf',)})
)
UserAdmin.fieldsets = tuple(campos)
# Fim dos dados do Usuário


class LojaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'razao_social', 'cnpj', 'endereco', 'latitude', 'longitude', 'data_criacao',
                    'data_modificacao']
    search_fields = ['nome', 'razao_social', 'cnpj', 'endereco', 'data_criacao', 'data_modificacao']
    list_per_page = 10


class EntregadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'telefone', 'chave_pix', 'endereco', 'data_nascimento', 'loja']
    search_fields = ['nome', 'cpf', 'email', 'telefone']
    list_per_page = 10


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']
    search_fields = ['categoria']
    list_per_page = 10


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'categoria', 'preco']
    search_fields = ['produto']
    list_per_page = 10


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'telefone', 'endereco', 'data_nascimento', 'latitude', 'longitude']
    search_fields = ['nome', 'cpf', 'email', 'telefone']
    list_per_page = 10


class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data_venda', 'cliente', 'forma_pagamento', 'forma_da_venda']
    search_fields = ['cliente', 'forma_pagamento', 'forma_da_venda']
    list_per_page = 10


class DetalheVendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'venda', 'produto']
    search_fields = ['venda', 'produto']
    list_per_page = 10


class EntregaAdmin(admin.ModelAdmin):
    list_display = ['venda', 'entregador']
    search_fields = ['venda', 'entregador']
    list_per_page = 10


# Registrando os modelos na Administração do Django
admin.site.register(Usuario, UserAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Entregador, EntregadorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(DetalheVenda, DetalheVendaAdmin)
admin.site.register(Entrega, EntregaAdmin)
