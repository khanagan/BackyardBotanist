from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from mainPageApp.models import Plant
from mainPageApp.models import User
from mainPageApp.models import TaxGroup
from mainPageApp.models import Subgroup
from mainPageApp.models import Subgroup
from mainPageApp.models import Location
from mainPageApp.models import Pictures
from mainPageApp.models import ConservationRank
from mainPageApp.models import ListingStatus
from mainPageApp.models import Sighting
from mainPageApp.models import ChangePassword
from mainPageApp.models import PlantLocation

# Create your views here.

def home(request):
    page = loader.get_template('home.html')
    return HttpResponse(page.render())

def changePassword(request):
    page = loader.get_template('changePassword.html')
    return HttpResponse(page.render())

def invalidUser(request):
   # if
    page = loader.get_template('invalidUser.html')
    return HttpResponse(page.render())

def displayReport1(request):
    #plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    plants = Plant.objects.raw('SELECT 1 as id, plantId, commonName, scientificName, yearLastDocumented, rankID, groupID, subgroupID, statusID from Plant limit 10')
    return render(request, "reportPage1.html", {"Plant": plants})

def displayReport2(request):
    plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    return render(request, "reportPage2.html", {"Plant": plants})

def displayReport3(request):
    plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    return render(request, "reportPage3.html", {"Plant": plants})

def displayReport4(request):
    plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    return render(request, "reportPage4.html", {"Plant": plants})

