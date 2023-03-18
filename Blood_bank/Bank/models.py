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
    age = models.IntegerField(blank = True)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='male')
    blood_type = models.CharField(max_length=4,choices = BLOOD_CHOICES,default='a+')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','first_name', 'last_name']


class BloodCamp(models.Model):
    camp_name = models.CharField(max_length=100)
    city  = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    organise_date  = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)