# formulaire d'inscription**

from django.contrib import admin
from .models import Appointment



#voir les rdv
from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date', 'time')

admin.site.register(Appointment, AppointmentAdmin)

