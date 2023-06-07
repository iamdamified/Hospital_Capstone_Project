from django.db import models

# Create your models here.

class Intro(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.header



class Department(models.Model):
    service = models.CharField(max_length=50)
    image = models.ImageField(upload_to='service_image')
    description = models.TextField()

    def __str__(self):
        return self.service
    


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    sickness_type = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    image = models.ImageField(upload_to='patient_image')
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    testimonials = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_image')
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    about = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class Appointment(models.Models):
    services = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    date = models.DateField()
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    comment = models.TextField()


    def __str__(self):
        return self.name