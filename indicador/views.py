from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import  CreateView
from django.contrib.auth.models import User
from .models import *
from .forms import *
# from .api_powerbi import *
from django.http import JsonResponse

import numpy as np
import xlrd
import os
# Create your views here.

class Crear_Usuario(CreateView): #crear usuario
    model = Usuario
    template_name = 'base/Usuario.html'
    form_class = UsuarioForm
    second_form_class = UserForm
    success_url = reverse_lazy('Streaming')
    
    def get_context_data(self,**kwargs):
        context = super(Crear_Usuario, self).get_context_data(**kwargs)
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
            return render(request,'base/Usuario_Error.html')



def api_bi(request):
    import pandas as pd
    from datetime import datetime
    from datetime import timedelta
    import requests
    import time
    import random

    ##class for data_generation


    def data_generation():
        FACTURACION = random.randint(10,20)
        RECAUDO = random.randint(10,20)
        COSTOS =random.randint(5, 30)
        GASTOS = random.randint(20, 100)
        INGRESOS = random.randint(50, 500)
        NOMINA = random.randint(10, 20)
        COSTO_MEDICAMENTOS = random.randint(2, 10)
        FECHA = datetime.now().isoformat()

        return [FACTURACION,
                RECAUDO,
                COSTOS,
                GASTOS,
                INGRESOS,
                NOMINA,
                COSTO_MEDICAMENTOS,
                FECHA
                ]


    # if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/a944c466-734b-4bd4-8cd8-c77d529a3150/datasets/87c5fec3-469e-4369-b5fd-136db20487e9/rows?tenant=a944c466-734b-4bd4-8cd8-c77d529a3150&UPN=ceo%40wetechin.org&key=kYjxgjRj77d7rvPRGI%2Byb0z7cfG6r91ey5Lj90bD4sO1WizwNf0z79lhENFFqGpLo2L0u8%2BW4ZkkpadXa3g%2FdQ%3D%3D'
    #'https://api.powerbi.com/beta/a944c466-734b-4bd4-8cd8-c77d529a3150/datasets/a61197ae-f34a-454f-9c35-dc30e8c515d3/rows?redirectedFromSignup=1&key=bRPsa8kIiVBgdFCrhc8Bn1fZZf2o65H0oWv0AbvFOhYkvevcRWT67yvPcxJmaABDYHuuE9YJzgDGTLuFvZxOmQ%3D%3D'
    # 'https://api.powerbi.com/beta/e81af6ba-a66f-4cab-90f9-9225862c5cf8/datasets/51a56115-ac32-437a-8f2c-3ed1fa1dc37a/rows?key=24THP%2FqLUg2EWnDtFiTUr8GTjjPOU%2FxjT%2BnkTt9%2FHMlkMG%2B5BhWe0pYVfsJcE8gVNitZ3C2Fp1akv3LR7hLVNQ%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["FACTURACION", "RECAUDO", "COSTOS","GASTOS", "INGRESOS", "NOMINA", "COSTO_MEDICAMENTOS", "FECHA"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(2)


# ESTA ES LA VISTA DE LA PAGINA DE INICIO
def index(request):
    sub_grup = Sub_grupo.objects.all()
    tam = sub_grup.count()
    lista_sub_grup = []

    # crear matriz de listas
    for i in range(tam):
        lista_sub_grup.append([])
        for j in range(2):
            lista_sub_grup[i].append(None)

    cont = 0
    for i in sub_grup:

        indicador = Indicador.objects.filter(sub_grupo = i.id)
        contar_indicadores = indicador.count()+10
        indicadores_diligenciados = 2
        porc_diligenciado = round((indicadores_diligenciados/contar_indicadores)*100,1)
        lista_sub_grup[cont][0] = porc_diligenciado

        cont += 1

    print(lista_sub_grup)

    contexto = {'lista':lista_sub_grup}

    return render(request, 'base/index.html',contexto)


def Streaming(request,*args, **kwargs):
    return render(request, 'indicadores/Streaming.html')

def Dashboard(request,*args, **kwargs):
    return render(request, 'indicadores/Dashboard.html')

def Dashboard1(request,*args, **kwargs):
    return render(request, 'indicadores/Dashboard1.html')

def Dashboard2(request,*args, **kwargs):
    return render(request, 'indicadores/Dashboard2.html')
    
def Pagina_Inicio(request,*args, **kwargs):
    return render(request, 'base/pagina_inicio.html')


#ESTOS SON LOS TEMAS DE LA PAGINA
def tema_1(request,*args, **kwargs):
    return render(request, 'base/TemaBlue/tema_1.html')

def tema_2(request,*args, **kwargs):
    return render(request, 'base/TemaWhite/tema_white_1.html')

