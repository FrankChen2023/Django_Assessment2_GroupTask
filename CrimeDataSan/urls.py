from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'Crime'

urlpatterns = [
        path('', views.index, name='index'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('date_search/', views.date_search, name='date_search'),
        path('position_search/', views.position_search, name='position_search'),
        path('coordinates_search/', views.coordinates_search, name='coordinates_search'),
        path('date_result/<str:date>/', views.date_result, name='date_result'),
        path('position_result/<str:position>/', views.position_result, name='position_result'),
        path('total/', views.total, name='total'),
        path('signup/', views.signup, name='signup'),
]