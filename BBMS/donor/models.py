from django.db import models


class Donor(models.Model):
    name = models.CharField(max_length=50 , blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=15,blank=False)
    age = models.PositiveIntegerField()
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    mobile_no = models.PositiveIntegerField(blank=False)
    Bgroup = models.CharField(max_length=3)

class Blood_Donate(models.Model):
    donor = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)
