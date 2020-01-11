from django import forms
from .models import Produto
from django.forms.widgets import ClearableFileInput

class ProdutoForm(forms.ModelForm):
	
    class Meta:
        model = Produto
        fields = '__all__'
