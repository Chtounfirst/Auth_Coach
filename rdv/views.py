from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rdv.forms import AppointmentForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Appointment
 
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



from django.contrib import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from rdv.forms import AppointmentForm
from rdv.models import Appointment

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            existing_appointment = Appointment.objects.filter(date=form_cleaned_data['date'], time=form_cleaned_data['time']).exists()
            if existing_appointment:
                form.add_error('date', 'Ce créneau est déjà pris. Veuillez choisir une autre date ou heure.')
            else:
                appointment = form.save(commit=False)
                appointment.client = request.user
                appointment.save()
                messages.success(request, 'Rendez-vous enregistré avec succès.')
                return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'rdv/make_appointment.html', {'form': form})

# def make_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form_cleaned_data = form.cleaned_data
#             existing_appointment = Appointment.objects.filter(date=form_cleaned_data['date'], time=form_cleaned_data['time']).exists()
#             if existing_appointment:
#                 form.add_error('date', 'Ce créneau est déjà pris. Veuillez choisir une autre date ou heure.')
#             else:
#                 appointment = form.save(commit=False)
#                 appointment.client = request.user
#                 appointment.save()
#                 messages.success(request, 'Rendez-vous enregistré avec succès.')
#                 return redirect('appointment_list')
#     else:
#         form = AppointmentForm()
#     return render(request, 'rdv/make_appointment.html', {'form': form})

#vue des rendez vous
# from django.shortcuts import render
# from .models import Appointment

# def appointment_view(request):
#     appointments = Appointment.objects.all()
#     context = {'appointments': appointments}
#     return render(request, 'appointments.html', context)

#test affichage vue
from django.shortcuts import render
from .models import Appointment

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment
# @login_required
# def appointment_list(request):
#     user_appointments = Appointment.objects.filter(client=request.user)
#     return render(request, 'rdv/appointment_confirm.html', {'appointments': user_appointments})



from django.shortcuts import render
from .models import Appointment

@login_required
def appointment_list(request):
    user_appointments = Appointment.objects.filter(client=request.user)
    return render(request, 'rdv/appointment_confirm.html', {'appointments': user_appointments})
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'rdv/appointment_confirm.html', {'appointment': appointment})

from django.shortcuts import render
from django.views import View
from .forms import AppointmentForm

class AppointmentView(View):
    def get(self, request):
        form = AppointmentForm()
        return render(request, 'appointment.html', {'form': form})
        
    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return render(request, 'rdv/appointment_confirmation.html', {'appointment': appointment})
        else:
            return render(request, 'appointment.html', {'form': form})
from django.contrib.auth.views import LoginView

from datetime import time, timedelta

def available_time_slots(start_time, end_time, appt_length, break_length):
    current_time = start_time
    slots = []
    while current_time < end_time:
        slots.append(current_time.strftime('%H:%M'))
        current_time += timedelta(minutes=appt_length)
        if current_time < end_time:
            current_time += timedelta(minutes=break_length)
    return slots

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'rdv/appointment_confirm_delete.html'
    success_url = reverse_lazy('home')


class CustomLoginView(LoginView):
    template_name = 'rdv/login.html'
    
    
from django.shortcuts import redirect





