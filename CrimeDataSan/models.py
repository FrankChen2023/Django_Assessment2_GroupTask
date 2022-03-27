from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class CrimeDate(models.Model):
    date = models.TextField()
    weekday = models.TextField()
    district = models.TextField()
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date, self.weekday, self.district, self.address

class CrimePosition(models.Model):
    district = models.TextField()
    address = models.TextField()
    date = models.TextField()
    longitude = models.TextField()
    latitude = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.district, self.address, self.date, self.longitude, self.latitude