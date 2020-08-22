from django import forms


class URLForm(forms.Form):
    link = forms.URLField(max_length=2500, label=False)
