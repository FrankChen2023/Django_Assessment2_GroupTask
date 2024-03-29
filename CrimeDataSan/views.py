from django.shortcuts import render, redirect, get_object_or_404
from .models import CrimeDate, CrimePosition, Visitor
from CrimeDataSan.forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'Crime/index.html')

def date_search(request):
    date_1=[]
    date_2=[]
    date_3=[]
    for day in range(1,10):
        date_1.append('0' + str(day) + '.01.2015')
        date_2.append('0' + str(day) + '.02.2015')
        date_3.append('0' + str(day) + '.03.2015')
    for day in range(10,32):
        date_1.append(str(day) + '.01.2015')
        date_3.append(str(day) + '.03.2015')
    for day in range(10,29):
        date_2.append(str(day) + '.02.2015')
    return render(request, 'Crime/date_search.html', {'date_1':date_1, 'date_2':date_2, 'date_3':date_3})

def position_search(request):
    return render(request, 'Crime/position_search.html')

def coordinates_search(request):
    position_search_rows = CrimePosition.objects.all()
    if request.method=="POST":
        longitude = str(request.POST.get('longitude',''))
        latitude = str(request.POST.get('latitude',''))
        position_search_rows = CrimePosition.objects.filter(latitude__startswith=latitude, longitude__startswith=longitude)
    return render(request, 'Crime/coordinates_search.html', {'position_search_rows' : position_search_rows})

def date_result(request, date):
    Crime_date = CrimeDate.objects.filter(date = date)
    return render(request, 'Crime/date_result.html', {'Crime_date' : Crime_date})

def position_result(request, position):
    Crime_position = CrimePosition.objects.filter(district = position)
    return render(request, 'Crime/position_result.html', {'Crime_position' : Crime_position})

def total(request):
    Crime_total_date = CrimeDate.objects.all()
    Crime_total_position = CrimePosition.objects.all()
    return render(request, 'Crime/total.html', {'Crime_total_date' : Crime_total_date, 'Crime_total_position' : Crime_total_position})

@login_required
def data_edit(request):
    row_date = None
    row_position = None
    if request.method=="POST" and 'id1' in request.POST:
        id = request.POST.get('id1','')
        try:
            row_date = CrimeDate.objects.get(id=id)
            row_position = CrimePosition.objects.get(id=id)
        except:
            pass
    if request.method=="POST" and 'id2' in request.POST:
        id = request.POST.get('id2','')
        try:
            row_date = CrimeDate.objects.get(id=id).delete()
            row_position = CrimePosition.objects.get(id=id).delete()
        except:
            pass
    if request.method=="POST" and 'Id' in request.POST:
        Id = request.POST.get('Id','')
        Date = str(request.POST.get('Date',''))
        DayOfWeek = str(request.POST.get('DayOfWeek',''))
        PdDistrict = str(request.POST.get('PdDistrict',''))
        Address = str(request.POST.get('Address',''))
        Longitude = str(request.POST.get('Longitude',''))
        Latitude = str(request.POST.get('Latitude',''))
        try:
            row_date = CrimeDate.objects.get(id=Id)
            row_position = CrimePosition.objects.get(id=Id)
            row_date.date = row_position.date = [Date, row_date.date][Date=='']
            row_date.weekday = [DayOfWeek, row_date.weekday][DayOfWeek=='']
            row_date.district = row_position.district = [PdDistrict, row_position.district][PdDistrict=='']
            row_date.address = row_position.address = [Address, row_position.address][Address=='']
            row_position.longitude = [Longitude, row_position.longitude][Longitude=='']
            row_position.latitude = [Latitude, row_position.latitude][Latitude=='']
            CrimeDate.objects.filter(id=Id).update(date=row_date.date, weekday=row_date.weekday, 
            district=row_date.district, address=row_date.address)
            CrimePosition.objects.filter(id=Id).update(date=row_position.date,  district=row_position.district, 
            address=row_position.address, longitude=row_position.longitude, latitude=row_position.latitude)
        except:
            CrimeDate.objects.create(id=Id, date=Date, weekday=DayOfWeek, district=PdDistrict, 
            address=Address).save()
            CrimePosition.objects.create(id=Id, date=Date, district=PdDistrict, address=Address, 
            longitude=Longitude, latitude=Latitude).save()
    return render(request, 'Crime/data_edit.html', {'row_date' : row_date, 'row_position' : row_position})

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('/')


