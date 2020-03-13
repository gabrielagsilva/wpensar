from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', LoginView.as_view(template_name="loja/login.html", redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]