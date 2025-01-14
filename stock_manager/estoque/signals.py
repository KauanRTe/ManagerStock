from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movimentacao, Produto

@receiver(post_save, sender=Movimentacao)
def atualizar_estoque(sender, instance, created, **kwargs):
    if created:
        print(f'Movimentação criada: {instance.produto.nome} ({instance.quantidade})')
        produto = instance.produto
        print(f"Antes de atualizar: {produto.quantidade}")
        if instance.tipo == 'E':
            produto.quantidade += instance.quantidade
        elif instance.tipo == 'S':
            produto.quantidade -= instance.quantidade
        print(f"Depois de atualizar: {produto.quantidade}")
        produto.save()
        