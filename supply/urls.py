
from django.conf.urls import url

from supply.views import CartridgeView
from django.urls import path

urlpatterns = [
    path('cartridgeview/', CartridgeView.as_view(), name='cartridge-list'),
]
