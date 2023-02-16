#formulaire d'inscription
from django import forms
from .models import Appointment


from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'date', 'time']
    
    
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
    ####################################creneaux dispo#############################################"
   
    def get_available_slots(self):
        date = self.cleaned_data['date']
        return Appointment.get_available_slots(date)   
    
