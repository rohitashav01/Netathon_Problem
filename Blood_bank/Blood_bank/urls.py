"""Blood_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Bank.views import add_user,user_login,user_logout,home_page,admin_camp,show_camps,user_disease,donor_list,register_camp,contact_donor
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home'),
    path('blood-bank/register',add_user,name='new-user'),
    path('blood-bank/disease',user_disease,name='disease'),
    path('blood-bank/login',user_login,name='login'),
    path('blood-camp/register',register_camp,name='register-camp'),
    path('blood-bank/logout',user_logout,name='logout'),
    path('blood-bank/admin_camp',admin_camp,name='camp'),
    path('blood_bank/availaible_camps',show_camps,name='avail-camps'),
    path('donor/list',donor_list, name='donor-list'),
    path('donor/<int:id>/contact',contact_donor,name='contact')   
]


