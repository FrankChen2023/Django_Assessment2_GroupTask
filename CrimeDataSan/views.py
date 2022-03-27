from django.shortcuts import render, get_object_or_404
from .models import CrimeDate, CrimePosition

# Create your views here.

def index(request):
    return render(request, 'index.html')

def date_search(request):
    return render(request, 'date_search.html')

def position_search(request):
    return render(request, 'position_search.html')

def coordinates_search(request, latitude, longitude):
    latitude = str(latitude)
    longitude = str(longitude)
    position_search_rows = CrimePosition.objects.filter(latitude__startwith=latitude, longitude__startwith=longitude)
    return render(request, 'coordinates_search.html', {'position_search_rows' : position_search_rows})

def date_result(request, date):
    Crime_date = CrimeDate.objects.get(date = date)
    return render(request, 'date_result.html', {'Crime_date' : Crime_date})

def position_result(request, position):
    Crime_position = CrimePosition.objects.get(position = position)
    return render(request, 'position_result.html', {'Crime_position' : Crime_position})

def total(request):
    Crime_total_date = CrimeDate.objects.all()
    Crime_total_position = CrimePosition.objects.all()
    return render(request, 'position_result.html', {'Crime_total_date' : Crime_total_date, 'Crime_total_position' : Crime_total_position})