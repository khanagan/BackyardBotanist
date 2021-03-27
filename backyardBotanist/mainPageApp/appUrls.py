from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('invalidUser', views.invalidUser, name='invalidUser'),
    path('databaseSearchPage', views.databaseSearchPage, name='databaseSearchPage'),
]