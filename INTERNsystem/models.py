from django.db import models

# Create your models here.

class Student(models.Model):
    StudID = models.CharField(max_length=15,primary_key=True)
    StudName = models.CharField(max_length=70)
    StudCourse = models.CharField(max_length=50)
    StudMentor = models.CharField(max_length=70)
    StudEmailAddr = models.CharField(max_length=30)
    StudTelNo = models.CharField(max_length=15)
    StudImg = models.ImageField(upload_to='Student Profile Picture/',null=True,blank=True)

    def delete(self):
        self.StudImg.delete()
        super().delete()

class Company(models.Model):
    CompanyID = models.CharField(max_length=15,primary_key=True)
    CompanyName = models.TextField(max_length=70)
    CompanyAddr = models.TextField(max_length=100)
    CompanySector = models.CharField(max_length=30)
    CompanyTelNo = models.CharField(max_length=15)

class Advisor(models.Model):
    AdvID = models.CharField(max_length=15,primary_key=True)
    AdvName = models.TextField(max_length=70)
    AdvTelNo = models.CharField(max_length=15)
    AdvEmailAddr = models.CharField(max_length=30)

class Internship(models.Model):
    StudID = models.ForeignKey(Student,on_delete=models.CASCADE)
    CompanyID = models.ForeignKey(Company,on_delete=models.CASCADE)
    AdvID = models.ForeignKey(Advisor,on_delete=models.CASCADE,null=True,blank=True)
    StartDate = models.CharField(max_length=15,null=True,blank=True)
    EndDate = models.CharField(max_length=15,null=True,blank=True)
    Session = models.TextField(max_length=50,null=True,blank=True)
    Salary = models.CharField(max_length=10,null=True,blank=True)
    ProjectBrief = models.TextField(max_length=300,null=True,blank=True)

class UPLOADBYADMIN (models.Model):
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='ADMIN/INTERN APPLICATION PREQUISITE/')

    def __str__(self):
        return str(self.pdf)

    def delete(self):
        self.pdf.delete()
        super().delete()

class UPLOADBYSTUDENT (models.Model):
    StudID = models.ForeignKey(Student,on_delete=models.CASCADE)
    CompanyID = models.ForeignKey(Company,on_delete=models.CASCADE)
    BorangJawapanSyarikat = models.FileField(upload_to='Borang Jawapan Syarikat Pelajar/')

    def delete(self):
        self.BorangJawapanSyarikat.delete()
        super().delete()












