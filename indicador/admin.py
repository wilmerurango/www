from django.contrib import admin

from indicador.models import *
# Register your models here.  
admin.site.register(Tipo_reporte)
admin.site.register(Grupo_general)
admin.site.register(Sub_grupo)
admin.site.register(Indicador)
admin.site.register(Lenar_Indicador)
admin.site.register(Tipo_Proc)
admin.site.register(Proceso)
admin.site.register(Plan_Mejoramiento)
admin.site.register(Oportunidad_Ejecucion)
admin.site.register(Estado_Avance)
admin.site.register(Estado_Accion)
admin.site.register(Porcentaje_Avance)
admin.site.register(Estado_Hallazgo)
admin.site.register(Seguimiento_Eficacia)
admin.site.register(Parametro_Segui_Eficacia)
admin.site.register(Cargo)
admin.site.register(Norma)
admin.site.register(Unidad_Medida)
admin.site.register(Nivel_Referencia)
admin.site.register(Usuario)