def tema_3(request,*args, **kwargs):
    return render(request, 'base/TemaWhiteTotal/tema_3.html')

def tema_4(request,*args, **kwargs):
    return render(request, 'base/TemaWhiteBlue/tema_4.html')
#fin TEMAS DE LA PAGINA********************



# INICIO VISTAS PARA TIPO DE REPORTE
def Tipo_reporteList(request):
    
    # archi = xlrd.open_workbook('C:\\env\\src\\Calidad\\Apps\\indicador\\funciones\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(0)

    # cont = 0
    # for i in range(1,hoja1.nrows): 
    #     fila = hoja1.cell_value(i,0)
    #     a= Tipo_reporte()
    #     a.nombre ="prueba"
    #     a.descripcion = fila
    #     a.save()
    #     print(fila)
    a= np.random.random()
    print('esta es la variable aleatoria', a) 

    tiporeporte = Tipo_reporte.objects.all()
    contexto = {'tiporeportes':tiporeporte}
    return render(request, 'indicadores/tiporeporte_list.html', contexto) 

def Tipo_reporteCrear(request):
    if request.method == 'POST':
        form = Tipo_reporteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Tipo_reporte_list')
    else:
        # controlar las peticiones a solo get y post
        form = Tipo_reporteForm()
    return render(request, 'indicadores/tiporeporte_form.html', {'form':form})

def Tipo_reporteEdit(request, id_):
    tipo_reporte_tem = Tipo_reporte.objects.get(id=id_)
    if request.method =='GET':
        form = Tipo_reporteForm(instance = tipo_reporte_tem)
    else:
        form = Tipo_reporteForm(request.POST, instance = tipo_reporte_tem)
        if form.is_valid():
            form.save()
        return redirect('Tipo_reporte_list')
    return render(request,'indicadores/tiporeporte_form.html', {'form':form})

def Tipo_reporteElim(request, id_):
    tiporeport = Tipo_reporte.objects.get(id = id_)
    tiporeport.delete()
    return redirect('Tipo_reporte_list')
#FIN VISTAS PARA TIPO DE REPORTE*******************



# INICIO VISTAS PARA Grupo_general
def Grupo_generalList(request):
    
    Grupogeneral = Grupo_general.objects.all()
    contexto = {'Grupo_generals':Grupogeneral}
    return render(request, 'indicadores/Grupo_general_list.html', contexto) 

def Grupo_generalCrear(request):
    if request.method == 'POST' :
        form = Grupo_generalForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Grupo_general_list')
    else:
        form = Grupo_generalForm()
    return render(request, 'indicadores/Grupo_general_form.html', {'form':form})

def Grupo_generalEdit(request, id_):
    Grupo_general_tem = Grupo_general.objects.get(id=id_)
    if request.method =='GET':
        form = Grupo_generalForm(instance = Grupo_general_tem)
    else:
        form = Grupo_generalForm(request.POST, instance = Grupo_general_tem)
        if form.is_valid():
            form.save()
        return redirect('Grupo_general_list')
    return render(request,'indicadores/Grupo_general_form.html', {'form':form})

def Grupo_generalElim(request, id_):
    Grupo_general_tem = Grupo_general.objects.get(id = id_)
    Grupo_general_tem.delete()
    return redirect('Grupo_general_list')



# INICIO VISTAS PARA Sub_grupo
def Sub_grupoList(request):
    Sub_grupol = Sub_grupo.objects.all()
    contexto = {'Sub_grupos':Sub_grupol}
    return render(request, 'indicadores/Sub_grupo_list.html', contexto) 

def Sub_grupoCrear(request):
    if request.method == 'POST' :
        form = Sub_grupoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Sub_grupo_list')
    else:
        form = Sub_grupoForm()
    return render(request, 'indicadores/Sub_grupo_form.html', {'form':form})

def Sub_grupoEdit(request, id_):
    Sub_grupo_tem = Sub_grupo.objects.get(id=id_)
    if request.method =='GET':
        form = Sub_grupoForm(instance = Sub_grupo_tem)
    else:
        form = Sub_grupoForm(request.POST, instance = Sub_grupo_tem)
        if form.is_valid():
            form.save()
        return redirect('Sub_grupo_list')
    return render(request,'indicadores/Sub_grupo_form.html', {'form':form})

def Sub_grupoElim(request, id_):
    Sub_grupo_tem = Sub_grupo.objects.get(id = id_)
    Sub_grupo_tem.delete()
    return redirect('Sub_grupo_list')



# INICIO VISTAS PARA Indicador
def IndicadorList(request):
    Indicadorl = Indicador.objects.all()
    contexto = {'Indicadors':Indicadorl}
    return render(request, 'indicadores/Indicador_list.html', contexto) 

