from django import forms
from . models import Funcionario
from django.forms import ModelForm

class FuncionarioForm(ModelForm):

	class Meta:
		model = Funcionario
		fields = "__all__"