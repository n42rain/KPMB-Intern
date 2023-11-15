from django import template
from INTERNsystem.models import Student,UPLOADBYSTUDENT

register = template.Library()

@register.filter
def display_status(StudID):
    try:
        StudImg = Student.objects.get(StudID=StudID).StudImg
        if StudImg:
            return "ACCEPTED"
    except Student.DoesNotExist:
        pass
    return "PENDING"

@register.filter
def display_status2(StudID):
    try:
        BorangJawapanSyarikat = UPLOADBYSTUDENT.objects.get(StudID=StudID).BorangJawapanSyarikat
        if BorangJawapanSyarikat:
            return "ACCEPTED"
    except UPLOADBYSTUDENT.DoesNotExist:
        pass
    return "PENDING"


