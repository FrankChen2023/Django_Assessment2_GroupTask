from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'visitor'

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Visitor.objects.create(user=instance)
        instance.visitor.save()
    
