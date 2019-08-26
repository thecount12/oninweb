"""
form data for meh
"""
from django import forms
from supply.models import Batch


class AddBatch(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_name', 'distillate', 'terpene_type', 'thc',
                  'cbd', 'cartridge_type', 'quantity', 'delivery_for',
                  'sold', 'paid']

