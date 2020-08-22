from django import forms


class URLForm(forms.Form):
    link = forms.CharField(max_length=2500, label=False)
