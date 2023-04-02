from django.db import models

# Create your models
class Patient(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField()
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    mobile_no = models.PositiveIntegerField(blank=False)
    Bgroup = models.CharField(max_length=3)
    # units = models.PositiveIntegerField()
    # status = models.CharField(max_length=50, default='Pending')