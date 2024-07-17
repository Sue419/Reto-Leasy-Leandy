
# Create your models here.
from django.db import models

class DataTaxi(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_number = models.CharField(max_length=20)
    contract_start = models.DateField()
    weekly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_plate = models.CharField(max_length=20)