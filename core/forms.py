import datetime

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Loja, Entregador, Categoria, Produto, Cliente, Venda, DetalheVenda
from django import forms
from tempus_dominus.widgets import DatePicker, DateTimePicker


# ------- FORM LOGIN -------
class LoginForm(forms.Form):
    pass


# ------- CRIAR USUÁRIO FORM -------
class CriarContaForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'cpf', 'email', 'password1', 'password2')
        labels = {'cpf': 'CPF'}


# ------- LOJA FORM -------
class LojaCadastroForm(forms.ModelForm):

    class Meta:
        model = Loja
        fields = ('nome', 'razao_social', 'cnpj', 'endereco', 'latitude', 'longitude')
        labels = {
            'nome': 'Nome',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'endereco': 'Endereço Completo',
            'latitude': 'Latitude',
            'longitude': 'Longitude'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome da loja'}),
            'razao_social': forms.TextInput(attrs={'placeholder': 'Digite a razão social da loja'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'Digite o CNPJ da loja'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Digite o endereço completo da loja'}),
        }


# ------- ENTREGADORES FORM -------
class EntregadorCadastroForm(forms.ModelForm):
    class Meta:
        model = Entregador
        fields = ('nome', 'cpf', 'email', 'telefone', 'chave_pix', 'endereco', 'data_nascimento')
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'email': 'Email',
            'telefone': 'Telefone',
            'chave_pix': 'Chave PIX',
            'endereco': 'Endereço Completo',
            'data_nascimento': 'Data de Nascimento'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do Entregador'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Digite o CPF do Entregador',
                                          'data-mask':'000.000.000-00'}),
            'email': forms.TextInput(attrs={'placeholder': 'Digite o e-mail'}),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefone',
                    'data-mask': '(00) 00000-0000',
                }
            ),
            'chave_pix': forms.TextInput(attrs={'placeholder': 'Digite a chave pix',
                                                'data-mask': '000.000.000-00'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Digite o endereço completo'}),
            'data_nascimento': forms.DateInput(attrs={'placeholder': 'Digite a data de nascimento',
                                                      'data-mask': '00/00/0000'}, format='%d/%m/%Y'),
        }


# ------- CATEGORIA FORM -------
class CategoriaCadastroForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('categoria',)
        labels = {
            'categoria': 'Categoria',
        }

        widgets = {
            'categoria': forms.TextInput(attrs={'placeholder': 'Digite o nome do Categoria'}),
        }


# ------- PRODUTO FORM -------
class ProdutoCadastroForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('produto', 'categoria', 'preco')
        labels = {
            'produto': 'Produto',
            'categoria': 'Categoria',
            'preco': 'Preço'
        }
        widgets = {
            'produto': forms.TextInput(attrs={'placeholder': 'Digite o produto'}),
            'categoria': forms.Select(),
        }


# ------- CLIENTES FORM -------
class ClienteCadastroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'cpf', 'email', 'telefone', 'endereco', 'data_nascimento', 'latitude', 'longitude')
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço Completo',
            'data_nascimento': 'Data de Nascimento',
            'latitude': 'Latitude',
            'longitude': 'Longitude'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do Cliente'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Digite o CPF do Entregador',
                                          'data-mask': '000.000.000-00'}),
            'email': forms.TextInput(attrs={'placeholder': 'Digite o e-mail'}),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefone',
                    'data-mask': '(00) 00000-0000',
                }
            ),
            'endereco': forms.TextInput(attrs={'placeholder': 'Digite o endereço completo'}),
            'data_nascimento': forms.DateInput(attrs={'placeholder': 'Digite a data de nascimento',
                                                      'data-mask': '00/00/0000'}, format='%d/%m/%Y'),
        }


# ------- VENDA FORM -------
class VendaCadastroForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('data_venda', 'cliente', 'forma_pagamento', 'forma_da_venda', 'status')
        labels = {
            'data_venda': 'Data da Venda',
            'cliente': 'Cliente',
            'forma_pagamento': 'Forma de Pagamento',
            'forma_da_venda': 'Forma da Venda',
            'status': 'Status',
        }

        clientes = Cliente.objects.all().values_list('id', 'nome')
        clientes_tuple = tuple(tuple(sub) for sub in clientes)

        widgets = {
            'data_venda': DateTimePicker(options={
                # 'minDate': '2022-01-01',
                # 'maxDate': datetime.datetime.now().strftime('%Y-%m-%d'),
                'collapse': True,
                # 'useCurrent': True,
                'timezone': 'America/Fortaleza'
            }, attrs={
                'append': 'fa fa-calendar',
                'icon_toogle': True,
                'input_toogle': True,
                'size': 'large',
                'timezone': 'America/Fortaleza'
            }),
            'cliente': forms.Select(choices=clientes_tuple)

        }


# ------- DETALHES_VENDA FORM -------
class DetalheVendaCadastroForm(forms.ModelForm):
    class Meta:
        model = DetalheVenda
        fields = ('id', 'venda', 'produto')
        labels = {
            'id': 'Código',
            'venda': 'Venda',
            'produto': 'Produto',
        }




