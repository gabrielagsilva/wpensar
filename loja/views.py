from django.shortcuts import render, redirect
from .models import Produto, User, Compra, Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/produtos.html', {'produtos':produtos})


def cadastro(request):
    user = request.user
    if user.is_authenticated:
        return redirect('produtos')

    erro = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        else:
            return render(request, 'loja/cadastro.html', {'form':form})
    
    form = UserCreationForm()
    return render(request, 'loja/cadastro.html', {'form':form})


def carrinho(request):
    pedidos = {}
    total = 0
    if 'cart' in request.session:
        for ID, qt in request.session['cart'].items():
            produto = Produto.objects.get(ID=ID)
            pedidos[ID] = { 'titulo': produto.titulo,
                            'valor': produto.valor*qt,
                            'quantidade': qt}
            total += produto.valor*qt

    return render(request, 'loja/carrinho.html', {'pedidos':pedidos, 'total': total})


def add_cart(request, ID):
    if 'cart' in request.session:
        if ID in request.session['cart']:
            request.session['cart'][ID] += 1
        else:
            request.session['cart'][ID] = 1
        request.session.modified = True
    else:
        request.session['cart'] = {ID: 1}
    
    return redirect('carrinho')


def remove_item(request, ID):
    request.session['cart'][ID] -= 1
    if request.session['cart'][ID] == 0:
        del request.session['cart'][ID]
    request.session.modified = True
    
    return redirect('carrinho')


def finalizar(request):
    user = request.user
    if user.is_authenticated:
        compra = Compra.objects.create(user = user, total=0)
        total = 0
        for ID, qt in request.session['cart'].items():
            p = Produto.objects.get(ID=ID)
            produto = Item.objects.create(
                produto = p,
                quantidade = qt,
                valor = p.valor*qt
            )
            total += p.valor*qt
            compra.produtos.add(produto)
        compra.total = total
        compra.save()
        return redirect('minhas_compras')
    else:
        return redirect('login')


def minhas_compras(request):
    user = request.user
    if user.is_authenticated:
        compras = Compra.objects.all().filter(user=user)
        return render(request, 'loja/minhas-compras.html', {'compras':compras})
    else:
        return redirect('produtos')