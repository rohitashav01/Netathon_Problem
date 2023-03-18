from django.db import models

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

class AppUser(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank = True)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='male')
    blood_type = models.CharField(max_length=4,choices = BLOOD_CHOICES,default='a+')
    password = models.CharField(max_length=50)