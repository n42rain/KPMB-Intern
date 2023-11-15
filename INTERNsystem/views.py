import os;
from django.shortcuts import render, get_object_or_404, redirect;
from django.http import HttpResponse,HttpResponseRedirect;
from django.db.models import Q;
from django.urls import reverse;
from django.contrib import messages;
from django.conf import settings;
from INTERNsystem.forms import StudentForm,adminuploadForm,studuploadForm;
from INTERNsystem.models import Student,Company,Advisor,Internship,UPLOADBYADMIN,UPLOADBYSTUDENT;
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage;



# Create your views here.

def mainpage(request):
    return render(request,'mainpage.html')

def index(request):
    return render(request,'index.html')

def addstud(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,("Data successfully uploaded."))
        else:
            context = { 'form' : form }
            return render(request,'addstud.html',context)
    context = {'form':StudentForm()}
    return render(request,'addstud.html',context)

def displaystud(request):
    alldata=Student.objects.all()
    dict={
        'studdata' : alldata
    }
    return render(request,'displaystud.html',dict)

def deletestud(request,StudID):
    
    BorangJawapanSyarikat = get_object_or_404(Student,StudID=StudID)
    BorangJawapanSyarikat.delete()
    return redirect('displaystud')

def addcompany(request):
    if request.method =='POST':
        C_ID=request.POST['CompanyID']
        C_name=request.POST['CompanyName']
        C_addr=request.POST['CompanyAddr']
        C_sector=request.POST['CompanySector']
        C_telno=request.POST['CompanyTelNo']
        data = Company (CompanyID=C_ID,CompanyName=C_name,CompanyAddr=C_addr,CompanySector=C_sector,CompanyTelNo=C_telno)
        data.save()
        dict={
            'message': 'Data save'
        }
        messages.success(request,("Data successfully uploaded."))
        return render(request,'addcompany.html')
    else:
        dict={
            'message':''
        }
        return render(request,'addcompany.html')

def displaycompany(request):
    alldata=Company.objects.all()
    dict={
        'compdata' : alldata
    }
    return render(request,'displaycompany.html',dict)

def updatecomp(request,CompanyID):
    data=Company.objects.get(CompanyID=CompanyID)
    dict={
        'data': data
    }
    return render(request,"updatecomp.html",dict)

def update_datacomp(request,CompanyID):
    S_name=request.POST['CompanyName']
    S_course=request.POST['CompanyAddr']
    S_weight=request.POST['CompanySector']
    S_height=request.POST['CompanyTelNo']
    data=Company.objects.get(CompanyID=CompanyID)
    data.CompanyName=S_name
    data.CompanyAddr=S_course
    data.CompanySector=S_weight
    data.CompanyTelNo=S_height
    data.save()
    return HttpResponseRedirect(reverse("displaycompany"))

def deletecomp(request,CompanyID):
    data = Company.objects.get(CompanyID=CompanyID)
    data.delete()
    return HttpResponseRedirect(reverse("displaycompany"))

def addadv(request):
    if request.method =='POST':
        C_ID=request.POST['AdvID']
        C_name=request.POST['AdvName']
        C_addr=request.POST['AdvEmailAddr']
        C_telno=request.POST['AdvTelNo']
        data = Advisor(AdvID=C_ID,AdvName=C_name,AdvEmailAddr=C_addr,AdvTelNo=C_telno)
        data.save()
        dict={
            'message': 'Data save'
        }
        messages.success(request,("Data successfully uploaded."))
        return render(request,'addadv.html')
    else:
        dict={
            'message':''
        }
        return render(request,'addadv.html')

def displayadv(request):
    alldata=Advisor.objects.all()
    dict={
        'advdata' : alldata
    }
    return render(request,'displayadv.html',dict)

def updateadv(request,AdvID):
    data=Advisor.objects.get(AdvID=AdvID)
    dict={
        'data': data
    }
    return render(request,"updateadv.html",dict)

def update_dataadv(request,AdvID):
    S_name=request.POST['AdvName']
    S_course=request.POST['AdvTelNo']
    S_weight=request.POST['AdvEmailAddr']
    data=Advisor.objects.get(AdvID=AdvID)
    data.AdvName=S_name
    data.AdvTelNo=S_course
    data.AdvEmailAddr=S_weight
    data.save()
    return HttpResponseRedirect(reverse("displayadv"))

