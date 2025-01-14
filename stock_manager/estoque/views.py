from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'Produtos': produtos})


