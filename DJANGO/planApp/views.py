from django.shortcuts import render
from .models import SoilMoistureReading

# Create your views here.
def moisture_list(request):
    soil_readings = SoilMoistureReading.objects.all().order_by('-timestamp')
    return render(request, 'planApp/moisture_list.html', {'soil_readings': soil_readings})

