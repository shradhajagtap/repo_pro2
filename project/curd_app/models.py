from django.db import models


class Car(models.Model):
    CAR_NAME = [("bolero", "Bolero"), ("creta", "Creta"), ("kia", "Kia"), ("thar", "Thar")]
    CAR_MODEL = [("old", "Old"), ("new", "New")]
    customer_name = models.CharField(max_length=20)
    car_company = models.CharField(max_length=20)
    car_name_mode = models.CharField(max_length=10, choices=CAR_NAME)
    car_model_mode = models.CharField(max_length=10, choices=CAR_MODEL)
    car_capacity = models.CharField(max_length=20)
    car_cc = models.CharField(max_length=20)

