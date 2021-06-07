from django import forms
from django.forms import fields
from django.forms.widgets import SelectDateWidget
from .models import WorkTool

class ToolForm(forms.ModelForm):
    name =  forms.CharField(label='Nombre de la Herramienta', required=True)
    name.widget.attrs.update({'class': 'form-control'})
    serial_number = forms.CharField(label='Número de serie', required=True)
    serial_number.widget.attrs.update({'class': 'form-control'})
    model = forms.CharField(label='Modelo', required=True)
    model.widget.attrs.update({'class': 'form-control'})
    has_been_in_mainteance = forms.BooleanField(label='¿Ha tenido mantenimiento?', required=False)
    mainteance_date = forms.DateField(
        label='Fecha de mantenimeinto',
        widget=forms.SelectDateWidget(years=range(2021, 2030))
    )
    mainteance_date.widget.attrs.update({'class': 'form-control'})
    is_in_maintain = forms.BooleanField(label='¿Está en mantenimiento?', required=False)
    specifications = forms.CharField(label='Características', required=False)
    specifications.widget.attrs.update({'class': 'form-control'})
    has_tracker = forms.BooleanField(label='Cuenta con rastreador', required=False)
    tracker_id=forms.CharField(label='ID del rastreador', required=False)
    tracker_id.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = WorkTool

        fields='__all__'
