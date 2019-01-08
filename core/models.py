from django.db import models
from django.conf import settings
import datetime


class Tema(models.Model):
    DEFAULT_PK = 1
    nome = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10,decimal_places=2)
    cor_toalha = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Temas'
        verbose_name = 'Tema'

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    DEFAULT_PK = 1
    nome = models.CharField(max_length=50)
    data = models.DateField(default=datetime.date.today)
    telefone = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Clientes'
        verbose_name = 'Cliente'


    def __str__(self):
        return self.nome


class Item(models.Model):
    tema = models.ForeignKey(Tema, default=Tema.DEFAULT_PK, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()


    class Meta:
        verbose_name_plural = 'Itens'
        verbose_name = 'Item'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Endereços'
        verbose_name = 'Endereço'

    def __str__(self):
        return self.logradouro


class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, default=Cliente.DEFAULT_PK, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, primary_key=True)
    tema = models.ForeignKey(Tema, default=Tema.DEFAULT_PK, on_delete=models.CASCADE)

    data_festa = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    valor_cobrado = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name_plural = 'Aluguéis'
        verbose_name = 'Aluguel'

    def __str__(self):
        return 'Aluguel para '+str(self.cliente)