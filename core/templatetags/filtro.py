from django import template
from core.models import Produto

register = template.Library()


@register.filter(name='get_preco')
def get_preco(produto_id):
    return Produto.objects.filter(id=produto_id)
