from django.shortcuts import render

def produtos(request):
    return render(request, 'loja/produtos.html', {})