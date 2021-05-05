from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.templatetags import static
from django.shortcuts import get_object_or_404
from django.db import connection
from django.core.exceptions import *
from .models import User, Plant, TaxGroup, Subgroup, Location, Pictures, ConservationRank, ListingStatus, Sighting, ChangePassword, PlantLocation
from .forms import userLoginForm, userChangePasswordForm, addSightingForm


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

def displayReport1raw(request):
    plants = Plant.objects.raw('select 1 as id, plantId, commonName, rankId, groupId, subgroupId, statusId from Plant order by yearLastDocumented desc limit 10')
    return render(request, "reportPage1raw.html", {"Plant": plants})

def displayReport1ORM(request):
    plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','subgroupId','statusId').order_by('-yearLastDocumented')[:10]
    return render(request, "reportPage1ORM.html", {"Plant": plants})

def addSighting(request):
    if request.method == 'POST':
        form = addSightingForm(request.POST)
        if form.is_valid():
            sightingid = form.cleaned_data['sightingid']
            userid = form.cleaned_data['userid']
            plantid = form.cleaned_data['plantid']
            county = form.cleaned_data['county']
            state = form.cleaned_data['state']
            row = Sighting(sightingId = sightingid, userId = userid, plantId = plantid, county = county, state = state)
            row.save()
            return HttpResponseRedirect('addedSighting')
    else: 
        form = addSightingForm()
    return render(request, 'addSighting.html', {'form': form})

def addedSighting(request):
#    page = loader.get_template('addedSighting.html')
#    if request.method == 'POST':
#        form = addSightingForm(request.POST)
#        print(form)
#        if form.is_valid():
#            sightingid = form.cleaned_data['sightingid']
#            userid = form.cleaned_data['userid']
##            plantid = form.cleaned_data['plantid']
#            county = form.cleaned_data['county']
#            state = form.cleaned_data['state']
    sightings = Plant.objects.all()         
    return render(request, 'addedSighting.html', {'sighting':sightings})


def displayReport2(request):
    plants=Plant.objects.all()
    return render(request, "reportPage2.html", {"Plant": plants})

def displayReport3(request):
    plants=Plant.objects.all()
    return render(request, "reportPage3.html", {"Plant": plants})

def displayReport4(request):
    plants=Plant.objects.all()
    return render(request, "reportPage4.html", {"Plant": plants})

