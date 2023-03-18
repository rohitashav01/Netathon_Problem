from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from Bank.forms import AppUserForm
from .models import ProfileUser,BloodCamp

def home_page(request):
    return render(request,'home.html',{})

def add_user(request):
    form = AppUserForm()
    if request.method == 'POST':
            form = AppUserForm(request.POST)
            print(request.POST)
            # username = request.POST.get('username')
            # email = request.POST.get('email')
            # age = request.POST.get('age')
            # gender = request.POST.get('gender')
            # blood_type = request.POST.get('blood_type')
            # password = request.POST.get('password')
            print(request.POST['password'])
            if form.is_valid():
                # ProfileUser.set_password(request.POST['password'])
                form.save()
                return redirect('home')
    return render(request,'new_user.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_main = authenticate(request,email=email,password=password)
        print(user_main)
        app_user = authenticate(request,email=email,password=password)
        main_user = authenticate(request,email=email,password=password)
        if not ProfileUser.is_superuser:
            print('hello world')
            login(request,app_user)
            return redirect('home')
        elif ProfileUser.is_superuser:
            print('this is admin')
            login(request,main_user)
            return redirect('home')
        else:
            raise Http404("email or password is incorrect")
    return render(request,'login.html',{})


def user_logout(request):
    logout(request)
    return redirect('home')


def admin_camp(request):
    form = BloodCamp()
    if request.method == 'POST':
        camp_name = request.POST.get('camp_name')
        city = request.POST.get('city')
        location = request.POST.get('location')
        organise_date = request.POST.get('organise_date')
        camp = BloodCamp.objects.get(camp_name=camp_name,city=city,location=location,organise_date=organise_date)
        camp.save()
        return redirect('home')
    return render(request,'camp.html',{'form':form})