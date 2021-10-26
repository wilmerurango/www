from django.urls import path
from indicador.views import *

urlpatterns = [
    path('index/', index, name='index'),

    #ESTOS SON LOS TIPOS DE REPORTE
    path('Tiporeporte_list/', Tipo_reporteList, name='Tipo_reporte_list'),
    path('Tiporeporte_crear/', Tipo_reporteCrear, name='Tipo_reporte_crear'),
    path('Tipo_reporte_edit/<int:id_>/',Tipo_reporteEdit, name = 'Tipo_reporte_edit'),
    path('Tipo_reporte_elim/<int:id_>/',Tipo_reporteElim, name = 'Tipo_reporte_elim'),

    #ESTOS SON LOS Grupo_general
    path('Grupo_general_list/', Grupo_generalList, name='Grupo_general_list'),
    path('Grupo_general_crear/', Grupo_generalCrear, name='Grupo_general_crear'),
    path('Grupo_general_edit/<int:id_>/',Grupo_generalEdit, name = 'Grupo_general_edit'),
    path('Grupo_general_elim/<int:id_>/',Grupo_generalElim, name = 'Grupo_general_elim'),

    #ESTOS SON LOS Sub_grupo
    path('Sub_grupo_list/', Sub_grupoList, name='Sub_grupo_list'),
    path('Sub_grupo_crear/', Sub_grupoCrear, name='Sub_grupo_crear'),
    path('Sub_grupo_edit/<int:id_>/',Sub_grupoEdit, name = 'Sub_grupo_edit'),
    path('Sub_grupo_elim/<int:id_>/',Sub_grupoElim, name = 'Sub_grupo_elim'),

    #ESTOS SON LOS Indicador
    path('Indicador_list/', IndicadorList, name='Indicador_list'),
    path('Indicador_crear/', IndicadorCrear, name='Indicador_crear'),
    path('Indicador_edit/<int:id_>/',IndicadorEdit, name = 'Indicador_edit'),
    path('Indicador_elim/<int:id_>/',IndicadorElim, name = 'Indicador_elim'),

    #ESTOS SON LOS Lenar_Indicador
    path('Lenar_Indicador_list/', Lenar_IndicadorList, name='Lenar_Indicador_list'),
    path('Lenar_Indicador_crear/', Lenar_IndicadorCrear, name='Lenar_Indicador_crear'),
    path('Lenar_Indicador_edit/<int:id_>/',Lenar_IndicadorEdit, name = 'Lenar_Indicador_edit'),
    path('Lenar_Indicador_edit_form/<int:id_>/',Lenar_IndicadorEdit_Form, name = 'Lenar_Indicador_edit_form'),
    path('Lenar_Indicador_edit_Sin_Efecto/<int:id_>/',Lenar_IndicadorEdit_Sin_Efecto, name = 'Lenar_Indicador_edit_sin_efecto'),
    path('Lenar_Indicador_elim/<int:id_>/',Lenar_IndicadorElim, name = 'Lenar_Indicador_elim'),
    path('Lista_sub_grupo/',Lista_sub_grupo, name = 'Lista_sub_grupo_ajax'),
    path('Lista_indicador/',Lista_Indicador, name = 'Lista_Indicador_ajax'),
    # Estas son las vistas para mostrar campos ocultos
    path('Lenar_Indicador_numerador/',Lenar_Indicador_numerador, name = 'Lenar_Indicador_numerador'),
    path('Lenar_Indicador_unidad/',Lenar_Indicador_unidad, name = 'Lenar_Indicador_unidad'),

    #ESTOS SON LOS Plan_Mejoramiento
    path('Plan_Mejoramiento_list/', Plan_MejoramientoList, name='Plan_Mejoramiento_list'),
    path('Plan_Mejoramiento_crear/<int:id_>', Plan_MejoramientoCrear, name='Plan_Mejoramiento_crear'),
    path('Plan_Mejoramiento_edit/<int:id_>/',Plan_MejoramientoEdit, name = 'Plan_Mejoramiento_edit'),
    path('Plan_Mejoramiento_elim/<int:id_>/',Plan_MejoramientoElim, name = 'Plan_Mejoramiento_elim'),


    #ESTOS SON LOS Estado_Avance
    path('Estado_Avance_list/', Estado_AvanceList, name='Estado_Avance_list'),
    path('Estado_Avance_crear/', Estado_AvanceCrear, name='Estado_Avance_crear'),
    path('Estado_Avance_edit/<int:id_>/',Estado_AvanceEdit, name = 'Estado_Avance_edit'),
    path('Estado_Avance_elim/<int:id_>/',Estado_AvanceElim, name = 'Estado_Avance_elim'),

    #ESTOS SON LOS Estado_Accion
    path('Estado_Accion_list/', Estado_AccionList, name='Estado_Accion_list'),
    path('Estado_Accion_crear/', Estado_AccionCrear, name='Estado_Accion_crear'),
    path('Estado_Accion_edit/<int:id_>/',Estado_AccionEdit, name = 'Estado_Accion_edit'),
    path('Estado_Accion_elim/<int:id_>/',Estado_AccionElim, name = 'Estado_Accion_elim'),

    #ESTOS SON LOS Oportunidad_Ejecucion
    path('Oportunidad_Ejecucion_list/', Oportunidad_EjecucionList, name='Oportunidad_Ejecucion_list'),
    path('Oportunidad_Ejecucion_crear/', Oportunidad_EjecucionCrear, name='Oportunidad_Ejecucion_crear'),
    path('Oportunidad_Ejecucion_edit/<int:id_>/',Oportunidad_EjecucionEdit, name = 'Oportunidad_Ejecucion_edit'),
    path('Oportunidad_Ejecucion_elim/<int:id_>/',Oportunidad_EjecucionElim, name = 'Oportunidad_Ejecucion_elim'),

    #ESTOS SON LOS Porcentaje_Avance
    path('Porcentaje_Avance_list/', Porcentaje_AvanceList, name='Porcentaje_Avance_list'),
    path('Porcentaje_Avance_crear/', Porcentaje_AvanceCrear, name='Porcentaje_Avance_crear'),
    path('Porcentaje_Avance_edit/<int:id_>/',Porcentaje_AvanceEdit, name = 'Porcentaje_Avance_edit'),
    path('Porcentaje_Avance_elim/<int:id_>/',Porcentaje_AvanceElim, name = 'Porcentaje_Avance_elim'),

    #ESTOS SON LOS Estado_Hallazgo
    path('Estado_Hallazgo_list/', Estado_HallazgoList, name='Estado_Hallazgo_list'),
    path('Estado_Hallazgo_crear/', Estado_HallazgoCrear, name='Estado_Hallazgo_crear'),
    path('Estado_Hallazgo_edit/<int:id_>/',Estado_HallazgoEdit, name = 'Estado_Hallazgo_edit'),
    path('Estado_Hallazgo_elim/<int:id_>/',Estado_HallazgoElim, name = 'Estado_Hallazgo_elim'),

    #ESTOS SON LOS Seguimiento_Eficacia
    path('Seguimiento_Eficacia_list/', Seguimiento_EficaciaList, name='Seguimiento_Eficacia_list'),
    path('Seguimiento_Eficacia_crear/', Seguimiento_EficaciaCrear, name='Seguimiento_Eficacia_crear'),
    path('Seguimiento_Eficacia_crear_dos/<int:id_>/', Seguimiento_EficaciaCrearDos, name='Seguimiento_Eficacia_crear_dos'),
    path('Seguimiento_Eficacia_edit/<int:id_>/',Seguimiento_EficaciaEdit, name = 'Seguimiento_Eficacia_edit'),
    path('Seguimiento_Eficacia_elim/<int:id_>/',Seguimiento_EficaciaElim, name = 'Seguimiento_Eficacia_elim'),
    path('Lista_Estado_Accion/',Lista_Estado_Accion, name = 'Lista_estado_Accion_ajax'),
    path('Lista_Estado_Hallazgo/',Lista_Estado_Hallazgo, name = 'Lista_estado_Hallazgo_ajax'),
    path('Lista_Porcentaje_Avance/',Lista_Porcentaje_Avance, name = 'Lista_porcentaje_Avance_ajax'),
    path('Lista_Plan_Mejoramiento/',Lista_Plan_Mejoramiento, name = 'Lista_Plan_Mejoramiento_ajax'),


    # #ESTOS SON LOS Parametro_Segui_Eficacia
    path('Parametro_Segui_Eficacia_list/', Parametro_Segui_EficaciaList, name='Parametro_Segui_Eficacia_list'),
    path('Parametro_Segui_Eficacia_crear/', Parametro_Segui_EficaciaCrear, name='Parametro_Segui_Eficacia_crear'),
    path('Parametro_Segui_Eficacia_edit/<int:id_>/',Parametro_Segui_EficaciaEdit, name = 'Parametro_Segui_Eficacia_edit'),
    path('Parametro_Segui_Eficacia_elim/<int:id_>/',Parametro_Segui_EficaciaElim, name = 'Parametro_Segui_Eficacia_elim'),


    #Cargo
    path('Cargo_list/', CargoList, name='Cargo_list'),
    path('Cargo_crear/', CargoCrear, name='Cargo_crear'),
    path('Cargo_edit/<int:id_>/',CargoEdit, name = 'Cargo_edit'),
    path('Cargo_elim/<int:id_>/',CargoElim, name = 'Cargo_elim'),
    # path('Form_Edit_Cargo/<int:id_>/',Form_Edit_Cargo, name = 'Form_Edit_Cargo'),


    #Unidad_Medida
    path('Unidad_Medida_list/', Unidad_MedidaList, name='Unidad_Medida_list'),
    path('Unidad_Medida_crear/', Unidad_MedidaCrear, name='Unidad_Medida_crear'),
    path('Unidad_Medida_edit/<int:id_>/',Unidad_MedidaEdit, name = 'Unidad_Medida_edit'),
    path('Unidad_Medida_elim/<int:id_>/',Unidad_MedidaElim, name = 'Unidad_Medida_elim'),


    #Norma
    path('Norma_list/', NormaList, name='Norma_list'),
    path('Norma_crear/', NormaCrear, name='Norma_crear'),
    path('Norma_edit/<int:id_>/',NormaEdit, name = 'Norma_edit'),
    path('Norma_elim/<int:id_>/',NormaElim, name = 'Norma_elim'),

    #Nivel_Referencia
    path('Nivel_Referencia_list/', Nivel_ReferenciaList, name='Nivel_Referencia_list'),
    path('Nivel_Referencia_crear/', Nivel_ReferenciaCrear, name='Nivel_Referencia_crear'),
    path('Nivel_Referencia_edit/<int:id_>/',Nivel_ReferenciaEdit, name = 'Nivel_Referencia_edit'),
    path('Nivel_Referencia_elim/<int:id_>/',Nivel_ReferenciaElim, name = 'Nivel_Referencia_elim'),

    #ESTOS PROCESOS
    path('Proceso_list/', ProcesoList, name='Proceso_list'),
    path('Proceso_crear/', ProcesoCrear, name='Proceso_crear'),
    path('Proceso_edit/<int:id_>/',ProcesoEdit, name = 'Proceso_edit'),
    path('Proceso_elim/<int:id_>/',ProcesoElim, name = 'Proceso_elim'),

    #ESTOS SON LOS TIPOS DE PROCESO
    path('Tipo_Proc_list/', Tipo_ProcList, name='Tipo_Proc_list'),
    path('Tipo_Proc_crear/', Tipo_ProcCrear, name='Tipo_Proc_crear'),
    path('Tipo_Proc_edit/<int:id_>/',Tipo_ProcEdit, name = 'Tipo_Proc_edit'),
    path('Tipo_Proc_elim/<int:id_>/',Tipo_ProcElim, name = 'Tipo_Proc_elim'),

]    