from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from . views import *


urlpatterns = [
   path('registration/',register_V2,name = 'registerUrl'),
   path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name ='loginUrl'),
   path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name ='logoutUrl'),

]
