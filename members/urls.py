from django.urls import path
from . import views

'''
url is how we create link paths for each page
'''
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('members/testing/', views.testing, name='testing'),
]
