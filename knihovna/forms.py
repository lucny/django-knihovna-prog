from django import forms
from .models import Kniha


class KnihaForm(forms.ModelForm):

    class Meta:
        model = Kniha
        fields = ['titul', 'obsah', 'pocet_stran',
                  'rok_vydani', 'autori', 'obalka',
                  'vydavatelstvi', 'zanry']
        widgets = {
            'titul': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej titul knihy'}),
            'obsah': forms.Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej obsah knihy'}),
            'pocet_stran': forms.NumberInput(attrs={'class': 'form-control',
                                           'value': '200', 'min': 10, 'max': 2000}),
        }
        labels = {
            'titul': 'Titul knihy',
            'obsah': 'Stručný obsah knihy',
            'pocet_stran': 'Počet stran',
        }
        required = {
            'title': True,
            'obsah': False,
            'pocet_stran': False,
        }
