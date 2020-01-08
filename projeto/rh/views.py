from django.shortcuts import render, redirect
from projeto.rh.forms import FuncionarioForm
from . models import Funcionario 

# Create your views here.

def rh(request):
	form = FuncionarioForm(request.POST or None)

	if request.method == 'POST':
		form.save()
		return redirect('/rh')

	return render(request, 'rh.html', {'form': form})



def consulta(request):
	form = Funcionario.objects.all()

	return render(request, 'consulta.html', {'form': form})

def detalhe(request):
	form = Funcionario.objects.all()
	return render(request, 'detalhe.html',{'form': form})