def deleteadv(request,AdvID):
    data = Advisor.objects.get(AdvID=AdvID)
    data.delete()
    return HttpResponseRedirect(reverse("displayadv"))

def addintern(request):
    if request.method=='POST':
        StudID=request.POST['StudID']
        CompanyID=request.POST['CompanyID']
        AdvID=request.POST['AdvID']
        StartDate=request.POST['StartDate']
        EndDate=request.POST['EndDate']
        Session=request.POST['Session']
        Salary=request.POST['Salary']
        ProjectBrief=request.POST['ProjectBrief']
        S_ID = Student.objects.get(StudID=StudID)
        Sp_code = Company.objects.get(CompanyID=CompanyID)
        C_ID = Advisor.objects.get(AdvID=AdvID)   
        data=Internship(StudID=S_ID,CompanyID=Sp_code,AdvID=C_ID,StartDate=StartDate,EndDate=EndDate,Session=Session,Salary=Salary,ProjectBrief=ProjectBrief)
        data.save()
        messages.success(request,("Data successfully uploaded."))
        return render(request,'addintern.html')
    else:
        dict={
            'message':''
        }
    alldata=Student.objects.all()
    alldata2=Company.objects.all()
    alldata3=Advisor.objects.all()
    alldata4=UPLOADBYSTUDENT.objects.all()
    dict = {
            'studdata' : alldata ,
            'compdata' : alldata2,
            'advdata' : alldata3,
            'filedata': alldata4
        }
    return render(request,'addintern.html',dict)

def displayintern(request):
    alldata=Internship.objects.all()
    dict={
        'interndata' : alldata
    }
    return render(request,'displayintern.html',dict)

def updateintern(request,id):
    data=Internship.objects.get(id=id)
    dict = {
        'data':data
    }
    return render(request,"updateintern.html",dict)

def update_dataintern(request,id):
    S_level=request.POST['StartDate']
    S_venue=request.POST['EndDate']
    S_date=request.POST['Session']
    Rank=request.POST['Salary']
    ProjectBrief=request.POST['ProjectBrief']
    data=Internship.objects.get(id=id)
    data.StartDate=S_level
    data.EndDate=S_venue
    data.Session=S_date
    data.Salary=Rank
    data.ProjectBrief=ProjectBrief
    data.save()
    return HttpResponseRedirect(reverse("displayintern"))


def deleteintern(request,code):
    data =  Internship.objects.get(id=code)
    data.delete()
    return HttpResponseRedirect(reverse("displayintern"))


class adminuploadview(TemplateView):
    template_name = 'adminupload.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        get_files = UPLOADBYADMIN.objects.all()
        context = {'form':adminuploadForm,'get_files':get_files}
        return context 

    def post(self,request,**kwargs):
        context = {}
        if request.method == "POST":
            form = adminuploadForm(request.POST,request.FILES)

            if form.is_valid():
                form.save()
                #UPLOADBYADMIN.objects.get_or_create(name=form.cleaned_data.get('name'))
                #UPLOADBYADMIN.objects.get_or_create(pdf=form.cleaned_data.get('pdf'))

                return redirect ('adminuploadview')
            else:
                context['form'] = form
        else:
            context['form'] = form

        return redirect ('adminuploadview')

def deleteadminupload(request,id):
    pdf = get_object_or_404(UPLOADBYADMIN,id=id)
    pdf.delete()
    return redirect('adminuploadview')

'''
def searchcomp(request):
        return render(request,'searchcomp.html')

def searchdatacomp(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query:
            company = Company.objects.filter(CompanyAddr__icontains=query)
            return render(request,'searchcomp.html',{'company':company},{'query':query})
        else:
            print("No information to show!")
            return render(request,'searchcomp.html',{})
'''

def studfileupload(request):
    if request.method == 'POST':
        form = studuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,("Data successfully uploaded."))
        else:
            context = { 'form' : form }
            return render(request,'studfileupload.html',context)
    context = {'form':studuploadForm()}
    return render(request,'studfileupload.html',context)

def displayfileupload(request):
    alldata= UPLOADBYSTUDENT.objects.all()
    dict={
        'alldata' : alldata
    }
    return render(request,'displayfileupload.html',dict)

def deletefileupload(request,id):
    data = get_object_or_404(UPLOADBYSTUDENT,id=id)
    data.delete()
    return redirect('displayfileupload')






