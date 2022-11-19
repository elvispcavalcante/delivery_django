# Passo a passo para criar uma página. Para cada link no path você precisa criar as 3 coisas abaixo:
# 1º - URL
# 2º - View
# 3º - Template

from django.urls import path, reverse, reverse_lazy
from django.contrib.auth import views as auth_view
from .views import PaginaPerfil, Criarconta, Principal, LojaCadastro, LojaConsulta, LojaAlteracao, LojaDeletar, \
    EntregadorCadastro, EntregadorConsulta, EntregadorAlterar, EntregadorDeletar, CategoriaCadastro, \
    CategoriaAlterar, CategoriaConsulta, CategoriaDeletar, ClienteCadastro, ClienteConsulta, ClienteAlterar, \
    ClienteDeletar, ProdutoCadastro, ProdutoConsulta, ProdutoAlterar, ProdutoDeletar, consultaVenda, \
    inserirVenda, editarVenda, deletarVenda

app_name = 'core'

urlpatterns = [

    # ------- URLS DE USUÁRIO -------
    path('', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', PaginaPerfil.as_view(template_name='editarperfil.html'), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(template_name='criarconta.html'),
         name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('core:principal')),
         name='mudarsenha'),

    # ------- URL PRINCIPAL -------
    path('principal/', Principal.as_view(template_name='principal.html'), name='principal'),

    # ------- URLS DA LOJA -------
    path('lojacadastro/', LojaCadastro.as_view(success_url=reverse_lazy('core:lojaconsulta')), name='lojacadastro'),
    path('lojaconsulta/', LojaConsulta.as_view(), name='lojaconsulta'),
    path('lojaalterar/<int:pk>', LojaAlteracao.as_view(success_url=reverse_lazy('core:lojaconsulta')),
         name='lojaalterar'),
    path('lojadeletar/<int:pk>', LojaDeletar.as_view(success_url=reverse_lazy('core:lojaconsulta')),
         name='lojadeletar'),

    # ------- URLS DOS ENTREGADORES -------
    path('entregadorcadastro/', EntregadorCadastro.as_view(success_url=reverse_lazy('core:entregadorconsulta')),
         name='entregadorcadastro'),
    path('entregadorconsulta/', EntregadorConsulta.as_view(), name='entregadorconsulta'),
    path('entregadoralterar/<int:pk>', EntregadorAlterar.as_view(success_url=reverse_lazy('core:entregadorconsulta')),
         name='entregadoralterar'),
    path('entregadordeletar/<int:pk>', EntregadorDeletar.as_view(success_url=reverse_lazy('core:entregadorconsulta')),
         name='entregadordeletar'),

    # ------- URLS DE CATEGORIA -------
    path('categoriacadastro/', CategoriaCadastro.as_view(success_url=reverse_lazy('core:categoriaconsulta')),
         name='categoriacadastro'),
    path('categoriaconsulta/', CategoriaConsulta.as_view(), name='categoriaconsulta'),
    path('categoriaalterar/<int:pk>', CategoriaAlterar.as_view(success_url=reverse_lazy('core:categoriaconsulta')),
         name='categoriaalterar'),
    path('categoriadeletar/<int:pk>', CategoriaDeletar.as_view(success_url=reverse_lazy('core:categoriaconsulta')),
         name='categoriadeletar'),

    # ------- URLS DE PRODUTO -------
    path('produtocadastro/', ProdutoCadastro.as_view(success_url=reverse_lazy('core:produtoconsulta')),
         name='produtocadastro'),
    path('produtoconsulta/', ProdutoConsulta.as_view(), name='produtoconsulta'),
    path('produtoalterar/<int:pk>', ProdutoAlterar.as_view(success_url=reverse_lazy('core:produtoconsulta')),
         name='produtoalterar'),
    path('produtodeletar/<int:pk>', ProdutoDeletar.as_view(success_url=reverse_lazy('core:produtoconsulta')),
         name='produtodeletar'),

    # ------- URLS DE CLIENTE -------
    path('clientecadastro/', ClienteCadastro.as_view(success_url=reverse_lazy('core:clienteconsulta')),
         name='clientecadastro'),
    path('clienteconsulta/', ClienteConsulta.as_view(), name='clienteconsulta'),
    path('clientealterar/<int:pk>', ClienteAlterar.as_view(success_url=reverse_lazy('core:clienteconsulta')),
         name='clientealterar'),
    path('clientedeletar/<int:pk>', ClienteDeletar.as_view(success_url=reverse_lazy('core:clienteconsulta')),
         name='clientedeletar'),

    # ------- URLS DE VENDA -------
    path('consultavenda/', consultaVenda, name='consultavenda'),
    path('inserirvenda/', inserirVenda, name='inserirvenda'),
    path('editarvenda/<int:id>', editarVenda, name='editarvenda'),
    path('deletarvenda/<int:id>', deletarVenda, name='deletarvenda'),
]

