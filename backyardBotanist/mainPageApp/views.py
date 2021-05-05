import datetime

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.templatetags import static
from django.shortcuts import get_object_or_404
from django.db import connection
from django.core.exceptions import *
from .models import User, Plant, TaxGroup, Subgroup, Location, Pictures, ConservationRank, ListingStatus, Sighting, ChangePassword, PlantLocation
from .forms import userLoginForm, userChangePasswordForm, addSightingForm, userCreateAccountForm


# Create your views here.

def home(request):
    #page = loader.get_template('home.html')
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return HttpResponseRedirect('databaseSearchPage.html')
    else:
        form = userLoginForm()
    return render(request, 'home.html', {'form': form})


def changePassword(request):
    #page = loader.get_template('changePassword.html')
    #return HttpResponse(page.render())
    if request.method == 'POST':
        form = userChangePasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            oldPassword = form.cleaned_data['oldPassword']
            newPassword = form.cleaned_data['newPassword']
            with connection.cursor() as cursor:
                cursor.execute('SELECT email, password FROM User WHERE email LIKE "' + email + '" AND password LIKE "' + oldPassword + '"')
                u = cursor.fetchall()
            cursor.close()
            if len(u) != 1:
                return HttpResponseRedirect('invalidUser')
            else:
                User.objects.filter(email=email, password=oldPassword).update(password=newPassword)
            return HttpResponseRedirect('databaseSearchPage')
    else:
        form = userChangePasswordForm()
    return render(request, 'changePassword.html', {'form': form})

def createAccount(request):
    if request.method == 'POST':
        form = userCreateAccountForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmPassword = form.cleaned_data['confirmPassword']
            with connection.cursor() as cursor:
                cursor.execute('SELECT email, password FROM User WHERE email LIKE "' + email + '" AND password LIKE "' + password + '"')
                u = cursor.fetchall()
            cursor.close()
            if len(u) > 0:
                return HttpResponseRedirect('invalidUser')
            else:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT max(UserID) FROM User')
                    u2 = cursor.fetchall()
                cursor.close()
                User.objects.create(email=email, password=password, userId=(u2[0][0] + 1), numSightings=0, joinDate=datetime.today())
            return HttpResponseRedirect('databaseSearchPage')
    else:
        form = userCreateAccountForm()
    return render(request, 'createAccount.html', {'form': form})

def invalidUser(request):
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

def databaseSearchPage(request):
    page = loader.get_template('databaseSearchPage.html')
    if request.method == "POST":
        form = userLoginForm(request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #Verifies existance of user, if exists proceed to view DB, else display invalid User
            with connection.cursor() as cursor:
                cursor.execute('SELECT email, password FROM User WHERE email LIKE "' + email + '" AND password LIKE "' + password + '"')
                u = cursor.fetchall()
            cursor.close()
            if len(u) != 1:
                return HttpResponseRedirect('invalidUser')
    return HttpResponse(page.render())

def displayReport2(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT PlantID, CommonName, ScientificName, YearLastDocumented, Plant.StatusID AS StatusID, FederalListingStatus, StateListingStatus FROM Plant, ListingStatus WHERE Plant.StatusID = ListingStatus.StatusID")
        plantListing = cursor.fetchall()
    #print(plantListing)
    cursor.close()
    return render(request, "reportPage2.html", {"PlantLocation": plantListing})

def displayReport3(request):
    plants=Plant.objects.all()
    return render(request, "reportPage3.html", {"Plant": plants})

def displayReport4(request):
    plants=Plant.objects.all()
    return render(request, "reportPage4.html", {"Plant": plants})

