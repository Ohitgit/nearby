
from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name='home'),
    path('login',signin,name='login'),
    path('business_list/<str:city>/<str:categorys>',business_list,name="business_list"),
    path('business_detalies/<str:slug>',business_detalies,name="business_detalies"),
    path('enquiry',enquiry,name='enquiry'),
    path('page',page,name='page')
]