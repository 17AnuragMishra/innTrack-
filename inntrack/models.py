from django.db import models

# Create your models here.
# models.py

class Shipment(models.Model):
    member_id = models.CharField(max_length=100)
    order_number = models.CharField(max_length=100)
    tracking_id = models.CharField(max_length=10)
    priority = models.IntegerField()
    current_location = models.CharField()
    destination = models.CharField(max_length=100)
    delivery_date = models.IntegerField()

