from django.db import models

class Driver(models.Model):
    name = models.CharField('Nombre del Driver', max_length = 100, null = True, blank = False)
    description = models.TextField('Descripción', null = True, blank = False)


#se crea una twbla parta almacenar a los terceros registrados en la contabilidad
class Third(models.Model):

    cedula = 'Cedula'
    nit = 'NIT'
    passport = 'Pasaporte'
    typ_id = [
        (cedula, 'Cedula'),
        (nit, 'NIT'),
        (passport, 'Pasaporte'),
    ]

    type_id = models.CharField('Tipo Identificación',max_length = 15, choices=typ_id, default=cedula)
    number_id = models.CharField('Numero de Identificación', max_length = 15, null=True, blank=False)
    name = models.CharField('Nombres', max_length = 100, null = True, blank = False)
    last_name = models.CharField('Apellidos', max_length = 100, null = True, blank = True)
    email = models.EmailField('E-mail', blank = True)
    direction = models.CharField('Dirección', max_length = 100, null = True, blank = True)
    telefon = models.CharField('Telefono', max_length = 15, blank = True)

    def __str__(self):
       return '%s %s' % (self.name, self.Apellidos)

class ParentCostCenter(models.Model):
    code = models.CharField('Código Centro de Costo', max_length = 100, null = True, blank = False)
    name = models.CharField('Nombre Centro de Costo', max_length = 100, null = True, blank = False)
    
class ChildCostCenter(models.Model):
    parentCostCenter = models.ForeignKey(ParentCostCenter,verbose_name='Centro de Costo Hijo', on_delete = models.PROTECT, null=True, blank = False)
    code = models.CharField('Código Centro de Costo', max_length = 100, null = True, blank = False)
    name = models.CharField('Nombre Centro de Costo', max_length = 100, null = True, blank = False)

class Causation(models.Model):
    third = models.ForeignKey(Third, verbose_name='Grupo General', on_delete = models.PROTECT, null=True, blank = False)
    value = models.FloatField('Valor a causar')
    account = models.CharField('Cuenta Contable', max_length = 20, null=True, blank = False)


class Service(models.Model):
    fijo = 'Fijo'
    variable = 'Variable'
    fixvar = [
        (fijo, 'Fijo'),
        (variable, 'Variable'),
    ]

    third = models.ForeignKey(Third,verbose_name='Tercero', on_delete = models.PROTECT, null=True, blank = False)
    name = models.CharField('Nombre Servicio', max_length = 100, null = True, blank = False)
    driver = models.ForeignKey(Driver, verbose_name='Driver de Distribución', on_delete = models.PROTECT, null=True, blank = False)
    fixedVariable = models.CharField('Fijo o Variable', choices=fixvar, max_length=8, default= fijo)


