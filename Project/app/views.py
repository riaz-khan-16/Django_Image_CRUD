from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
 
# Create your views here.
 
 
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')

def display_hotel_images(request):
 
    if request.method == 'GET':
 
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
    
        template = loader.get_template('display_hotel_images.html')
        context = {
            'hotel_images': Hotels
        }
        return HttpResponse(template.render(context, request))
    
def delete(request, id):
            hotel = Hotel.objects.get(id=id)
            hotel.delete()   
            return HttpResponse('successfully Deleted') 

