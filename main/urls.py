from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-f3/', views.about_f3, name='about_f3'),
    path('paulding-region/', views.paulding_region, name='paulding_region'),
    path('contact/', views.contact, name='contact'),
] 