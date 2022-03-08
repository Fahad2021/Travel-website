from django.contrib import admin
from django.urls import path,include
from travel import views

urlpatterns = [
    path('',views.home,name='home'),
    path('package/',views.package,name='package'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('condition/',views.condition,name='condition'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register')
  
]