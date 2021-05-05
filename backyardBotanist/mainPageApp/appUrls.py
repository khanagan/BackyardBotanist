from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('invalidUser', views.invalidUser, name='invalidUser'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('displayReport1raw', views.displayReport1raw, name='displayReport1raw'),
    path('displayReport1ORM', views.displayReport1ORM, name='displayReport1ORM'),
    path('displayReport2', views.displayReport2, name='displayReport2'),
    path('displayReport3', views.displayReport3, name='displayReport3'),
    path('displayReport4', views.displayReport4, name='displayReport4'),
    path('addSighting', views.addSighting, name='addSighting'),
    path('addedSighting', views.addedSighting, name='addedSighting'),
    path('databaseSearchPage', views.databaseSearchPage, name='databaseSearchPage'),
    path('groupSearchPage', views.groupSearchPage, name='groupSearchPage'),
]
