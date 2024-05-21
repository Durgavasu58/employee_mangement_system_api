from django.contrib import admin
from .models import Employee, AddressDetails, WorkExperience, Qualification, Project
# Register your models here.

admin.site.register(Employee)
admin.site.register(AddressDetails)
admin.site.register(WorkExperience)
admin.site.register(Qualification)
admin.site.register(Project)