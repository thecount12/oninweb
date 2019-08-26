"""
views
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from supply.models import Cartridge
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from supply.models import Batch
from supply.forms import AddBatch
from supply.models import Cartridge
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


def add_batch_view(request):
    # user = User.objects.get(pk=pk)
    # batch = get_object_or_404(Batch, pk=pk)
    blah = Cartridge.objects.all()
    print("all cartridge")
    print(blah)
    print("end cartridge")
    if request.method == 'POST':
        form = AddBatch(request.POST)
        if form.is_valid():
            cartridge = request.POST.get('cartridge_type')  # list jupiter or kshb either 1 or 2
            quantity = request.POST.get('quantity')  # form number
            print("quantity as posted: {}".format(quantity))
            pk = "cartridge_type id {}".format(int(cartridge) - 1)  # pk accurate list id -1
            print("pk is {}".format(pk))
            pk_qty = blah[int(cartridge)-1].quantity  # pk quantity
            print("pk quantity {}".format(pk_qty))
            bazinga = pk_qty - int(quantity)  # adjusted number
            print("subtract {}".format(bazinga))
            zoom = Cartridge.objects.get(id=cartridge)
            zoom.quantity = (pk_qty - int(quantity))
            zoom.save()
            print("zoom")
            print(zoom)
            print("end zoom")
            batches = form.save(commit=False)
            batches.save()
            return redirect('/thanks/')
    else:
        form = AddBatch()
    return render(request, 'addbatch.html', {'form': form})