def IndicadorCrear(request):
    if request.method == 'POST' :
        form = IndicadorForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Indicador_list')
    else:
        form = IndicadorForm()
    return render(request, 'indicadores/Indicador_form.html', {'form':form})

def IndicadorEdit(request, id_):
    Indicador_tem = Indicador.objects.get(id=id_)
    if request.method =='GET':
        form = IndicadorForm(instance = Indicador_tem)
    else:
        form = IndicadorForm(request.POST, instance = Indicador_tem)
        if form.is_valid():
            form.save()
        return redirect('Indicador_list')
    return render(request,'indicadores/Indicador_form.html', {'form':form})

def IndicadorElim(request, id_):
    Indicador_tem = Indicador.objects.get(id = id_)
    Indicador_tem.delete()
    return redirect('Indicador_list')



# INICIO VISTAS PARA Lenar_Indicador
def Lenar_IndicadorList(request):
    # Lenar_Indicadorl = Lenar_Indicador.objects.all()

    # if Lenar_Indicadorl.count() != 0:
    #     for i in Lenar_Indicadorl:
    #         i.resultado = round(i.valor_numerador/i.valor_denominador,1)
    #         i.save()

    Lenar_Indicadorl = Lenar_Indicador.objects.all()
    contexto = {'Lenar_Indicadors':Lenar_Indicadorl}
    return render(request, 'indicadores/Lenar_Indicador_list.html', contexto) 

def Lenar_IndicadorCrear(request):
    Lenar_Indicadorl = Lenar_Indicador.objects.all()
    if request.method == 'POST' :
        form = Lenar_IndicadorForm(request.POST)
        if form.is_valid(): 
            form.save()
            print(form)
        return redirect('Lenar_Indicador_crear')
    else:
        form = Lenar_IndicadorForm()
    
    if Lenar_Indicadorl.count() != 0:
        Lenar_ind_ultimo = Lenar_Indicadorl.last()
        Lenar_ind_ultimo.resultado = round((Lenar_ind_ultimo.valor_numerador/Lenar_ind_ultimo.valor_denominador)*Lenar_ind_ultimo.indicador.factor,2)
        Lenar_ind_ultimo.save()

    return render(request, 'indicadores/Lenar_Indicador_form.html', {'form':form, 'Lenar_Indicadors':Lenar_Indicadorl})

def Lenar_IndicadorEdit(request, id_):
    Lenar_Indicador_tem = Lenar_Indicador.objects.get(id=id_)
    if request.method =='GET':
        form = Lenar_IndicadorForm(instance = Lenar_Indicador_tem)
    else:
        form = Lenar_IndicadorForm(request.POST, instance = Lenar_Indicador_tem)
        if form.is_valid():
            form.save()
            Lenar_Indicador_tem = Lenar_Indicador.objects.get(id=id_)
            Lenar_Indicador_tem.resultado = round((Lenar_Indicador_tem.valor_numerador/Lenar_Indicador_tem.valor_denominador)*Lenar_Indicador_tem.indicador.factor,2)
            Lenar_Indicador_tem.save()
        return redirect('Lenar_Indicador_list')
    return render(request,'indicadores/Lenar_Indicador_form.html', {'form':form})

#esta es la edicion en la vista del formulario cuando se esta LLenando el Indicador
def Lenar_IndicadorEdit_Form(request, id_):
    Lenar_Indicador_tem = Lenar_Indicador.objects.get(id=id_)
    if request.method =='GET':
        form = Lenar_IndicadorForm(instance = Lenar_Indicador_tem)
    else:
        form = Lenar_IndicadorForm(request.POST, instance = Lenar_Indicador_tem)
        if form.is_valid():
            form.save()
            Lenar_Indicador_tem = Lenar_Indicador.objects.get(id=id_)
            Lenar_Indicador_tem.resultado = round((Lenar_Indicador_tem.valor_numerador/Lenar_Indicador_tem.valor_denominador)*Lenar_Indicador_tem.indicador.factor,2)
            Lenar_Indicador_tem.save()

        return redirect('Lenar_Indicador_crear')
    return render(request,'indicadores/Lenar_Indicador_form_2.html', {'form':form})

#esta vista se realiza porque al momento de editar con los efectos se pierden los valores del numerador y del denominador
def Lenar_IndicadorEdit_Sin_Efecto(request, id_):
    Lenar_Indicador_tem = Lenar_Indicador.objects.get(id=id_)
    if request.method =='GET':
        form = Lenar_IndicadorForm(instance = Lenar_Indicador_tem)
    else:
        form = Lenar_IndicadorForm(request.POST, instance = Lenar_Indicador_tem)
        if form.is_valid():
            form.save()
            Lenar_Indicador_tem = Lenar_Indicador.objects.get(id=id_)
            Lenar_Indicador_tem.resultado = round((Lenar_Indicador_tem.valor_numerador/Lenar_Indicador_tem.valor_denominador)*Lenar_Indicador_tem.indicador.factor,2)
            Lenar_Indicador_tem.save()

        return redirect('Lenar_Indicador_crear')
    return render(request,'indicadores/Lenar_Indicador_form_3.html', {'form':form})


