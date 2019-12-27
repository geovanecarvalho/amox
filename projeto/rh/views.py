from django.shortcuts import render

# Create your views here.

def rh(request):
	return render(request, 'rh.html')