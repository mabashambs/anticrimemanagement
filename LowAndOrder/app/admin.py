from django.contrib import admin
from app.models import Police
from app.models import Detective
from app.models import Citizen
from app.models import Station
from app.models import Complent
from app.models import Criminal
from app.models import Status
# Register your models here.


class PoliceAdmin(admin.ModelAdmin):
    list_display=["police_id","police_name","date_of_birth","address","mobile_no","designation","station_id","username","password"]

class DetectiveAdmin(admin.ModelAdmin):
    list_display=["detective_id","detective_name","date_of_birth","mobile_no","username","password"]

class CitizenAdmin(admin.ModelAdmin):
    list_display=["citizen_id","citizen_name","date_of_birth","email_id","gender","mobile_no","address","username","password"]

class StationAdmin(admin.ModelAdmin):
    list_display=["station_id","station_name","address","city","district","contact_no"]

class ComplentAdmin(admin.ModelAdmin):
    list_display=["complent_id","complent_type","complient_name","date_of_complent","description","proof","station_id","location"]

class CriminalAdmin(admin.ModelAdmin):
    list_display=["criminal_id","criminal_name","img","crime"]

class StatusAdmin(admin.ModelAdmin):
    list_display=["complent_id","complent_type","complient_name","date_of_complent","description","station_id","location","status"]


admin.site.register(Police,PoliceAdmin)
admin.site.register(Detective,DetectiveAdmin)
admin.site.register(Citizen,CitizenAdmin)
admin.site.register(Station,StationAdmin)
admin.site.register(Complent,ComplentAdmin)
admin.site.register(Criminal,CriminalAdmin)
admin.site.register(Status,StatusAdmin)