def Lenar_IndicadorElim(request, id_):
    Lenar_Indicador_tem = Lenar_Indicador.objects.get(id = id_)
    Lenar_Indicador_tem.delete()
    return redirect('Lenar_Indicador_list')

    # if request.method == 'POST':
    #     Lenar_Indicador_tem.delete()
    #     return redirect('Lenar_Indicador_list')
    # return render(request,'indicadores/Lenar_Indicador_elim.html', {'Lenar_Indicador_tem':Lenar_Indicador_tem})

#listas para los selects deendientes
def Lista_sub_grupo(request):
    grupo_general = request.GET.get('grupo_general')
    sub_grupo1 = Sub_grupo.objects.filter(grupo_general=grupo_general).order_by('nombre')
    return render(request,'indicadores/listas_dependientes/Lista_sub_grupo.html',{'sub_grupos':sub_grupo1})

def Lista_Indicador(request):
    sub_grupo = request.GET.get('sub_grupo')
    indicador1 = Indicador.objects.filter(sub_grupo=sub_grupo)
    return render(request,'indicadores/listas_dependientes/Lista_Indicador.html',{'indicadors':indicador1})

# Estas son las vistas necesarias para mostrar los campos ocultos dependientes
def Lenar_Indicador_numerador(request):
    Lenar_Indicadorl = Lenar_Indicador.objects.all()
    if request.method == 'POST' :
        form = Lenar_IndicadorForm(request.POST)
        if form.is_valid(): 
            form.save()
    else:
        form = Lenar_IndicadorForm()

    indicador = request.GET.get('indicador')
    indicador1 = Indicador.objects.filter(id = indicador).last()
    return render(request,'indicadores/listas_dependientes/Lenar_Indicador_numerador.html',{'indicadors':indicador1, 'form':form} )

#esta es la vista para cambiar de manera asincronica la unidad del indicdor a la hora de registrarlo
def Lenar_Indicador_unidad(request):
   indicador = request.GET.get('indicador')
   indicador1 = Indicador.objects.filter(id = indicador).last()
   return render(request, 'indicadores/listas_dependientes/Lenar_Indicador_unidad.html',{'unidad':indicador1})

# INICIO VISTAS PARA Plan_Mejoramiento
def Plan_MejoramientoList(request):
    Plan_Mejoramientol = Plan_Mejoramiento.objects.all()
    contexto = {'Plan_Mejoramientos':Plan_Mejoramientol}
    return render(request, 'indicadores/Plan_Mejoramiento_list.html', contexto) 

def Plan_MejoramientoCrear(request, id_):
    llave_prim = Lenar_Indicador.objects.get(id =id_)
    
    
    contar_planes_mejo = Plan_Mejoramiento.objects.filter(lenar_Indicador=id_)

    if contar_planes_mejo.count() == 0:
        instancia = Plan_Mejoramiento()
        instancia.lenar_Indicador = llave_prim
    else:
        instancia = contar_planes_mejo.first()

    if request.method == 'POST' :
        form = Plan_MejoramientoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Plan_Mejoramiento_list')
    else:
        form = Plan_MejoramientoForm(instance = instancia)
    return render(request, 'indicadores/Plan_Mejoramiento_form.html', {'form':form})

def Plan_MejoramientoEdit(request, id_):
    Plan_Mejoramiento_tem = Plan_Mejoramiento.objects.get(id=id_)
    if request.method =='GET':
        form = Plan_MejoramientoForm(instance = Plan_Mejoramiento_tem)
    else:
        form = Plan_MejoramientoForm(request.POST, instance = Plan_Mejoramiento_tem)
        if form.is_valid():
            form.save()
        return redirect('Plan_Mejoramiento_list')
    return render(request,'indicadores/Plan_Mejoramiento_form.html', {'form':form})

def Plan_MejoramientoElim(request, id_):
    Plan_Mejoramiento_tem = Plan_Mejoramiento.objects.get(id = id_)
    Plan_Mejoramiento_tem.delete()
    return redirect('Plan_Mejoramiento_list')



# INICIO VISTAS PARA Seguimiento de la Eficacia
# Estado_Avance
def Estado_AvanceList(request):
    Estado_Avance1 = Estado_Avance.objects.all()
    contexto = {'Estado_Avances':Estado_Avance1}
    return render(request, 'indicadores/Estado_Avance_list.html', contexto) 

