"""
supply urls
"""

from django.urls import path
from supply.views import CartridgeView
from supply.views import CartDetailView


urlpatterns = [
    path('', CartridgeView.as_view(), name='cartridge-list'),
    path('<int:pk>', CartDetailView.as_view(), name='cart-detail'),
]
