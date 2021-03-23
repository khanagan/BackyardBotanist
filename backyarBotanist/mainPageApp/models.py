from django.db import models

# Create your models here.
class Plant(models.Model):
    commonName = models.CharField(max_length=100)
    scientificName = models.CharField(max_length=100)
    yearLastDocumented = models.DateTimeField("year")
    federalListingStatus = models.CharField(max_length=100)