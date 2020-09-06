from django import forms
from django.core.exceptions import ValidationError


class URLForm(forms.Form):
    link = forms.CharField(max_length=2500, label=False)
