from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.shortcuts import render , redirect
from solicitud.forms import *
from django.http import JsonResponse
from django.core import serializers
import json
import datetime 

class Crear_User(CreateView): #crear usuario
    model = Usuario
    template_name = 'usuario/usuario.html'
    form_class = UsuarioForm
    second_form_class = UserForm
    success_url = reverse_lazy('home')

    def get_context_data(self,**kwargs):
        context = super(Crear_User, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            usuario = form.save(commit =False)
            usuario.user = form2.save()
            usuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
          return render(request,'usuario/usuario_error.html')
            # return self.render_to_response(self.get_context_data(form = form, form2 = form2))