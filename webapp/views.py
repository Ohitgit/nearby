from django.shortcuts import render
from .forms import *
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
# Create your views here.

def home(request):
    try:
        
        category=Category.objects.all()
        
        location = Location.objects.values('city')
        sublocation=SubLocation.objects.values('area')
        comibned=list(location)+list(sublocation)
    except Category.DoesNotExist:
          category=None
    return render(request,'webapp/home.html',{'category':category,'comibned':comibned})

def signin(request):
    fm=LoginForm()
    if request.method == "POST":
       
        form = LoginForm(request.POST)
        # print('fomr',form)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password=form.cleaned_data['password']
            user = authenticate(request,username=mobile,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/')

    return render(request,'webapp/login.html',{'fm':fm})


def business_list(request,city,categorys):
     print(city,'============')
     category=Category.objects.all()
     location = Location.objects.values('city')
     sublocation=SubLocation.objects.values('area')
     comibned=list(location)+list(sublocation)
     if city != 'null' and categorys != 'null':
        business_list1=Business_Detalies.objects.filter(Q(category__name=categorys) or Q(location__location__city=city) or Q(location__area=city) )
        print('business_list',business_list1)
        return render(request,'webapp/business_list.html',{'business_list1':business_list1,'category':category,'comibned':comibned})
     else:
         return render(request,'webapp/404.html')


def business_detalies(request,slug):
     category=Category.objects.all()
     
     location = Location.objects.values('city')
     sublocation=SubLocation.objects.values('area')
     comibned=list(location)+list(sublocation)
     business_slug=Business_Detalies.objects.get(slug=slug)
     return render(request,'webapp/business_detalies.html',{'category':category,'comibned':comibned})