from django import forms
from .models import Ankieta


class AnkietaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnkietaForm, self).__init__(*args, **kwargs)
        self.fields['wiek'].widget.attrs = {
            'class': 'form-control',
            'min': '1',
            'max': '150'
        }
        self.fields['wzrost'].widget.attrs = {
            'class': 'form-control',
            'min': '50',
            'max': '250'
        }
        self.fields['plec'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['kolor'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Ankieta
        fields = ('wiek', 'wzrost', 'plec', 'kolor')
        labels = {'plec': 'Płeć'}
