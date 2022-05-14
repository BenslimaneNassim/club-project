from django.forms import ModelForm, widgets
from .models import Inscription, Message_contact
from django import forms

class InscriptionForm(ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'
        exclude = ['accepted']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'name-class','placeholder':'Nom *'}),
            'first_name' : forms.TextInput(attrs={'class':'name-class','placeholder':'Prénom *'}),
            'date_naissance' : forms.DateInput(attrs={'class':'name-class','placeholder':'Naissance* (YYYY-MM-JJ)'}),
            'email' : forms.EmailInput(attrs={'class':'name-class','placeholder':'Email (optionel)'}),
            'sexe' : forms.Select(attrs={'class':'sexe-class','placeholder':'Sexe*'}),
            'phone' : forms.TextInput(attrs={'class':'name-class','placeholder':'Numero* (+213...)'}),
            'scan_1' : forms.FileInput(attrs={'id':'extrait-class','class':'extrait-class'}),
            'image' : forms.FileInput(attrs={'id':'image-class','class':'image-class'}),
            'scan_2' : forms.FileInput(attrs={'id':'scan-2-class','class':'scan-2-class'}),
            'scan_3' : forms.FileInput(attrs={'id':'scan-3-class','class':'scan-3-class'}),
        }
class MessageForm(ModelForm):
    class Meta:
        model = Message_contact
        fields = '__all__'
