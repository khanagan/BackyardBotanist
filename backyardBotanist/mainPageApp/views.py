from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.templatetags import static
from django.shortcuts import get_object_or_404
from .models import User
# Create your views here.

def home(request):
    page = loader.get_template('home.html')
    return HttpResponse(page.render())

def changePassword(request):
    page = loader.get_template('changePassword.html')
    return HttpResponse(page.render())

def invalidUser(request, email):
    page = loader.get_template('invalidUser.html')
    return HttpResponse(page.render())

def databaseSearchPage(request):
    page = loader.get_template('databaseSearchPage.html')
    return HttpResponse(page.render())


