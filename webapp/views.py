from django.shortcuts import render
from .forms import *
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    try:
        category=Category.objects.all()
        location = Location.objects.values('city')
        sublocation=SubLocation.objects.values('area')
        comibned=list(location)+list(sublocation)
        print('combined====',comibned)
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