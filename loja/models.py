from django.conf import settings
from django.db import models
from django.utils import timezone


class Produto(models.Model):
    ID = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    em_estoque = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to ='produtos/{}'.format(ID), default=None, blank=True, null=True)

    def publish(self):
        self.save()


class User(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    nivel = models.IntegerField()

    def publish(self):
        self.save()


class Compra(models.Model):
    ID = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through="Quantidade")

    def publish(self):
        self.save()


class Quantidade(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def publish(self):
        self.save()