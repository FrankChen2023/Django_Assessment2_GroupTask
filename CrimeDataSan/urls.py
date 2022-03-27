from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('date_search/', views.date_search, name='date_search'),
path('position_search/', views.position_search, name='position_search'),
path('coordinates_search/', views.coordinates_search, name='coordinates_search'),
path('date_result/', views.date_result, name='date_result'),
path('position_result/', views.position_result, name='position_result'),
path('total/', views.total, name='total'),
]