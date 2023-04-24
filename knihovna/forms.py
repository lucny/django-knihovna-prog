from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, ButtonHolder
from django import forms
from .models import Kniha


class KnihaForm(forms.ModelForm):
    next = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = Kniha
        fields = ['titul', 'obsah', 'pocet_stran',
                  'rok_vydani', 'autori', 'obalka',
                  'vydavatelstvi', 'zanry', 'editor']
        widgets = {
            'titul': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej titul knihy'}),
            'obsah': forms.Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej obsah knihy'}),
            'pocet_stran': forms.NumberInput(attrs={'class': 'form-control',
                                           'value': '200', 'min': 10, 'max': 2000}),
            'autori': forms.SelectMultiple(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej jednoho nebo více autorů'}),
            'zanry': forms.SelectMultiple(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej jeden nebo více žánrů'}),
            'vydavatelstvi': forms.Select(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej jedno vydavatelství'}),
            'rok_vydani': forms.NumberInput(attrs={'class': 'form-control',
                                           'value': '2023', 'min': 1000, 'max': 2023}),
            'obalka': forms.ClearableFileInput(attrs={'class': 'form-control',
                                           'placeholder': 'Vlož obrázek'}),
            'editor': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }
        labels = {
            'titul': 'Titul knihy',
            'obsah': 'Stručný obsah knihy',
            'pocet_stran': 'Počet stran',
            'autori': 'Autoři knih',
            'zanry': 'Žánry',
            'vydavatelstvi': 'Vydavatelství',
            'rok_vydani': 'Vydání',
            'obalka': 'Obálka',
        }
        required = {
            'title': True,
            'obsah': False,
            'pocet_stran': False,
            'autori': True,
            'zanry': False,
            'vydavatelstvi': False,
            'vydani': False,
            'obalka': False,
        }

    def __init__(self, *args, **kwargs):
        super(KnihaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Fieldset(
                'Informace o knize',
                'titul',
                'obsah',
                'pocet_stran',
                'autori',
                'zanry',
                'vydavatelstvi',
                'rok_vydani',
                'obalka',
                'editor',
                'next',
            ),
            FormActions(
                ButtonHolder(
                    Submit('submit', 'Uložit', css_class='btn-primary mr-2'),
                    Submit('cancel', 'Storno', css_class='btn-secondary'),
                    css_class='d-flex'
                )
            ),
        )

