from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#esta clase representa el tipo de reporte que el usuario tiene dentro de la organizacion 
class Tipo_reporte(models.Model):
    nombre = models.CharField('Nombre del Tipo de Reporte', max_length = 60, null=True, blank=False)
    descripcion = models.TextField('Descripción del Tipo de Reporte',max_length = 200, null=True, blank=False)

    def __str__(self):
        return '%s' % (self.nombre)


#este la clase del grupo general que contiene a los indicadores, modificar el tipo de eliminacion cambiar modelo en cascada
class Grupo_general(models.Model):
    tipo_reporte = models.ForeignKey(Tipo_reporte, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Tipo de Reporte')
    nombre=models.CharField('Nombre del Grupo General',max_length = 60, null=True, blank=False)
    descripcion = models.TextField('Descripción',max_length = 200, null=True, blank = False)
    ente_control = models.CharField('Ente de Control',max_length = 200, null=True, blank = False)

    def __str__(self):
        return '%s' % (self.nombre)


#esta clase representa los subgrupos en donde se encuentran los indicadores
class Sub_grupo(models.Model):
    grupo_general = models.ForeignKey(Grupo_general, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Grupo General')
    nombre = models.CharField('Nombre del Sub-Grupo',max_length = 60, null=True, blank=False)
    descripcion = models.TextField('Descripción del Sub-Grupo',max_length = 200, null=True, blank = False)

    def __str__(self):
        return '%s' % (self.nombre)   


class Tipo_Proc(models.Model):
    nombre_tipo_proc = models.CharField('Tipo de Proceso', max_length=100, null = True)
    descrip_tipo_proc = models.TextField('Descripcion', null=True)
    
    def __str__(self):
        return '%s' % (self.nombre_tipo_proc)

class Cargo(models.Model):
    nombre_cargo = models.CharField('Nombre del Cargo', max_length=100, null = True)

    def __str__(self):
        return '%s' % (self.nombre_cargo)


#crear usuario
class Usuario(models.Model):
    master = 'Master'
    digitador = 'Digitador'
    lector = 'Lector'
    roles = [
        (master , 'Master'),
        (digitador , 'Digitador'),
        (lector , 'Lector'),
    ]
    user = models.OneToOneField(User, on_delete = models.PROTECT ,null=True)
    rol = models.CharField('Rol',max_length=50, choices=roles, default=lector, null=True)
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE, verbose_name='Cargo', null= True)


class Norma(models.Model):
    ley = 'Ley'
    decreto = 'Decreto'
    resolucion = 'Resolución'
    circular = 'Circular'
    acuerdo = 'Acuerdo'

    tipos = [
        (ley , 'Ley'),
        (decreto , 'Decreto'),
        (resolucion , 'Resolución'),
        (circular , 'Circular'),
        (acuerdo , 'Acuerdo'),
    ]

    nombre_norma = models.CharField('Nombre de la Norma', max_length=100, null = True)
    descripcion_norma = models.TextField('Descripción Norma', null=True)
    tipo_documento = models.CharField('Tipo de Documento', max_length=12, choices=tipos, default=ley)
    num_norma = models.CharField('Número Norma', max_length=10, null=True)
    fecha_emision = models.DateField('Fecha Emision', null=True)
    emitido = models.CharField('Emitido Por', max_length=100, null=True)
    estado = models.CharField('Estado', max_length=100, null=True)
    dir_url = models.CharField('Direccion URL', max_length=200, null=True)
    obs = models.TextField('Observación', null=True)

    def __str__(self):
        return '%s' % (self.nombre_norma)

# esta clase representa los procesos a los cuales estan atados cada uno de los indicadores
class Proceso(models.Model):
    tipo_Proc = models.ForeignKey(Tipo_Proc, on_delete = models.CASCADE, verbose_name='Tipo de Proceso', null= True)
    nombre_proceso = models.CharField('Nombre del Proceso', max_length=100, null = True, blank = False)
    objetivo = models.TextField('Objetivo del Proceso', null=True)
    alcance = models.TextField('Alcance del Proceso', null=True)
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE, verbose_name='Responsable', null= True)
    norma = models.ForeignKey(Norma, on_delete = models.CASCADE, verbose_name='Norma', null= True)
    codigo = models.CharField('Código del Proceso', max_length = 20, null=True)

    def __str__(self):
        return '%s' % (self.nombre_proceso)


class Actividad(models.Model):
    proceso = models.ForeignKey(Proceso,on_delete = models.CASCADE, verbose_name='Nombre del Proceso', null= True)
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE, verbose_name='Responsable', null= True)
    descrip_actividad = models.TextField('Actividad', null=True)
    

