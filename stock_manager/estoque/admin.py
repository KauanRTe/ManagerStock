from django.contrib import admin
from .models import Categoria, Produto, Movimentacao
# Register your models here.

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Movimentacao)

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data')
    fields = ('produto', 'tipo', 'quantidade', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('produto_nome',)
    

