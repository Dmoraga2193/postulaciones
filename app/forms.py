from django import forms
from .models import Postulacion, Cliente
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidators
from django.forms.forms import Form  
from django.forms import ValidationError
from django.forms.fields import EmailField  
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
    username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El usuario ya existe")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Este email ya existe")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Contraseñas no coinciden")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  

class CambiarContraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label= 'Nueva contraseña',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label= 'Confirmar contraseña',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))


class PerfilClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','region','ciudad','comuna','direccion','telefono','codigo_postal']