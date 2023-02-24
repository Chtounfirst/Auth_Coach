
# #formulaire d'inscription

from django.db import models
# from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
class Appointment(models.Model):
    

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    
    
    


# class Appointment(models.Model):
#     client = models.CharField(max_length=100, default='John Doe')
#     date = models.DateField()
#     time = models.TimeField()
#     email = models.EmailField()
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
    # Vérifier que la date est un jour de la semaine où les rendez-vous sont disponibles
    def clean(self):
        super().clean()
        
       
        if self.date and self.date.weekday() in [5, 6]:
            raise ValidationError("Les rendez-vous ne sont pas disponibles le week-end.")
        if self.date and self.date < timezone.localdate():
            raise ValidationError("La date du rendez-vous ne peut pas être dans le passé.")

        
    
# def clean(self):
#         # Vérifier si un rendez-vous existe déjà à la même date et heure
#         existing_appointment = Appointment.objects.filter(date=self.date, time=self.time).first()
#         if existing_appointment:
#             raise ValidationError('Ce créneau horaire est déjà pris. Veuillez choisir un autre horaire.')


