# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import  ValidateFormSerializer
from .models import Truck, Storage
from . import logic
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

import logging
logger = logging.getLogger(__name__)

# shapely import.
from shapely.strtree import STRtree
from shapely.geometry import Polygon, Point
import shapely.wkt




# Data output for the template 
def manage_storages(request):
    context = {}
    logger = logging.getLogger(__name__)
    logger.info("ХУЙ")
    storages = Storage.objects.all()
    for str in storages:
        context[str] = list(Truck.objects.filter(is_online=True,storage=str))
    return render(request, 'calc/detail/detail.html',
                {'context': context,
                })

def check_entry_of_point(point,polygon):
        return polygon.contains(point)

def update_storages_data(post_data):
    for str,trucks in post_data['storage_data'].items():
        capacity_Fe = 0
        capacity_SeO2 = 0
        capacity_none_type= 0
        new_capacity_Fe = 0
        new_capacity_SeO2 = 0 
        storage = Storage.objects.get(id = str)
        print(storage.coordinates)
        polygon = shapely.wkt.loads(storage.coordinates)
            
        for id , val in trucks['trucks_data'].items():
            print(val)
            point = Point(val['coordinate_x'],val['coordinate_y'])
            #if check_entry_of_point(point,polygon):
            truck = Truck.objects.get(id=id)
            capacity_Fe += truck.carrying_capacity * truck.percentage_Fe
            capacity_SeO2 += truck.carrying_capacity * truck.percentage_SiO2
            capacity_none_type += truck.carrying_capacity * (1-(truck.percentage_Fe+truck.percentage_SiO2))
            
        new_capacity_Fe = capacity_Fe + storage.capacity * storage.percentage_Fe
        new_capacity_SeO2 = capacity_Fe + storage.capacity * storage.percentage_SiO2
        new_capacity= (new_capacity_Fe + new_capacity_SeO2+(capacity_none_type + (storage.capacity - ((storage.capacity * storage.percentage_Fe) + (storage.capacity * storage.percentage_SiO2)))))
        new_persanage_Fe = new_capacity_Fe/new_capacity
        new_persanage_SeO2 =  new_capacity_SeO2/new_capacity
        storage.capacity = new_capacity
        storage.percentage_SiO2=new_persanage_SeO2
        storage.percentage_Fe=new_persanage_Fe
        storage.save()

        #Storage.objects.get(id = str).update(capacity=new_capacity, percentage_SiO2=new_persanage_SeO2,percentage_Fe=new_persanage_Fe)       

@require_POST
def coordinate_update(request):
    valid_ser = ValidateFormSerializer(data = json.loads(request.POST['data']))
    if valid_ser.is_valid():
        post_data = valid_ser.validated_data   
        print(post_data['storage_data'])
        update_storages_data(post_data)    
    else:
        print(valid_ser.errors)
    #return redirect('calc:manage_storages')
    return JsonResponse({"update": "OK"})
    #return HttpResponseRedirect(reverse('calc:manage_storages'))
