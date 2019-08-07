"""
views
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from supply.models import Cartridge

# Create your views here.


class CartridgeView(ListView):
    model = Cartridge


class CartDetailView(DetailView):
    model = Cartridge
