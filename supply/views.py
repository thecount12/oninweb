from django.shortcuts import render
from django.views.generic.list import ListView
from supply.models import Cartridge

# Create your views here.


class CartridgeView(ListView):
    model = Cartridge
