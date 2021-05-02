from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('invalidUser', views.invalidUser, name='invalidUser'),
    path('displayReport1', views.displayReport1, name='displayReport1'),
    path('displayReport2', views.displayReport2, name='displayReport2'),
    path('displayReport3', views.displayReport3, name='displayReport3'),
    path('displayReport4', views.displayReport4, name='displayReport4'),
]
