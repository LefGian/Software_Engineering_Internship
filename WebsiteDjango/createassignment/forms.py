import imp
from django import forms
from startsite.models import *



class AufgabeErstellenForm(forms.ModelForm):

    class Meta:
        model = Aufgabe
        fields =['name', 'aufgabenstellung', 'loesung', 'user', 'schwierigkeit', 'zeit', 'themengebiet']
