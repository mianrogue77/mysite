from django import forms
from .models import Elemento, Efecto

# Form para el CRUD del objeto 'Elemento'
class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ['nombre', 'habilitado']

# Form para el CRUD del objeto 'Efecto'
class EfectoForm(forms.ModelForm):
    class Meta:
        model = Efecto
        fields = ['element_one', 'key_word', 'element_two']