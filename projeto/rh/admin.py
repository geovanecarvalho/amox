from django.contrib import admin
from . models import Funcionario, Entrada, Saida
# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Entrada)
admin.site.register(Saida)

