from django import forms
from .models import Postulacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidators
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

class PostulacionForm(forms.ModelForm):

    email = forms.EmailField(max_length=50,help_text="Ejemplo: arteplastica@dominio.cl")
    cv = forms.FileField(required=False, validators=[MaxSizeFileValidators(max_file_size=5)],help_text="Adjunte su Currículum Vitae(Opcional): Archivos compatibles (PDF,DOC,DOCX) con un tamaño máximo de 5MB")
    celular = PhoneNumberField()
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        existe = Postulacion.objects.filter(email__iexact=email).exists()

        if existe:
            raise ValidationError("Este correo ya fue ingresado anteriormente.")
        
        return email
    
    def clean_phone(self):
        celular = self.cleaned_data["celular"]
        existe = Postulacion.objects.filter(celular__iexact=celular).exists()

        if existe:
            raise ValidationError("Ya existe Postulación con este Celular.")
        
        return celular

    class Meta:
        model = Postulacion
        #fields = '__all__'        
        fields = ['nombre','ap_paterno','ap_materno','comuna','edad','celular','email','nivel_ed','nivel_excel','cargo','experiencia','describir_experiencia','cv','disponibilidad']
                
class CustomUserCreationForm(UserCreationForm):  
    
    class Meta:
        model = User
        fields = ["username","password1","password2"]