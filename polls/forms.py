from django import forms
from .models import board

class boardForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

class boardModelForm(forms.ModelForm):
    class Meta:
        model = board
        fields = '__all__'