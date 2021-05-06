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
from .forms import userLoginForm, userChangePasswordForm, addSightingForm, userCreateAccountForm, deleteAccountForm, \
    searchPlantForm,  groupForm, subGroupForm


# Create your views here.

def home(request):
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
            else:
                return HttpResponseRedirect('databaseSearchPage')
    else:
        form = userLoginForm()
    return render(request, 'home.html', {'form': form})


def changePassword(request):
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

def admin(request):
    if request.method == 'POST':
        form = deleteAccountForm(request.POST)
        if form.is_valid():
            userID = form.cleaned_data['userID']
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM User WHERE userID = ' + str(userID))
                u = cursor.fetchall()
            cursor.close()
            if len(u) != 1 or u[0][1] == "admin@email.com":
                return HttpResponseRedirect('invalidUser')
            else:
                User.objects.filter(userId=userID).delete()
            return HttpResponseRedirect('admin')
    else:
        form = deleteAccountForm()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT UserID, email, joinDate, numSightings FROM User")
        UserList = cursor.fetchall()
    cursor.close()
    return render(request, 'admin.html', {'form': form, "UserList": UserList})

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
    #page = loader.get_template('databaseSearchPage.html')
    if request.method == 'POST':
        form = searchPlantForm(request.POST)
        if form.is_valid():
            plant = form.cleaned_data['plant']
            with connection.cursor() as cursor:
                cursor.execute('SELECT PlantID, CommonName, ScientificName, YearLastDocumented FROM Plant WHERE CommonName LIKE "'+ plant + '" OR ScientificName LIKE "' + plant + '"')
                p = cursor.fetchall()
            cursor.close()
            return render(request, "databaseSearchPage.html", {"PlantList": p, 'form': form})
    else:
        form = searchPlantForm()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT PlantID, CommonName, ScientificName, YearLastDocumented FROM Plant")
        plantList = cursor.fetchall()
    cursor.close()
    return render(request, "databaseSearchPage.html", {"PlantList": plantList, 'form': form})

def displayReport2(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT PlantID, CommonName, ScientificName, YearLastDocumented, Plant.StatusID AS StatusID, FederalListingStatus, StateListingStatus FROM Plant, ListingStatus WHERE Plant.StatusID = ListingStatus.StatusID")
        plantListing = cursor.fetchall()
    #print(plantListing)
    cursor.close()
    return render(request, "reportPage2.html", {"PlantLocation": plantListing})


def displayReport3(request):
    groupNo = 3
    with connection.cursor() as cursor:
        sql = ('SELECT CommonName, ScientificName '
               'FROM TaxGroup RIGHT JOIN Plant ON Plant.groupId = TaxGroup.groupId '
               'WHERE TaxGroup.groupId = %s ')
        cursor.execute(sql, groupNo)
        groupListing = cursor.fetchall()
    cursor.close()
    return render(request, "reportPage3.html", {"GroupList": groupListing})

def groupSearchPage(request):
    if request.method == 'POST':
        form = groupForm(request.POST)
       # if form.is_valid():
       #     groupNo = form.cleaned_data['GroupNo.']
    return render(request, 'groupSearchPage.html')

def displayReport4(request):
    groupNo = 3
    with connection.cursor() as cursor:
        sql = ('SELECT CommonName, ScientificName '
               'FROM Subgroup RIGHT JOIN Plant ON Plant.groupId = Subgroup.groupId '
               'WHERE Subgroup.groupId = %s ')
        cursor.execute(sql, groupNo)
        groupListing = cursor.fetchall()
    cursor.close()
    return render(request, "reportPage4.html", {"GroupList": groupListing})

def subGroupSearchPage(request):
    if request.method == 'POST':
        form = groupForm(request.POST)
       # if form.is_valid():
       #     groupNo = form.cleaned_data['GroupNo.']
    return render(request, 'subGroupSearchPage.html')