class Unidad_Medida(models.Model):
    unid_medida = models.CharField('Unidad de Medida',max_length = 20, null=True, blank=False)
    def __str__(self):
        return '%s' % (self.unid_medida)

class Nivel_Referencia(models.Model):
    nivel_ref = models.CharField('Nivel de Referencia', max_length = 70, null= True)

    def __str__(self): 
        return '%s' % (self.nivel_ref)

#esta clase representa cada uno de los indicadores 
class Indicador(models.Model):
    indicador_eficiencia = "Indicador de Eficiencia"
    indicador_eficacia = "Indicador de Eficacia"
    indicador_economia = "Indicador de Economía"
    indicador_calidad = "Indicador de Calidad"
    indicador_insumo = "Indicador de Insumo"
    indicador_proceso = "Indicador de Proceso" 
    indicador_producto = "Indicador de Producto"  
    indicador_resultado = "Indicador de Resultado"
    tipo_indicador = {
        (indicador_eficiencia ,"Indicador de Eficiencia"),
        (indicador_eficacia ,"Indicador de Eficacia"),
        (indicador_economia ,"Indicador de Economía"),
        (indicador_calidad ,"Indicador de Calidad"),
        (indicador_insumo ,"Indicador de Insumo"),
        (indicador_proceso ,"Indicador de Proceso"),
        (indicador_producto ,"Indicador de Producto"),
        (indicador_resultado ,"Indicador de Resultado"),
    }


    ascendente = "Ascendente"
    descendente = "Descendente"
    tipo_tendencia = {
        (ascendente ,"Ascendente"),
        (descendente ,"Descendente"),
    }

    diaria = "Diaria"
    mensual = "Mensual"
    periodo = {
        (diaria ,"Diaria"),
        (mensual ,"Mensual"),
    }

    metrica = 'metrica'
    indicador = 'indicador'
    tipo_metrica_inicador =[
        (metrica,'Métrica'),
        (indicador,'Indicador'),
    ]

    tipo_indi = models.CharField(max_length=30,choices=tipo_indicador, default=indicador_eficiencia)
    metrica_indicador = models.CharField(max_length=9,choices=tipo_metrica_inicador, default=indicador)
    grupo_general = models.ForeignKey(Grupo_general, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Grupo General')
    sub_grupo = models.ForeignKey(Sub_grupo, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Sub-Grupo')
    proceso = models.ForeignKey(Proceso, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Nombre del Proceso')
    nombre=models.CharField('Nombre del Indicador',max_length = 60, null=True, blank=False)
    nombre_numerador =  models.CharField('Nombre del Numerador',max_length = 80, null=True, blank=False)
    nombre_denominador = models.CharField('Nombre del Denominador',max_length = 80, null=True, blank=True)
    estandar = models.FloatField('Estandar del Indicador', null = True, blank = False, default = 1)
    unidad_Medida = models.ForeignKey(Unidad_Medida, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Unidad de Medida')
    nivel_Referencia = models.ForeignKey(Nivel_Referencia, null=True, blank = True, on_delete = models.CASCADE, verbose_name='Nivel de Referencia')
    objetivo = models.TextField('Objetivo', null=True)
    justificacion = models.TextField('Justificación', null=True)
    dominio = models.CharField('Dominio',max_length = 100, null=True, blank=False)
    tendencia_ascendente = models.CharField(max_length=11,choices=tipo_tendencia, default=ascendente)
    # periodicidad = models.CharField('Periodicidad', null = True, max_length=30)
    periodicidad = models.CharField(max_length=7,choices=periodo, default=mensual)
    cantidad_periodicidad = models.IntegerField('Cantidad Periodicidad', default = 1)
    fuente_num = models.CharField('Fuente Númerador', null = True, max_length=30)
    fuente_den = models.CharField('Fuente Denominador', null = True, blank=True, max_length=30)
    factor = models.FloatField('Factor',default=1)
    formula = models.CharField('Formula', null = True, max_length=200, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE, verbose_name='Sistema de Procesamineto', null= True)
    cargo = models.ForeignKey(Cargo, on_delete = models.CASCADE, verbose_name='Responsable', null= True)
    vigil_control = models.CharField('Vigiancia y Control', null = True, max_length=150)

    def __str__(self):
        return '%s' % (self.nombre)

#esta clase representa el llenado de cada indicador 
class Lenar_Indicador(models.Model):
    grupo_general = models.ForeignKey(Grupo_general, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Grupo General')
    sub_grupo = models.ForeignKey(Sub_grupo, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Sub-Grupo')
    indicador = models.ForeignKey(Indicador, null=True, blank = False, on_delete = models.CASCADE, verbose_name='Nombre del Indicador')
    valor_numerador = models.FloatField('Valor Numerador', null = True)
    valor_denominador = models.FloatField('Valor Denominador', null = True, default =1) 
    fecha_inicio = models.DateField('Fecha Inicio Periodo', blank = True , null = True)
    fecha_fin = models.DateField('Fecha Fin Periodo', blank = True, null = True)
    fecha = models.DateField('Fecha Registro del Indicador', blank = True, null = True)
    resultado = models.FloatField('Resultado', default= 0, blank = True)
    analisis = models.TextField('Analisis', null=True)
    observacion = models.TextField('Analisis', null=True)

    def __str__(self):
        return '%s' % (self.indicador.nombre) 


class Plan_Mejoramiento(models.Model):
    lenar_Indicador = models.ForeignKey(Lenar_Indicador, null= True, verbose_name = "Indicador", on_delete = models.CASCADE) 
    que = models.TextField('¿QUE?')
    para_que = models.TextField('¿PARA QUE?')
    quien = models.TextField('¿QUIEN?')
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_termin = models.DateField('Fecha de Terminación')
    donde = models.TextField('¿DONDE?')
    como = models.TextField('¿COMO?')
    titulo = models.CharField('Título', max_length=100, null = True)
    cuento_costara = models.FloatField('¿Cuanto Costará ?', null = True)

    def __str__(self):
        return '%s' % (self.titulo)

class Oportunidad_Ejecucion(models.Model):
    oport_ejec = models.CharField('Oportunidad de Ejecución', max_length = 70)

    def __str__(self):
        return '%s' % (self.oport_ejec)


class Estado_Avance(models.Model):
    estado = models.CharField('Nombre del Estado', max_length = 70)

    def __str__(self):
        return '%s' % (self.estado)


class Estado_Accion(models.Model):
    estado_Avance = models.ForeignKey(Estado_Avance, null= True, verbose_name = "Nombre del Estado", on_delete = models.CASCADE)
    accion = models.CharField('Nombre de la Acción', max_length = 20)

    def __str__(self):
        return '%s' % (self.accion)


class Porcentaje_Avance(models.Model):
    estado_Avance = models.ForeignKey(Estado_Avance, null= True, verbose_name = "Nombre del Estado", on_delete = models.CASCADE)
    porc_avance = models.CharField('Porcentaje de Avance', max_length = 20)

    def __str__(self):
        return '%s' % (self.porc_avance)

class Estado_Hallazgo(models.Model):
    estado_Avance = models.ForeignKey(Estado_Avance, null= True, verbose_name = "Nombre del Estado", on_delete = models.CASCADE)
    hallazgo = models.CharField('Nombre Hallazgo', max_length = 30)

    def __str__(self):
        return '%s' % (self.hallazgo)

class Seguimiento_Eficacia(models.Model):
    plan_Mejoramiento = models.ForeignKey(Plan_Mejoramiento, null= True, verbose_name = "Plan de Mejoramiento", on_delete = models.CASCADE) 
    reponsable  = models.CharField('Responsable', max_length = 70)
    soportes_evidencias = models.TextField('Soportes o Evidencias')
    estado_Avance = models.ForeignKey(Estado_Avance,verbose_name = "Estado de Avance", on_delete = models.CASCADE)
    estado_Accion = models.ForeignKey(Estado_Accion, verbose_name= "Estado de la Acción", on_delete = models.CASCADE)
    fecha_evaluacion = models.DateField('Fecha de Evaluacion o Cierre')
    oportunidad_Ejecucion = models.ForeignKey(Oportunidad_Ejecucion, verbose_name = "Oportunidad de Evacuación", on_delete = models.CASCADE)
    porcentaje_Avance = models.ForeignKey(Porcentaje_Avance, verbose_name = "Porcentaje de Avance", on_delete = models.CASCADE)
    estado_Hallazgo = models.ForeignKey(Estado_Hallazgo, verbose_name = "Estado del hallazgo", on_delete = models.CASCADE)
    observacion = models.TextField('Observaciones')

class Parametro_Segui_Eficacia(models.Model):
    estado_Avance = models.ForeignKey(Estado_Avance, null= True, verbose_name = "Nombre del Estado", on_delete = models.CASCADE)
    estado_Hallazgo = models.ForeignKey(Estado_Hallazgo, null= True, verbose_name = "Nombre Hallazgo", on_delete = models.CASCADE)
    estado_accion = models.ForeignKey(Estado_Accion, verbose_name= "Estado de la Acción", on_delete = models.CASCADE)
    porcentaje_avance = models.ForeignKey(Porcentaje_Avance, verbose_name = "Porcentaje de Avance", on_delete = models.CASCADE)

