from django.contrib import admin
from .models import Numbers,Covid, districtdata,Emergency, Manchar,ElectricalData,ScienceData,CivilData,MechanicalData,ITData,Contact,DepartmentData,sales
# Register your models here.
admin.site.register(Numbers),
admin.site.register(Emergency),
admin.site.register(Manchar),
admin.site.register(Contact),
admin.site.register(DepartmentData),
admin.site.register(ITData),
admin.site.register(MechanicalData),
admin.site.register(CivilData),
admin.site.register(ScienceData),
admin.site.register(ElectricalData),
admin.site.register(sales),
admin.site.register(districtdata),
admin.site.register(Covid)

