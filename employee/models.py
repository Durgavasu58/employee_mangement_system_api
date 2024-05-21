from django.db import models

class AddressDetails(models.Model):
    hno = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    address = models.CharField(max_length=255)

class Qualification(models.Model):
    qualification_name = models.CharField(max_length=255)
    percentage = models.FloatField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    address_details = models.OneToOneField(AddressDetails, on_delete=models.CASCADE)
    work_experience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualification)
    projects = models.ManyToManyField(Project)
    photo = models.ImageField(upload_to="media/images/") 