def Estado_AvanceCrear(request):
    if request.method == 'POST' :
        form = Estado_AvanceForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Estado_Avance_list')
    else:
        form = Estado_AvanceForm()
    return render(request, 'indicadores/Estado_Avance_form.html', {'form':form})

def Estado_AvanceEdit(request, id_):

    Estado_Avance_tem = Estado_Avance.objects.get(id=id_)
    if request.method =='GET':
        form = Estado_AvanceForm(instance = Estado_Avance_tem)
    else:
        form = Estado_AvanceForm(request.POST, instance = Estado_Avance_tem)
        if form.is_valid():
            form.save()
        return redirect('Estado_Avance_list')
    return render(request,'indicadores/Estado_Avance_form.html', {'form':form})

def Estado_AvanceElim(request, id_):
    Estado_Avance_tem = Estado_Avance.objects.get(id = id_)
    Estado_Avance_tem.delete()
    return redirect('Estado_Avance_list')

def Lista_Plan_Mejoramiento(request):
    plan_Mejoramiento = request.GET.get('plan_Mejoramiento')
    plan = Plan_Mejoramiento.objects.get(id=plan_Mejoramiento)
    print("este es el plan" , plan.titulo)
    return render(request,'indicadores/listas_dependientes/Form_Plan_Mejoramiento.html',{'plan_mejora':plan} )


# Estado_Accion
def Estado_AccionList(request):
    Estado_Accion1 = Estado_Accion.objects.all()
    contexto = {'Estado_Accions':Estado_Accion1}
    return render(request, 'indicadores/Estado_Accion_list.html', contexto) 

def Estado_AccionCrear(request):

    if request.method == 'POST' :
        form = Estado_AccionForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Estado_Accion_list')
    else:
        form = Estado_AccionForm()
    return render(request, 'indicadores/Estado_Accion_form.html', {'form':form})

def Estado_AccionEdit(request, id_):

    Estado_Accion_tem = Estado_Accion.objects.get(id=id_)
    if request.method =='GET':
        form = Estado_AccionForm(instance = Estado_Accion_tem)
    else:
        form = Estado_AccionForm(request.POST, instance = Estado_Accion_tem)
        if form.is_valid():
            form.save()
        return redirect('Estado_Accion_list')
    return render(request,'indicadores/Estado_Accion_form.html', {'form':form})

def Estado_AccionElim(request, id_):
    Estado_Accion_tem = Estado_Accion.objects.get(id = id_)
    Estado_Accion_tem.delete()
    return redirect('Estado_Accion_list')


# Oportunidad_Ejecucion
def Oportunidad_EjecucionList(request):
    Oportunidad_Ejecucion1 = Oportunidad_Ejecucion.objects.all()
    contexto = {'Oportunidad_Ejecucions':Oportunidad_Ejecucion1}
    return render(request, 'indicadores/Oportunidad_Ejecucion_list.html', contexto) 

def Oportunidad_EjecucionCrear(request):
    if request.method == 'POST' :
        form = Oportunidad_EjecucionForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Oportunidad_Ejecucion_list')
    else:
        form = Oportunidad_EjecucionForm()
    return render(request, 'indicadores/Oportunidad_Ejecucion_form.html', {'form':form})

def Oportunidad_EjecucionEdit(request, id_):

    Oportunidad_Ejecucion_tem = Oportunidad_Ejecucion.objects.get(id=id_)
    if request.method =='GET':
        form = Oportunidad_EjecucionForm(instance = Oportunidad_Ejecucion_tem)
    else:
        form = Oportunidad_EjecucionForm(request.POST, instance = Oportunidad_Ejecucion_tem)
        if form.is_valid():
            form.save()
        return redirect('Oportunidad_Ejecucion_list')
    return render(request,'indicadores/Oportunidad_Ejecucion_form.html', {'form':form})

def Oportunidad_EjecucionElim(request, id_):
    Oportunidad_Ejecucion_tem = Oportunidad_Ejecucion.objects.get(id = id_)
    Oportunidad_Ejecucion_tem.delete()
    return redirect('Oportunidad_Ejecucion_list')


# Porcentaje_Avance
def Porcentaje_AvanceList(request):
    Porcentaje_Avance1 = Porcentaje_Avance.objects.all()
    contexto = {'Porcentaje_Avances':Porcentaje_Avance1}
    return render(request, 'indicadores/Porcentaje_Avance_list.html', contexto) 

