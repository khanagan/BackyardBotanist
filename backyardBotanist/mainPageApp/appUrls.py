from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('invalidUser', views.invalidUser, name='invalidUser'),
    path('displayData', views.displayData, name='displayData'),
]
