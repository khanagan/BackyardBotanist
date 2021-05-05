from django.db import models

# Create your models here.

class TaxGroup(models.Model):
    groupId = models.IntegerField(primary_key=True)
    taxGroup = models.CharField(max_length=100)

    class Meta:
        db_table = 'TaxGroup'

class Plant(models.Model):
    plantId = models.IntegerField(primary_key=True)
    commonName = models.CharField(max_length=100)
    scientificName = models.CharField(max_length=100)
#    yearLastDocumented = models.DateTimeField("year")
    yearLastDocumented = models.CharField(max_length=100)
    rankId = models.IntegerField()
    groupId = models.IntegerField()
    #groupId = models.ForeignKey(TaxGroup, on_delete=models.CASCADE)
    subgroupId = models.IntegerField()
    statusId = models.IntegerField()
    
    class Meta:
        db_table = 'Plant'

class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    joinDate = models.DateTimeField()
    numSightings = models.IntegerField()
    
    class Meta:
        db_table = 'User'

class Subgroup(models.Model):
    subgroupId = models.IntegerField(primary_key=True)
    taxSubgroup = models.CharField(max_length=100)
    groupId = models.IntegerField()
    
    class Meta:
        db_table = 'Subgroup'

class Location(models.Model):
    county = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'Location'

class Pictures(models.Model):
    pictureId = models.IntegerField(primary_key=True)
    imageFile = models.ImageField()
    plantId = models.IntegerField()
    userId = models.IntegerField()
    
    class Meta:
        db_table = 'Pictures'

class ConservationRank(models.Model):
    rankId = models.IntegerField(primary_key=True)
    stateRank = models.CharField(max_length=100)
    globalRank = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'ConservationRank'
   
class ListingStatus(models.Model):
    statusId = models.IntegerField(primary_key=True)
    federalStatus = models.CharField(max_length=100)
    stateStatus = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'ListingStatus'
     
class Sighting(models.Model):
    sightingId = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    plantId = models.IntegerField()
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Sighting'

class ChangePassword(models.Model):
    userId = models.IntegerField(primary_key=True)
    oldPass = models.CharField(max_length=100)
    newPass = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'ChangePassword'
    
class PlantLocation(models.Model):
    plantId = models.IntegerField(primary_key=True)
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'PlantLocation'