def Porcentaje_AvanceCrear(request):

    if request.method == 'POST' :
        form = Porcentaje_AvanceForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Porcentaje_Avance_list')
    else:
        form = Porcentaje_AvanceForm()
    return render(request, 'indicadores/Porcentaje_Avance_form.html', {'form':form})

def Porcentaje_AvanceEdit(request, id_):

    Porcentaje_Avance_tem = Porcentaje_Avance.objects.get(id=id_)
    if request.method =='GET':
        form = Porcentaje_AvanceForm(instance = Porcentaje_Avance_tem)
    else:
        form = Porcentaje_AvanceForm(request.POST, instance = Porcentaje_Avance_tem)
        if form.is_valid():
            form.save()
        return redirect('Porcentaje_Avance_list')
    return render(request,'indicadores/Porcentaje_Avance_form.html', {'form':form})

def Porcentaje_AvanceElim(request, id_):
    Porcentaje_Avance_tem = Porcentaje_Avance.objects.get(id = id_)
    Porcentaje_Avance_tem.delete()
    return redirect('Porcentaje_Avance_list')


# Estado_Hallazgo
def Estado_HallazgoList(request):
    Estado_Hallazgo1 = Estado_Hallazgo.objects.all()
    contexto = {'Estado_Hallazgos':Estado_Hallazgo1}
    return render(request, 'indicadores/Estado_Hallazgo_list.html', contexto) 

def Estado_HallazgoCrear(request):

    if request.method == 'POST' :
        form = Estado_HallazgoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Estado_Hallazgo_list')
    else:
        form = Estado_HallazgoForm()
    return render(request, 'indicadores/Estado_Hallazgo_form.html', {'form':form})

def Estado_HallazgoEdit(request, id_):

    Estado_Hallazgo_tem = Estado_Hallazgo.objects.get(id=id_)
    if request.method =='GET':
        form = Estado_HallazgoForm(instance = Estado_Hallazgo_tem)
    else:
        form = Estado_HallazgoForm(request.POST, instance = Estado_Hallazgo_tem)
        if form.is_valid():
            form.save()
        return redirect('Estado_Hallazgo_list')
    return render(request,'indicadores/Estado_Hallazgo_form.html', {'form':form})

def Estado_HallazgoElim(request, id_):
    Estado_Hallazgo_tem = Estado_Hallazgo.objects.get(id = id_)
    Estado_Hallazgo_tem.delete()
    return redirect('Estado_Hallazgo_list')




# Seguimiento_Eficacia
def Seguimiento_EficaciaList(request):
    Seguimiento_Eficacia1 = Seguimiento_Eficacia.objects.all()
    contexto = {'Seguimiento_Eficacias':Seguimiento_Eficacia1}
    return render(request, 'indicadores/Seguimiento_Eficacia_list.html', contexto) 

def Seguimiento_EficaciaCrear(request):
    if request.method == 'POST' :
        form = Seguimiento_EficaciaForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Seguimiento_Eficacia_list')
    else:
        form = Seguimiento_EficaciaForm()
    return render(request, 'indicadores/Seguimiento_Eficacia_form.html', {'form':form})

def Seguimiento_EficaciaCrearDos(request, id_):
    llave_prim = Plan_Mejoramiento.objects.get(id =id_)
    
    contar_seguimiento_efica = Seguimiento_Eficacia.objects.filter(plan_Mejoramiento=id_).count()

    if contar_seguimiento_efica == 0:
        instancia = Seguimiento_Eficacia()
        instancia.plan_Mejoramiento = llave_prim
    else:
        instancia = contar_seguimiento_efica.first()

    if request.method == 'POST' :
        form = Seguimiento_EficaciaForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Seguimiento_Eficacia_list')
    else:
        form = Seguimiento_EficaciaForm(instance = instancia)
    return render(request, 'indicadores/Seguimiento_Eficacia_form.html', {'form':form})

def Seguimiento_EficaciaEdit(request, id_):

    Seguimiento_Eficacia_tem = Seguimiento_Eficacia.objects.get(id=id_)
    if request.method =='GET':
        form = Seguimiento_EficaciaForm(instance = Seguimiento_Eficacia_tem)
    else:
        form = Seguimiento_EficaciaForm(request.POST, instance = Seguimiento_Eficacia_tem)
        if form.is_valid():
            form.save()
        return redirect('Seguimiento_Eficacia_list')
    return render(request,'indicadores/Seguimiento_Eficacia_form.html', {'form':form})

def Seguimiento_EficaciaElim(request, id_):
    Seguimiento_Eficacia_tem = Seguimiento_Eficacia.objects.get(id = id_)
    Seguimiento_Eficacia_tem.delete()
    return redirect('Seguimiento_Eficacia_list')

