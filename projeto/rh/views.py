from django.shortcuts import render
from projeto.rh.forms import FuncionarioForm 

# Create your views here.

def rh(request):
	form = FuncionarioForm(request.POST or None)

	if request.method == 'POST':
		form.save()

	return render(request, 'rh.html', {'form': form})