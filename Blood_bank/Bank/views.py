from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from .models import ProfileUser

def home_page(request):
    return render(request,'home.html',{})

def add_user(request):
    form = ProfileUser()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_type = request.POST.get('blood_type')
        password = request.POST.get('password')
        form = ProfileUser.objects.create(username=username,age=age,email=email,gender=gender,blood_type=blood_type,password=password)
        return redirect('home')
    return render(request,'new_user.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = ProfileUser.objects.get(email=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html',{})


def user_logout(request):
    logout(request)
    return redirect('home')