from django.db import models

# Create your models here.

class Funcionario(models.Model):
	nome = models.CharField(max_length=150)
	sexo = models.CharField(max_length=1)
	estado_civil = models.CharField(max_length=50)
	rg = models.CharField(max_length=12)
	cpf = models.CharField(max_length=11)
	fone = models.CharField(max_length=11)
	celular = models.CharField(max_length=12)
	funcao = models.CharField(max_length=50)
	admissao = models.DateField(auto_now=False)
	salario = models.DecimalField(max_digits=10, decimal_places=2)
	refeicao = models.DecimalField(max_digits=10, decimal_places=2)
	passagem = models.DecimalField(max_digits=10, decimal_places=2)
	cep = models.CharField(max_length=12)
	endereco = models.TextField()
	pais = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	foto = models.FileField(upload_to="media/foto/", blank=True)

	def __str__(self):
		return self.nome

class Entrada(models.Model):
	entrada = models.DateTimeField(auto_now_add=False)
	funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Saida(models.Model):
	saida = models.DateTimeField(auto_now_add=False)
	funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

