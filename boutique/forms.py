from django import forms
from .models import Produit


class New_produit_F(forms.ModelForm):
	class Meta:
		model = Produit
		fields = '__all__'