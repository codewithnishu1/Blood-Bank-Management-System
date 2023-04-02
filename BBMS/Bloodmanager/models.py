from django.db import models

# Create your models here.
from email.policy import default
from django.db import models

# Create your models here.
class admini(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password=models.CharField(max_length=50)

class Donation(models.Model):
    name = models.CharField(max_length=50 , blank=True)
    email = models.CharField(max_length=100)
    units = models.PositiveIntegerField()
    Bgroup = models.CharField(max_length=3)
    status = models.CharField(max_length=50, default='Pending')
    date = models.DateField(auto_now=True)

class Blood_request(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100)
    Bgroup = models.CharField(max_length=3)
    units = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='Pending')
    date = models.DateField(auto_now=True)