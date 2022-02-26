from django.core import validators
from django import forms
from .models import ContactModel

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields  = '__all__'

        widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'address':forms.Textarea(attrs={'class':'form-control'}),

   'mobile_no': forms.NumberInput( attrs={'class':'form-control'}),
  }






