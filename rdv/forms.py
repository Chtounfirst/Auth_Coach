#formulaire d'inscription
from django import forms
from .models import Appointment
from django.forms import ModelForm

from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta



from django.forms import ModelForm, DateTimeInput







class AppointmentForm(ModelForm):
      # Choix d'heures pour le champ de temps
    TIME_CHOICES = (
        ('9:00', '9:00'),
        ('9:30', '9:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
    )
    time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = Appointment
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    
    def clean(self):
            cleaned_data = super().clean()
            date = cleaned_data.get('date')
            time = cleaned_data.get('time')
            if date and time:
                conflicting_appointments = Appointment.objects.filter(date=date, time=time)
                if self.instance.pk:
                    conflicting_appointments = conflicting_appointments.exclude(pk=self.instance.pk)
                if conflicting_appointments.exists():
                    raise forms.ValidationError("Un rendez-vous existe déjà pour ce créneau horaire.")
                
            return cleaned_data
        
    def get_success_url(self):
        return reverse_lazy('appointment_confirm', kwargs={'pk': self.instance.pk})
    
    def appointment_confirm(request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        context = {'appointment': appointment}
        return render(request, 'appointment_confirm.html', context)