#listas para los selects deendientes
def Lista_Estado_Accion(request):
    estado_Avance = request.GET.get('estado_Avance')
    estado_Accion1 = Estado_Accion.objects.filter(estado_Avance=estado_Avance)
    return render(request,'indicadores/listas_dependientes/Lista_Estado_Accion.html',{'estado_Accions':estado_Accion1})

def Lista_Estado_Hallazgo(request):
    estado_Avance = request.GET.get('estado_Avance')
    estado_Hallazgo1 = Estado_Hallazgo.objects.filter(estado_Avance=estado_Avance)
    return render(request,'indicadores/listas_dependientes/Lista_Estado_Hallazgo.html',{'estado_Hallazgos':estado_Hallazgo1})

def Lista_Porcentaje_Avance(request):
    estado_Avance = request.GET.get('estado_Avance')
    porcentaje_Avance1 = Porcentaje_Avance.objects.filter(estado_Avance=estado_Avance)
    return render(request,'indicadores/listas_dependientes/Lista_Porcentaje_Avance.html',{'porcentaje_Avances':porcentaje_Avance1})



# Parametro_Segui_Eficacia
def Parametro_Segui_EficaciaList(request):
    Parametro_Segui_Eficacia1 = Parametro_Segui_Eficacia.objects.all()
    contexto = {'Parametro_Segui_Eficacias':Parametro_Segui_Eficacia1}
    return render(request, 'indicadores/Parametro_Segui_Eficacia_list.html', contexto) 

def Parametro_Segui_EficaciaCrear(request):
    if request.method == 'POST' :
        form = Parametro_Segui_EficaciaForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Parametro_Segui_Eficacia_list')
    else:
        form = Parametro_Segui_EficaciaForm()
    return render(request, 'indicadores/Parametro_Segui_Eficacia_form.html', {'form':form})

def Parametro_Segui_EficaciaEdit(request, id_):

    Parametro_Segui_Eficacia_tem = Parametro_Segui_Eficacia.objects.get(id=id_)
    if request.method =='GET':
        form = Parametro_Segui_EficaciaForm(instance = Parametro_Segui_Eficacia_tem)
    else:
        form = Parametro_Segui_EficaciaForm(request.POST, instance = Parametro_Segui_Eficacia_tem)
        if form.is_valid():
            form.save()
        return redirect('Parametro_Segui_Eficacia_list')
    return render(request,'indicadores/Parametro_Segui_Eficacia_form.html', {'form':form})

def Parametro_Segui_EficaciaElim(request, id_):
    Parametro_Segui_Eficacia_tem = Parametro_Segui_Eficacia.objects.get(id = id_)
    Parametro_Segui_Eficacia_tem.delete()
    return redirect('Parametro_Segui_Eficacia_list')



# Unidad_Medida
def Unidad_MedidaList(request):
    Unidad_Medida1 = Unidad_Medida.objects.all()
    contexto = {'Unidad_Medidas':Unidad_Medida1}
    return render(request, 'indicadores/Unidad_Medida_list.html', contexto) 

def Unidad_MedidaCrear(request):
    if request.method == 'POST':
        form = Unidad_MedidaForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Unidad_Medida_list')
    else:
        form = Unidad_MedidaForm()
    return render(request, 'indicadores/Unidad_Medida_form.html', {'form':form})

def Unidad_MedidaEdit(request, id_):

    Unidad_Medida_tem = Unidad_Medida.objects.get(id=id_)
    if request.method =='GET':
        form = Unidad_MedidaForm(instance = Unidad_Medida_tem)
    else:
        form = Unidad_MedidaForm(request.POST, instance = Unidad_Medida_tem)
        if form.is_valid():
            form.save()
        return redirect('Unidad_Medida_list')
    return render(request,'indicadores/Unidad_Medida_form.html', {'form':form})

def Unidad_MedidaElim(request, id_):
    Unidad_Medida_tem = Unidad_Medida.objects.get(id = id_)
    Unidad_Medida_tem.delete()
    return redirect('Unidad_Medida_list')




# Cargo
def CargoList(request):
    Cargo1 = Cargo.objects.all()
    contexto = {'Cargos':Cargo1}
    return render(request, 'indicadores/Cargo_list.html', contexto) 

