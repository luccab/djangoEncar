from django.db import models

# Create your models here.
class Users(models.Model):
    household_income = models.CharField(max_length=200)
    type_of_housing = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    geography = models.CharField(max_length=200)


class Cars(models.Model):
    consumer_budget = models.IntegerField(default=0)
    brand_preference = models.CharField(max_length=200)
    type_of_car = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    transmission_engine = models.CharField(max_length=200)
    mileage = models.CharField(max_length=200)
    safety_rating = models.CharField(max_length=200)
    maintenance = models.CharField(max_length=200)


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)