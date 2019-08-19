"""
form data for meh
"""
from django import forms
from supply.models import Batch


class AddBatch(forms.ModelForm):
    class Meta:
        model = Batch
