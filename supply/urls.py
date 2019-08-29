"""
supply urls
"""

from django.urls import path
from supply.views import CartridgeView
from supply.views import CartDetailView
from supply.views import add_batch_view
from supply.views import BatchView


urlpatterns = [
    path('', CartridgeView.as_view(), name='cartridge-list'),
    path('<int:pk>', CartDetailView.as_view(), name='cart-detail'),
    path('addbatch/', add_batch_view, name='addbatch'),
    path('batchview/', BatchView.as_view(), name='batch-view'),
]

