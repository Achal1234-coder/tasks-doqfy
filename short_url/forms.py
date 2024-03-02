from django.forms import forms
from . import models

class UrlForm(forms.Form):
    class Meta:
        model = models.Url
        fields = ['original_url']