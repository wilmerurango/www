from django import forms
from Apps.Costo.models import *

class ThirdForm(forms.ModelForm):
    class Meta:
        model = Third

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })