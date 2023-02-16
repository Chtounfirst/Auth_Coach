from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rdv.forms import AppointmentForm
from django.urls import reverse_lazy
 
# Views
@login_required
def home(request):
    return render(request, "rdv/index.html", {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'rdv/register.html', {'form': form})



#formulaire d'inscription



def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            existing_appointment = Appointment.objects.filter(date=form_cleaned_data['date'], time=form_cleaned_data['time']).exists()
            if existing_appointment:
                form.add_error('date', 'Ce créneau est déjà pris. Veuillez choisir une autre date ou heure.')
            else:
                form.save()
                return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'rdv/make_appointment.html', {'form': form})

#vue des rendez vous
# from django.shortcuts import render
# from .models import Appointment

def appointment_view(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'appointment.html', context)

#test affichage vue
from django.shortcuts import render
from .models import Appointment
from django.shortcuts import render, get_object_or_404

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'rdv/appointments.html', {'appointments': appointments})


####################################"#verifications de creneaux dispo#########################################""
# from django.shortcuts import render
# from .models import Appointment

# def appointment(request):
#     # Récupérer les créneaux disponibles pour une date donnée
#     date = request.POST.get('date')
#     available_slots = Appointment.objects.filter(date=date, availability=True)

#     # Passer les créneaux disponibles au formulaire Django
#     return render(request, 'appointment.html', {'available_slots': available_slots})
def get_available_slots(self):
    date = self.cleaned_data['date']
    return Appointment.get_available_slots(date) 

def get_success_url(self):
    return reverse_lazy('appointment_confirm', kwargs={'pk': self.instance.pk})

def appointment_confirm(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    context = {'appointment': appointment}
    return render(request, 'appointment_confirm.html', context)
