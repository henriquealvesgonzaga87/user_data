from pyexpat import model
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'bday', 'tax_number']
