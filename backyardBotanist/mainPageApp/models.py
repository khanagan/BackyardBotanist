from django.db import models

# Create your models here.
class Plant(models.Model):
    commonName = models.CharField(max_length=100)
    scientificName = models.CharField(max_length=100)
    yearLastDocumented = models.DateTimeField("year")
    federalListingStatus = models.CharField(max_length=100)

class User(models.Model):
    userId = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    joinDate = models.DateTimeField()
    numSightings = models.IntegerField()

class Group(models.Model):
    groupId = models.IntegerField()
    taxGroup = models.CharField(max_length=100)

class Subgroup(models.Model):
    subgroupID = models.IntegerField()
    taxSubgroup = models.CharField(max_length=100)

class Location(models.Model):
    county = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    stateListingStatus = models.CharField(max_length=100)

class Pictures(models.Model):
    pictureId = models.IntegerField()
    imageFile = models.ImageField()

class ConservationRank(models.Model):
    rankId = models.IntegerField()
    stateStatus = models.CharField(max_length=100)
    globalStatus = models.CharField(max_length=100)