# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import  Coordinate_Form
from .models import Truck, Storage
from . import logic
    
def manage_storages(request, storage_slug=None):
    storage = None
    storages = Storage.objects.all()
    trucks = Truck.objects.filter(is_online=True)
    
    if storage_slug:
        storage = get_object_or_404(Storage, slug=storage_slug)
        trucks = trucks.filter(storage=storage)

    return render(request, 'calc/detail/detail.html',
                {'storage': storage,
                'storages': storages,
                'trucks': trucks})


@require_POST
def coordinate_update(request):
    form = Coordinate_Form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        logic.storage_upload(cd['quantity'],cd['update'])
    return redirect('cart:cart_detail')