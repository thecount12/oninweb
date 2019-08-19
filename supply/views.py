"""
views
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from supply.models import Cartridge
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# @login_required(redirect_field_name='/login')
class CartridgeView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    redirect_field_name = 'next'  # to the proper page.
    model = Cartridge


# @login_required
class CartDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    redirect_field_name = 'next'  # to the proper page.
    model = Cartridge


def add_batch_view():
    pass
