from django.shortcuts import render

# Create your views here.
from .models import AppUser


def add_user(request):
    form = AppUser()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_type = request.POST.get('blood_type')
        password = request.POST.get('password')
        form = AppUser.objects.create(name=name,age=age,email=email,gender=gender,blood_type=blood_type,password=password)
    return render(request,'new_user.html',{'form':form})