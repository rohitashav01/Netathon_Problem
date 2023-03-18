from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER_CHOICES = [
    ('male','MALE'),
    ('female','FEMALE')
]
BLOOD_CHOICES = [
    ('a+','A+'),
    ('a+','A-'),
    ('b+','B+'),
    ('b+','B-'),
    ('o+','O+'),
    ('o+','O-'),
    ('ab+','AB+'),
    ('ab-','AB-')

]

class ProfileUser(AbstractUser):
    username = models.CharField(max_length=20)
    age = models.IntegerField(blank = True,null=True)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='male')
    blood_type = models.CharField(max_length=4,choices = BLOOD_CHOICES,default='a+')
    is_donor = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','first_name', 'last_name']


class BloodCamp(models.Model):
    camp_name = models.CharField(max_length=100)
    city  = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    organise_date  = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)



class Diseases(models.Model):
     user = models.ForeignKey(ProfileUser,on_delete=models.CASCADE)
     aids = models.BooleanField(default=False)
     asthma = models.BooleanField(default=False)
     bleeding_disorder = models.BooleanField(default=False)
     cancer = models.BooleanField(default=False)
     heart_disease = models.BooleanField(default=False)
     hepatitis_b_or_c = models.BooleanField(default=False)
     mad_cow = models.BooleanField(default=False)
    


class Chat(models.Model):
     user = models.ForeignKey(ProfileUser,on_delete=models.CASCADE)
     is_sender = models.BooleanField(default=False)
     is_receiver = models.BooleanField(default=False)
     message = models.CharField(max_length=1000)
     created_at = models.DateTimeField(auto_now=True)
     
    