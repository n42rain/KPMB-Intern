from django.urls import path
from . import views
from INTERNsystem.models import UPLOADBYADMIN
from INTERNsystem.forms import adminuploadForm
from INTERNsystem.views import adminuploadview

urlpatterns=[
    path("",views.mainpage,name="mainpage"),
    path("index",views.index,name="index"),
    path('addstud',views.addstud,name="addstud"),
    path("displaystud",views.displaystud,name="displaystud"),
    path('deletestud/<str:StudID>',views.deletestud,name="deletestud"),
    path("addcompany",views.addcompany,name="addcompany"),
    path("displaycompany",views.displaycompany,name="displaycompany"),
    path('updatecomp/<str:CompanyID>',views.updatecomp, name='updatecomp'),
    path('updatecomp/update_datacomp/<str:CompanyID>',views.update_datacomp, name='update_datacomp'),
    path('deletecomp/<str:CompanyID>',views.deletecomp, name='deletecomp'),
    path("addadv",views.addadv,name="addadv"),
    path("displayadv",views.displayadv,name="displayadv"),
    path('updateadv/<str:AdvID>',views.updateadv, name='updateadv'),
    path('updateadv/update_dataadv/<str:AdvID>',views.update_dataadv, name='update_dataadv'),
    path('deleteadv/<str:AdvID>',views.deleteadv, name='deleteadv'),
    path("addintern",views.addintern,name="addintern"),
    path("displayintern",views.displayintern,name="displayintern"),
    path('updateintern/<str:id>',views.updateintern, name='updateintern'),
    path('updateintern/update_dataintern/<str:id>',views.update_dataintern, name='update_dataintern'),
    path('deleteintern/<str:code>',views.deleteintern, name='deleteintern'),
    path('adminuploadview',adminuploadview.as_view(), name='adminuploadview'),
    path('deleteadminupload/<str:id>',views.deleteadminupload,name="deleteadminupload"),
    path('studfileupload',views.studfileupload,name='studfileupload'),
    path("displayfileupload",views.displayfileupload,name="displayfileupload"),
    path('deletefileupload/<str:id>',views.deletefileupload,name="deletefileupload"),

]