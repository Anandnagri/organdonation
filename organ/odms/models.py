from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    feedback = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    msg = models.TextField()


class Donor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    mothername = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    organ = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    bloodgroup = models.CharField(max_length=10)
    aadharnumber = models.CharField(max_length=12)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    emergencynumber = models.CharField(max_length=10)
    add = models.TextField()

# Create your models here.
