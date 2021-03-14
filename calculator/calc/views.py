# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import  Coordinate_Form
from .models import Truck, Storage
from . import logic

# Data output for the template 
def manage_storages(request, storage_slug=None):
    
    context = {}
    storages = Storage.objects.all()
    for str in storages:
        context[str] = list(Truck.objects.filter(is_online=True,storage=str))
    return render(request, 'calc/detail/detail.html',
                {'context': context,
                })


# Data update on the template 
@require_POST
def coordinate_update(request,truck_id):
    form = Coordinate_Form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        #logic.storage_upload(truck_id=truck_id, cd['quantity'],cd['update'])
    return redirect('cart:cart_detail')