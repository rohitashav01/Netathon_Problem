from django.conf import settings
from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import login,logout,authenticate
from Bank.forms import AppUserForm,DiseaseForm, ChatForm
from .models import ProfileUser,BloodCamp,Diseases, Chat
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def home_page(request):
    return render(request,'home.html',{})

def add_user(request):
    form = AppUserForm()
    if request.method == 'POST':
            form = AppUserForm(request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
    return render(request,'new_user.html',{'form':form})

def user_disease(request):
    form = DiseaseForm()
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.save()
            return redirect('home')
    return render(request,'disease.html',{'form':form})

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
            print(request.user.id)
            return redirect('disease')
        else:
            raise Http404("email or password is incorrect")
    return render(request,'login.html',{})

#user logout
def user_logout(request):
    logout(request)
    return redirect('home')

#add camps
def admin_camp(request):
    form = BloodCamp()
    if request.method == 'POST':
        camp_name = request.POST.get('camp_name')
        city = request.POST.get('city')
        location = request.POST.get('location')
        organise_date = request.POST.get('organise_date')
        camp = BloodCamp.objects.create(camp_name=camp_name,city=city,location=location,organise_date=organise_date)
        camp.save()

        user = ProfileUser.objects.filter(is_superuser=False).values()
        for u in user:
            print(u)
            subject = 'welcome to GFG world'
            message = f'Hi {u["username"]}, thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [u['email'], ]
            send_mail( subject, message, email_from, recipient_list )
        return redirect('home')
    return render(request,'camp.html',{'form':form})

#availaible camps
def show_camps(request):
    user = Diseases.objects.all()
    if request.user.is_authenticated:
        for u in user:
            if u.aids == False and u.asthma == False and u.bleeding_disorder == False and u.cancer == False and u.heart_disease == False and u.hepatitis_b_or_c == False and u.mad_cow:
                camps = BloodCamp.objects.all()
                print(request.user)
            else:
                raise PermissionDenied('You cannot donate blood')
    return render(request,'avail_camps.html', {'camps': camps})

#register for the camp
def register_camp(request):
    demo = Diseases.objects.all()
    if request.user.is_authenticated:
        for u in demo:
            if u.aids == False and u.asthma == False and u.bleeding_disorder == False and u.cancer == False and u.heart_disease == False and u.hepatitis_b_or_c == False and u.mad_cow:
                    user = ProfileUser.objects.filter(is_donor=True).values()
                    for u  in user:
                        subject = 'Blood Donation Camp Registration'
                        message = f'Hello {request.user.username},You have successfull registered  for the camp'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [request.user.email]
                        print(recipient_list)
                        send_mail(subject,message,email_from,recipient_list)
                        return redirect('home')
            else:
                raise PermissionDenied('You cannot donate blood')
    return render(request,'avail_camps.html',{})

#availaible list of donors
def donor_list(request):
    user = ProfileUser.objects.filter(is_donor=True)
    return render(request, 'donor.html', {'user':user})

def contact_donor(request,**kwargs):
    if id:=kwargs.get('id'):
        obj = ProfileUser.objects.get(id=id)
        if request.user.is_authenticated:
            subject = 'Blood Needed'
            message = f'Hello {obj.username}, {request.user.username} has requested for blood which matches your blood type'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [obj.email]
            print(recipient_list)
            send_mail(subject,message,email_from,recipient_list)
        return redirect('home')
    return render(request,'donor.html',{})




