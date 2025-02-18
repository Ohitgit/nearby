
from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name='home'),
    path('login',signin,name='login'),
    path('business_list/<str:city>/<str:category>',business_list,name="business_list")
]