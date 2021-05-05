from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.templatetags import static
from django.shortcuts import get_object_or_404
from django.db import connection
from .models import User, Plant
from .forms import userLoginForm


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
    page = loader.get_template('changePassword.html')
    return HttpResponse(page.render())

def invalidUser(request):
    page = loader.get_template('invalidUser.html')
    return HttpResponse(page.render())

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

def displayReport1(request):
    #plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    plants = Plant.objects.raw('SELECT 1 as id, plantId, commonName, scientificName, yearLastDocumented, rankID, groupID, subgroupID, statusID from Plant limit 10')
    print(plants)
    return render(request, "reportPage1.html", {"Plant": plants})

def displayReport2(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT PlantID, CommonName, ScientificName, YearLastDocumented, Plant.StatusID AS StatusID, FederalListingStatus, StateListingStatus FROM Plant, ListingStatus WHERE Plant.StatusID = ListingStatus.StatusID")
        plantListing = cursor.fetchall()
    #print(plantListing)
    cursor.close()
    return render(request, "reportPage2.html", {"PlantLocation": plantListing})

def displayReport3(request):
    plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    return render(request, "reportPage3.html", {"Plant": plants})

def displayReport4(request):
    plants=Plant.objects.all()
    #plants = Plant.objects.all().values('plantId','commonName','scientificName','yearLastDocumented','rankId','groupId','groupId__taxGroup','subgroupId','statusId')
    return render(request, "reportPage4.html", {"Plant": plants})

