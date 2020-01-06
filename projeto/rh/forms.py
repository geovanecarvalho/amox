from django import forms
from . models import Funcionario
from django.forms import ModelForm

class FuncionarioForm(ModelForm):

	class Meta:
		model = Funcionario
		fields = ('nome', 'sexo', 'estado_civil',
				  'rg', 'cpf', 'fone', 'celular',
				  'funcao', 'admissao', 'salario',
				  'refeicao', 'passagem', 'email', 'cep',
				  'endereco', 'pais', 'estado' )


		erros_mesages ={
			"nome": {'Este campo é obrigatorio'},

		}