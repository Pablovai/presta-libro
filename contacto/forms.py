from django import forms
from .models import ContactoPrincipal


class HumoForm(forms.ModelForm):

    class Meta:
        model = ContactoPrincipal
        fields = ['first_name', 'email', 'coments']


