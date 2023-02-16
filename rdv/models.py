



from django.db import models
from django.core.exceptions import ValidationError

# rendezvous/models.py

from django.db import models

from django.core.exceptions import ValidationError

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def clean(self):
        super().clean()

        # Vérifier que la date est un jour de la semaine où les rendez-vous sont disponibles
        if self.date.weekday() in [5, 6]:  # 5 = samedi, 6 = dimanche
            raise ValidationError('Les rendez-vous ne sont pas disponibles le week-end.')


    
    
    
############################creneaux dispo###################################"
#   

class Meta:
    unique_together = ('date', 'time')
# def clean(self):
#         # Vérifier si un rendez-vous existe déjà à la même date et heure
#         existing_appointment = Appointment.objects.filter(date=self.date, time=self.time).first()
#         if existing_appointment:
#             raise ValidationError('Ce créneau horaire est déjà pris. Veuillez choisir un autre horaire.')

