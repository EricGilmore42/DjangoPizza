from django import forms

from .models import *

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}

        widgets = {'text': forms.Textarea(attrs={'cols':80})}