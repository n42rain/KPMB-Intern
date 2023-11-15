from django import forms
from INTERNsystem.models import Student,UPLOADBYADMIN,UPLOADBYSTUDENT

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('StudID','StudName','StudCourse','StudMentor','StudEmailAddr','StudTelNo','StudImg')

class adminuploadForm(forms.ModelForm):
    name = forms.CharField()
    pdf = forms.FileField()

    class Meta():
        model = UPLOADBYADMIN
        fields = ('name','pdf')

class studuploadForm(forms.ModelForm):
    class Meta:
        model = UPLOADBYSTUDENT
        fields = ('StudID','CompanyID','BorangJawapanSyarikat')