from django.urls import path
from . import views

urlpatterns = [

    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), #le path du viue seting 
    path('mytest/', views.mytest, name='mytest'), #le path du viue de mytest 
    path('Home/', views.Home, name='Home'), #le path du viue de Accueill 

    
    

   
]