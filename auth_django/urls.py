"""auth_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import rdv.views
from rdv.views import CustomLoginView
# from .views import appointment_view
 
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', rdv.views.home, name='home'),
    path('', rdv.views.register, name='register'),
    path('admin/', admin.site.urls),
    #formulaire d'inscription
    path('rdv/', rdv.views.make_appointment, name='make_appointment'),
    #test vue rendez vous
    path('appointments/', rdv.views.appointment_list, name='appointment_list'),
    
    
    # path('appointments/', appointment_view, name='appointments'),
    # path('', include('appointments.urls')),
]