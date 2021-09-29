from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Services.views import Emergency1,ScienceDept,ElectricalDept,CivilDept, MechanicalDept,ClgCampus, home,MancharNos,AboutUs,contact,SearchFunction,ITDept,covid,sms
urlpatterns = [
    path('' , home),
    path('Campus', Emergency1),
    path('ClgCampus', ClgCampus),#computer
    path("it",ITDept),
    path("mechanical",MechanicalDept),
    path("civil",CivilDept),
    path("electrical",ElectricalDept),
    path("science",ScienceDept),
    path('MancharNos',MancharNos),
    path('about',AboutUs),
    path('contact',contact),
    path('search',SearchFunction),
    path('covid',covid),
    path('sms',sms)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
