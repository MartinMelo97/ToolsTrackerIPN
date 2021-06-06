from django import forms
from .models import WorkerUser

user_type_choices_dropdown = (
    ('', 'Selecciona:'), ('true', 'Usuario Supervisor'), ('false', 'Usuario Técnico')
)

class WorkerUserForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre(s)', required=True)
    last_name = forms.CharField(label='Apellidos', required=True)
    username = forms.CharField(label='Nombre de Usuario (Sólo lectura)', widget=forms.TextInput(attrs={'readonly': True}))
    phone_number = forms.CharField(label='Número telefónico')
    email = forms.CharField(widget=forms.EmailInput(), label='Correo Electrónico')
    job_title = forms.CharField(label='Puesto')
    rest_time = forms.CharField(label = 'Descanso')
    is_staff = forms.BooleanField(required=False)
    is_supervisor = forms.ChoiceField(choices=user_type_choices_dropdown, label='Selecciona tipo de usuario')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        model = WorkerUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'job_title', 'rest_time', 'is_supervisor', 'is_staff', 'password')

class WorkerUserFormEdit(forms.ModelForm):
    first_name = forms.CharField(label='Nombre(s)', required=True)
    last_name = forms.CharField(label='Apellidos', required=True)
    # username = forms.CharField(label='Nombre de Usuario (Sólo lectura)', widget=forms.TextInput(attrs={'readonly': True}))
    phone_number = forms.CharField(label='Número telefónico')
    email = forms.CharField(widget=forms.EmailInput(), label='Correo Electrónico')
    job_title = forms.CharField(label='Puesto')
    rest_time = forms.CharField(label = 'Descanso')
    is_staff = forms.BooleanField(required=False)
    is_supervisor = forms.ChoiceField(choices=user_type_choices_dropdown, label='Selecciona tipo de usuario')
    class Meta:
        model = WorkerUser
        fields = (
            'first_name',
            'last_name',
        #    'username',
            'email',
            'phone_number',
            'job_title',
            'rest_time',
            'is_supervisor',
            'is_staff'
        )
