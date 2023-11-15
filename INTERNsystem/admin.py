from django.contrib import admin
from .models import Student,Company,Advisor,Internship,UPLOADBYADMIN,UPLOADBYSTUDENT

# Register your models here.

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Advisor)
admin.site.register(Internship)
admin.site.register(UPLOADBYADMIN)
admin.site.register(UPLOADBYSTUDENT)
