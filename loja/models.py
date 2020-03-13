from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Produto(models.Model):
    ID = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    em_estoque = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to ='produtos', default=None, blank=True, null=True)

    def publish(self):
        self.save()


class Compra(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    produtos = models.ManyToManyField(Produto, through="Quantidade")

    def publish(self):
        self.save()


class Quantidade(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def publish(self):
        self.save()