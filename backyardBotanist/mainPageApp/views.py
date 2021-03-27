from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from mainPageApp.models import Plant
from mainPageApp.models import User
from mainPageApp.models import Group
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

def displayData(request):
    results=Plant.objects.all()
    return render(request, "index.html", {"Plant": results})
