"""Calidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from indicador.views import Streaming, Dashboard,Dashboard1, Dashboard2, Crear_Usuario, index, Pagina_Inicio,Dashboard3

urlpatterns = [
    path('Crear_Usuario/', Crear_Usuario.as_view(), name='Crear_Usuario'),

    path('admin/', admin.site.urls),

    #PAGINA DE INICIO
    path('',index, name ='index'),
    #LOGIN
    path('login/',LoginView.as_view(template_name= 'base/login.html'), name ='login'),
    #LOGOUT
    path('logout/',LogoutView.as_view(), name ='logout'),

    #STREAMING Y DASBOARD
    path('Streaming/', Streaming, name='Streaming'),
    path('Dashboard/', Dashboard, name='Dashboard'),
    path('Dashboard1/', Dashboard1, name='Dashboard1'),
    path('Dashboard2/', Dashboard2, name='Dashboard2'),
    path('Dashboard3/', Dashboard3, name='Dashboard3'),
    


    #ESTOS SON LOS TEMAS DE LA APLICACION
    # path('power_bi/', api_bi, name='api_bi'),
    # path('tema_1/', tema_1, name='tema_1'),
    # path('tema_2/', tema_2, name='tema_2'),
    # path('tema_3/', tema_3, name='tema_3'),
    # path('tema_4/', tema_4, name='tema_4'),

    # incluir direcciones de la aplicacion de costos
    path('costo/', include('Costo.urls')),

    # incluir direcciones de la aplicacion de usuarios
    path('usuario/', include('usuario.urls')),

    # incluir direcciones de la aplicacion de usuarios
    path('indicador/', include('indicador.urls')),

]