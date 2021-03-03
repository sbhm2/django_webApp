from django import forms

from app.models import App

class FilterForm(forms.Form):
    name   = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Enter product name", "class":"inputField"}), required=False)