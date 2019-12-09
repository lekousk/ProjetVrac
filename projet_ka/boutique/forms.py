from django import forms
from .models import Produit

class DateInput(forms.DateInput):
    input_type = 'date'

class NewProduitForm(forms.ModelForm):
	#error_css_class = 'error'
	#required_css_class = 'required'

	class Meta:
		model = Produit
		fields = '__all__'
		widgets = {
		'date_saisie' : DateInput(),
		'date_der_modif' : DateInput(),
		}