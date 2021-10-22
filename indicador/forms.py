from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
import datetime
from .models import *

class Tipo_reporteForm(forms.ModelForm):
    class Meta:
        model = Tipo_reporte

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Grupo_generalForm(forms.ModelForm):
    class Meta:
        model = Grupo_general
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Sub_grupoForm(forms.ModelForm):
    class Meta:
        model = Sub_grupo

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control form-control-solid form-control-lg',
                
            })

            if  self.fields[field] == "tendencia_ascendente":
                self.fields[field].widget.attrs.update({  
                    'type': 'checkbox',    
            })
        self.fields['metrica_indicador'].widget.attrs.update({ 'onchange': 'cambio_metrica_indicador()'})
        self.fields['sub_grupo'].queryset = Sub_grupo.objects.none()

        if 'grupo_general' in self.data:
            try:
                grupo_general_id = int(self.data.get('grupo_general'))
                self.fields['sub_grupo'].queryset = Sub_grupo.objects.filter(grupo_general_id=grupo_general_id).order_by('nombre')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_grupo'].queryset =  self.instance.grupo_general.sub_grupo_set.order_by('nombre')

class Lenar_IndicadorForm(forms.ModelForm):
    class Meta:
        model = Lenar_Indicador

        fields=(
            '__all__'
        )

    fecha_inicio = forms.DateField( 
                widget=forms.DateInput(
                    attrs={
                        "name":"start",
                        "placeholder":"Fecha Ini..",
                        "required":"",
                    }
                )
            )

    fecha_fin = forms.DateField( 
                widget=forms.DateInput(
                    attrs={
                        "name":"end",
                        "placeholder":"Fecha Fin..",
                        "required":"",
                    }
                )
            )


    fecha= forms.DateField(
                initial = datetime.datetime.now().strftime("%d/%m/%Y"),
                widget=forms.DateInput(
                    attrs={
                        "required":"",
                    }
                )          
            )

    

    # valor_numerador = forms.FloatField(initial=2000)

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'
        })
        # self.fields['indicador'].widget.attrs.update({ 'name': 'param', 'id':'kt_select2_1'})
        self.fields['valor_numerador'].widget.attrs.update({ 'onkeyup': 'resultado()'})
        self.fields['valor_denominador'].widget.attrs.update({ 'onkeyup': 'resultado()'})
        self.fields['fecha_inicio'].widget.attrs['readonly'] = True  
        self.fields['fecha_fin'].widget.attrs['readonly'] = True  
        self.fields['fecha'].widget.attrs['readonly'] = True  

        self.fields['sub_grupo'].queryset = Sub_grupo.objects.none()
        self.fields['indicador'].queryset = Indicador.objects.none()   

        if 'grupo_general' in self.data:
            try:
                grupo_general_id = int(self.data.get('grupo_general'))
                self.fields['sub_grupo'].queryset = Sub_grupo.objects.filter(grupo_general_id=grupo_general_id).order_by('nombre')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_grupo'].queryset =  self.instance.grupo_general.sub_grupo_set.order_by('nombre')

        if 'sub_grupo' in self.data:
            try:
                sub_grupo_id = int(self.data.get('sub_grupo'))
                self.fields['indicador'].queryset = Indicador.objects.filter(sub_grupo_id=sub_grupo_id).order_by('nombre')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['indicador'].queryset =  self.instance.sub_grupo.indicador_set.order_by('nombre')
            
class Plan_MejoramientoForm(forms.ModelForm):

    class Meta:
        model = Plan_Mejoramiento

        fields = (
            '__all__'
        )  

    fecha_inicio = forms.DateField( 
                widget=forms.DateInput(
                    attrs={
                        "id":"kt_datepicker_1",
                        "placeholder":"Fecha Inicio",
                        "required":"",
                        "data-date-format":"dd/mm/yyyy",
                    }
                )
            )

    fecha_termin = forms.DateField( 
                widget=forms.DateInput(
                    attrs={
                        "id":"kt_datepicker_1",
                        "placeholder":"Fecha Terminación",
                        "required":"",
                        "data-date-format":"dd/mm/yyyy",
                    }
                )
            )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

        self.fields['fecha_inicio'].widget.attrs['readonly'] = True  
        self.fields['fecha_termin'].widget.attrs['readonly'] = True  
        self.fields['lenar_Indicador'].widget.attrs['readonly'] = True

class Estado_AvanceForm(forms.ModelForm):
    class Meta:
        model = Estado_Avance

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Estado_AccionForm(forms.ModelForm):
    class Meta:
        model = Estado_Accion

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Oportunidad_EjecucionForm(forms.ModelForm):
    class Meta:
        model = Oportunidad_Ejecucion

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Porcentaje_AvanceForm(forms.ModelForm):
    class Meta:
        model = Porcentaje_Avance

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Estado_HallazgoForm(forms.ModelForm):
    class Meta:
        model = Estado_Hallazgo

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Seguimiento_EficaciaForm(forms.ModelForm):
    class Meta:
        model = Seguimiento_Eficacia

        fields =(
            '__all__'
        )

    fecha_evaluacion = forms.DateField(
                widget=forms.DateInput(
                    attrs={
                        "required":"",
                        "id":"kt_datepicker_5",
                        "data-date-format":"dd/mm/yyyy",
                    }
                )          
            )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

        self.fields['fecha_evaluacion'].widget.attrs['readonly'] = True  
        self.fields['estado_Accion'].queryset = Estado_Accion.objects.none()  
        self.fields['estado_Hallazgo'].queryset = Estado_Accion.objects.none()  
        self.fields['porcentaje_Avance'].queryset = Porcentaje_Avance.objects.none()
        
        if 'estado_Avance' in self.data:
            try:
                estado_Avance_id = int(self.data.get('estado_Avance'))
                self.fields['estado_Accion'].queryset = Estado_Accion.objects.filter(estado_Avance_id=estado_Avance_id)
                self.fields['estado_Hallazgo'].queryset = Estado_Hallazgo.objects.filter(estado_Avance_id=estado_Avance_id)
                self.fields['porcentaje_Avance'].queryset = Porcentaje_Avance.objects.filter(estado_Avance_id=estado_Avance_id)
            
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['estado_Accion'].queryset =  self.instance.estado_Avance.estado_Accion_set
            self.fields['estado_Hallazgo'].queryset =  self.instance.estado_Avance.estado_Hallazgo_set
            self.fields['porcentaje_Avance'].queryset =  self.instance.estado_Avance.porcentaje_Avance_set

class Parametro_Segui_EficaciaForm(forms.ModelForm):

    class Meta:
        model = Parametro_Segui_Eficacia

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class CargoForm(forms.ModelForm):

    class Meta:
        model = Cargo

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class NormaForm(forms.ModelForm):

    class Meta:
        model = Norma

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
        self.fields['descripcion_norma'].widget.attrs.update({
            'style': 'margin-top: 0px; margin-bottom: 0px; height: 187px;'
        })

class Nivel_ReferenciaForm(forms.ModelForm):

    class Meta:
        model = Nivel_Referencia

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Unidad_MedidaForm(forms.ModelForm):

    class Meta:
        model = Unidad_Medida

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class ProcesoForm(forms.ModelForm):

    class Meta:
        model = Proceso

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class Tipo_ProcForm(forms.ModelForm):

    class Meta:
        model = Tipo_Proc

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields =(
            'rol',
            'cargo',
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields=(
            # '__all__'
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
        self.fields['password'].widget.attrs.update({  
                'type': 'password'  
            })