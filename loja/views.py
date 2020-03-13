from django.shortcuts import render, redirect
from .models import Produto, User
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