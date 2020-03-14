from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('finalizar', views.finalizar, name='finalizar'),
    path('add/<ID>', views.add_cart, name='add_cart'),
    path('minhas-compras', views.minhas_compras, name='minhas_compras'),
    path('remove/<ID>', views.remove_item, name='remove_item'),
    path('login', LoginView.as_view(template_name="loja/login.html", redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]