def CargoCrear(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Cargo_list')
    else:
        form = CargoForm()
    return render(request, 'indicadores/Cargo_form.html', {'form':form})

def CargoEdit(request, id_):

    Cargo_tem = Cargo.objects.get(id=id_)
    if request.method =='GET':
        form = CargoForm(instance = Cargo_tem)
    else:
        form = CargoForm(request.POST, instance = Cargo_tem)
        if form.is_valid():
            form.save()
        return redirect('Cargo_list')
    return render(request,'indicadores/Cargo_form.html', {'form':form})

def CargoElim(request, id_):
    Cargo_tem = Cargo.objects.get(id = id_)
    Cargo_tem.delete()
    return redirect('Cargo_list')



# Norma
def NormaList(request):
    Norma1 = Norma.objects.all()
    contexto = {'Normas':Norma1}
    return render(request, 'indicadores/Norma_list.html', contexto) 

def NormaCrear(request):
    if request.method == 'POST':
        form = NormaForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Norma_list')
    else:
        form = NormaForm()
    return render(request, 'indicadores/Norma_form.html', {'form':form})

def NormaEdit(request, id_):

    Norma_tem = Norma.objects.get(id=id_)
    if request.method =='GET':
        form = NormaForm(instance = Norma_tem)
    else:
        form = NormaForm(request.POST, instance = Norma_tem)
        if form.is_valid():
            form.save()
        return redirect('Norma_list')
    return render(request,'indicadores/Norma_form.html', {'form':form})

def NormaElim(request, id_):
    Norma_tem = Norma.objects.get(id = id_)
    Norma_tem.delete()
    return redirect('Norma_list')



# Nivel_Referencia
def Nivel_ReferenciaList(request):
    Nivel_Referencia1 = Nivel_Referencia.objects.all()
    contexto = {'Nivel_Referencias':Nivel_Referencia1}
    return render(request, 'indicadores/Nivel_Referencia_list.html', contexto) 

def Nivel_ReferenciaCrear(request):
    if request.method == 'POST':
        form = Nivel_ReferenciaForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Nivel_Referencia_list')
    else:
        form = Nivel_ReferenciaForm()
    return render(request, 'indicadores/Nivel_Referencia_form.html', {'form':form})

def Nivel_ReferenciaEdit(request, id_):

    Nivel_Referencia_tem = Nivel_Referencia.objects.get(id=id_)
    if request.method =='GET':
        form = Nivel_ReferenciaForm(instance = Nivel_Referencia_tem)
    else:
        form = Nivel_ReferenciaForm(request.POST, instance = Nivel_Referencia_tem)
        if form.is_valid():
            form.save()
        return redirect('Nivel_Referencia_list')
    return render(request,'indicadores/Nivel_Referencia_form.html', {'form':form})

def Nivel_ReferenciaElim(request, id_):
    Nivel_Referencia_tem = Nivel_Referencia.objects.get(id = id_)
    Nivel_Referencia_tem.delete()
    return redirect('Nivel_Referencia_list')




# Proceso
def ProcesoList(request):
    Proceso1 = Proceso.objects.all()
    contexto = {'Procesos':Proceso1}
    return render(request, 'indicadores/Proceso_list.html', contexto) 

def ProcesoCrear(request):
    if request.method == 'POST':
        form = ProcesoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Proceso_list')
    else:
        form = ProcesoForm()
    return render(request, 'indicadores/Proceso_form.html', {'form':form})

def ProcesoEdit(request, id_):

    Proceso_tem = Proceso.objects.get(id=id_)
    if request.method =='GET':
        form = ProcesoForm(instance = Proceso_tem)
    else:
        form = ProcesoForm(request.POST, instance = Proceso_tem)
        if form.is_valid():
            form.save()
        return redirect('Proceso_list')
    return render(request,'indicadores/Proceso_form.html', {'form':form})

def ProcesoElim(request, id_):
    Proceso_tem = Proceso.objects.get(id = id_)
    Proceso_tem.delete()
    return redirect('Proceso_list')


# Tipo_Proc
def Tipo_ProcList(request):
    Tipo_Proc1 = Tipo_Proc.objects.all()
    contexto = {'Tipo_Procs':Tipo_Proc1}
    return render(request, 'indicadores/Tipo_Proc_list.html', contexto) 

def Tipo_ProcCrear(request):
    if request.method == 'POST' :
        form = Tipo_ProcForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('Tipo_Proc_list')
    else:
        form = Tipo_ProcForm()
    return render(request, 'indicadores/Tipo_Proc_form.html', {'form':form})

def Tipo_ProcEdit(request, id_):

    Tipo_Proc_tem = Tipo_Proc.objects.get(id=id_)
    if request.method =='GET':
        form = Tipo_ProcForm(instance = Tipo_Proc_tem)
    else:
        form = Tipo_ProcForm(request.POST, instance = Tipo_Proc_tem)
        if form.is_valid():
            form.save()
        return redirect('Tipo_Proc_list')
    return render(request,'indicadores/Tipo_Proc_form.html', {'form':form})

def Tipo_ProcElim(request, id_):
    Tipo_Proc_tem = Tipo_Proc.objects.get(id = id_)
    Tipo_Proc_tem.delete()
    return redirect('Tipo_Proc_list')
