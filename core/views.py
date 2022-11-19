from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView, UpdateView, CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, LojaCadastroForm, LoginForm, EntregadorCadastroForm, CategoriaCadastroForm, \
    ClienteCadastroForm, ProdutoCadastroForm, VendaCadastroForm, DetalheVendaCadastroForm
from .models import Usuario, Loja, Entregador, Categoria, Produto, Cliente, Venda, DetalheVenda, Entrega
from django.views.generic.detail import SingleObjectMixin
from django.db.models.aggregates import Sum
from django.contrib import messages
from django.contrib.messages import constants


# --------- Views do Usuário ---------
class PaginaLogin(CreateView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # usuario está autenticado:
            # redireciona para a página principal
            return HttpResponseRedirect('/principal/')
        else:
            return super().get(request, *args, **kwargs)  # redireciona para de login


class Principal(LoginRequiredMixin, TemplateView):
    template_name = 'principal.html'


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email', 'cpf']
    success_url = '/principal/'


class Criarconta(LoginRequiredMixin, FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm
    success_url = '/principal/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_sucess_url(self):
        return redirect(to='core:principal')
# --------- Fim das Views do Usuário ---------


# --------- Views da Loja ---------
class LojaCadastro(LoginRequiredMixin, CreateView):
    template_name = 'loja_cadastro.html'
    form_class = LojaCadastroForm
    success_url = reverse_lazy('core:lojaconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LojaConsulta(LoginRequiredMixin, ListView):
    template_name = 'loja_consulta.html'
    model = Loja
    queryset = Loja.objects.all()
    paginate_by = 1
    # def get_queryset(self):
    #     self.object_list = Loja.objects.all()
    #     return self.object_list


class LojaAlteracao(LoginRequiredMixin, UpdateView):
    model = Loja
    form_class = LojaCadastroForm
    success_url = reverse_lazy('lojaconsulta')
    template_name = 'loja_cadastro.html'


class LojaDeletar(LoginRequiredMixin, DeleteView):
    model = Loja
    queryset = Loja.objects.all()
    success_url = reverse_lazy('lojaconsulta')
    template_name = 'loja_deletar.html'
# --------- Fim das Views da Loja ---------


# --------- Views do Entregador ---------
class EntregadorCadastro(LoginRequiredMixin, CreateView):
    template_name = 'entregador_cadastro.html'
    form_class = EntregadorCadastroForm
    success_url = reverse_lazy('core:principal')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EntregadorConsulta(LoginRequiredMixin, ListView):
    template_name = 'entregador_consulta.html'
    model = Entregador
    queryset = Entregador.objects.all()
    paginate_by = 1


class EntregadorAlterar(LoginRequiredMixin, UpdateView):
    model = Entregador
    form_class = EntregadorCadastroForm
    template_name = 'entregador_cadastro.html'
    success_url = reverse_lazy('entregadorconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EntregadorDeletar(LoginRequiredMixin, DeleteView):
    model = Entregador
    queryset = Entregador.objects.all()
    success_url = reverse_lazy('core:entregadorconsulta')
    template_name = 'entregador_deletar.html'

# --------- Fim das Views do Entregador ---------


# --------- Views do Categoria ---------
class CategoriaCadastro(LoginRequiredMixin, CreateView):
    template_name = 'categoria_cadastro.html'
    form_class = CategoriaCadastroForm
    success_url = reverse_lazy('categoriaconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CategoriaConsulta(LoginRequiredMixin, ListView):
    template_name = 'categoria_consulta.html'
    model = Categoria
    queryset = Categoria.objects.all()
    paginate_by = 1


class CategoriaAlterar(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaCadastroForm
    template_name = 'categoria_cadastro.html'
    success_url = reverse_lazy('categoriaconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CategoriaDeletar(LoginRequiredMixin, DeleteView):
    model = Categoria
    queryset = Categoria.objects.all()
    success_url = reverse_lazy('core:categoriaconsulta')
    template_name = 'categoria_deletar.html'

# --------- Fim das Views do Cateooria ---------


# --------- Views do Produto ---------
class ProdutoCadastro(LoginRequiredMixin, CreateView):
    template_name = 'produto_cadastro.html'
    form_class = ProdutoCadastroForm
    success_url = reverse_lazy('produtoconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProdutoConsulta(LoginRequiredMixin, ListView):
    template_name = 'produto_consulta.html'
    model = Produto
    queryset = Produto.objects.all()
    paginate_by = 1


class ProdutoAlterar(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoCadastroForm
    template_name = 'produto_cadastro.html'
    success_url = reverse_lazy('produtoconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProdutoDeletar(LoginRequiredMixin, DeleteView):
    model = Produto
    queryset = Produto.objects.all()
    success_url = reverse_lazy('core:produtoconsulta')
    template_name = 'produto_deletar.html'

# --------- Fim das Views do Produto ---------


# --------- Views do Cliente ---------
class ClienteCadastro(LoginRequiredMixin, CreateView):
    template_name = 'cliente_cadastro.html'
    form_class = ClienteCadastroForm
    success_url = reverse_lazy('clienteconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ClienteConsulta(LoginRequiredMixin, ListView):
    template_name = 'cliente_consulta.html'
    model = Cliente
    queryset = Cliente.objects.all()
    paginate_by = 1


class ClienteAlterar(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteCadastroForm
    template_name = 'cliente_cadastro.html'
    success_url = reverse_lazy('clienteconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ClienteDeletar(LoginRequiredMixin, DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('core:clienteconsulta')
    template_name = 'cliente_deletar.html'

# --------- Fim das Views do Cliente ---------


# --------- Views da Venda ---------
class VendaCadastro(LoginRequiredMixin, CreateView):
    template_name = 'venda_cadastro.html'
    form_class = ClienteCadastroForm
    success_url = reverse_lazy('vendaconsulta')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def inserirVenda(request):
    if request.method == 'GET':
        form = VendaCadastroForm()
        form_detalhe_venda_factory = inlineformset_factory(Venda, DetalheVenda, form=DetalheVendaCadastroForm, extra=5)
        form_detalhe_venda = form_detalhe_venda_factory()
        context = {
            'form': form,
            'form_detalhe_venda': form_detalhe_venda,
        }
        return render(request, "venda_cadastro.html", context)
    elif request.method == 'POST':
        form = VendaCadastroForm(request.POST)
        form_detalhe_venda_factory = inlineformset_factory(Venda, DetalheVenda, form=DetalheVendaCadastroForm)
        form_detalhe_venda = form_detalhe_venda_factory(request.POST)
        if form.is_valid() and form_detalhe_venda.is_valid():
            # print(request.POST)
            # data_correta = request.POST['data_venda'] + timedelta(days=1)
            # request.POST['data_venda'] = data_correta
            # form.Venda.data_venda = data_correta
            venda = form.save()
            form_detalhe_venda.instance = venda
            form_detalhe_venda.save()
            return redirect(reverse_lazy('core:consultavenda'))
        else:
            context = {
                'form': form,
                'form_detalhe_venda': form_detalhe_venda
            }
        return render(request, 'venda_cadastro.html', context)


def consultaVenda(request):
    if request.method == 'GET':
        vendas = Venda.objects.all().exclude(status='Finalizado')
        vendas_finalizadas = Venda.objects.filter(status='Finalizado')
        # detalhes_vendas = DetalheVenda.objects.filter(venda__status__in=['Em atendimento', 'Entrega'])
        detalhes_vendas = DetalheVenda.objects.values('venda__id').annotate(total=Sum('produto__preco'))

        # print(detalhes_vendas)
        context = {
            'vendas': vendas,
            'vendas_finalizadas': vendas_finalizadas,
            'detalhes_vendas': detalhes_vendas,
        }
        return render(request, "venda_consulta.html", context)


def editarVenda(request, id):
    if request.method == 'GET':
        objeto = Venda.objects.filter(id=id).first()

        if objeto is None:
            return redirect(reverse_lazy('core:consultavenda'))

        form = VendaCadastroForm(instance=objeto)
        form_detalhe_venda_factory = inlineformset_factory(Venda, DetalheVenda, form=DetalheVendaCadastroForm, extra=5)
        form_detalhe_venda = form_detalhe_venda_factory(instance=objeto)
        context = {
            'form': form,
            'form_detalhe_venda': form_detalhe_venda,
        }
        return render(request, "venda_cadastro.html", context)
    elif request.method == "POST":
        objeto = Venda.objects.filter(id=id).first()

        if objeto is None:
            return redirect(reverse_lazy('core:consultavenda'))

        form = VendaCadastroForm(request.POST, instance=objeto)
        form_detalhe_venda_factory = inlineformset_factory(Venda, DetalheVenda, form=DetalheVendaCadastroForm)
        form_detalhe_venda = form_detalhe_venda_factory(request.POST, instance=objeto)

        if form.is_valid() and form_detalhe_venda.is_valid():
            # print(form.is_valid())
            # print(form_detalhe_venda.is_valid())
            # print('Error Messages: ', form_detalhe_venda.error_messages)
            # print('Errors: ', form_detalhe_venda.errors)
            venda = form.save()
            form_detalhe_venda.instance = venda
            form_detalhe_venda.save()
            return redirect(reverse_lazy('core:consultavenda'))
        else:
            context = {
                'form': form,
                'form_detalhe_venda': form_detalhe_venda
            }
            print(context)
            messages.add_message(request, constants.ERROR, f'Erro ao atualizar a venda')
        return render(request, 'venda_cadastro.html', context)


def deletarVenda(request, id):
    if request.method == 'POST':
        venda = Venda.objects.filter(id=id).first()
        if venda is None:
            return redirect(reverse_lazy('core:consultavenda'))
        venda.delete()
        messages.add_message(request, constants.SUCCESS, 'Venda excluída com sucesso')
        return redirect(reverse_lazy('core:consultavenda'))
    if request.method == 'GET':
        venda = Venda.objects.filter(id=id).first()
        if venda is None:
            return redirect(reverse_lazy('core:consultavenda'))

        context = {
            'venda': venda,
        }

        return render(request, 'venda_deletar.html', context)
