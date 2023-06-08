from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator, RegexValidator, EmailValidator

# Create your models here.


class Cargo_Postular(models.Model):
     cargo = models.CharField(max_length=25)

     def __str__(self):
         return self.cargo

nivel_educacion = [
    [0, "Basica Completa"],
    [1, "Media Completa"],
    [2, "Superior"]
]    

manejo_excel = [
    [0, "Basico"],
    [1, "Intermedio"],
    [2, "Alto"],
    [3, "Profesional"]
]

nivel_conocimientos = [
    [0, "De 0 a 2 años"],
    [1, "De 3 a 5 años"],
    [2, "De 6 a 8 años"],
    [3, "Sobre 9 años"]
]

comunas_santiago = [
    [0, "Santiago"],
    [1, "Providencia"],
    [2, "Las Condes"],
    [3, "La Florida"],
    [4, "Ñuñoa"],
    [5, "Vitacura"],
    [6, "Maipú"],
    [7, "Puente Alto"],
    [8, "La Reina"],
    [9, "Peñalolén"],
    [10, "Macul"],
    [11, "San Joaquín"],
    [12, "La Cisterna"],
    [13, "Independencia"],
    [14, "Cerrillos"],
    [15, "Renca"],
    [16, "Quinta Normal"],
    [17, "Lo Prado"],
    [18, "Pudahuel"]
]

class Postulacion(models.Model):
    nombre = models.CharField(max_length=15, verbose_name='Nombre', validators=[RegexValidator(regex=r'^[a-zA-Z]*$',message='El nombre solo debe contener letras')])
    ap_paterno = models.CharField(max_length=15, verbose_name='Apellido Paterno',validators=[RegexValidator(regex=r'^[a-zA-Z]*$',message='El apellido solo debe contener letras')])
    ap_materno = models.CharField(max_length=15, verbose_name='Apellido Materno',validators=[RegexValidator(regex=r'^[a-zA-Z]*$',message='El apellido solo debe contener letras')])
    comuna = models.IntegerField(choices=comunas_santiago, verbose_name='Comuna donde vives')
    edad = models.IntegerField(verbose_name='Edad',validators=[MinValueValidator(18, message='No puedes postular siendo menor de edad'),MaxValueValidator(100, message='La edad no puede ser mayor a 100.')])
    celular = PhoneNumberField(verbose_name='Celular',unique=True, help_text = "Ejemplo: +56 9 12345678  o  9 45216387")
    email = models.EmailField(verbose_name='Correo Electrónico',validators=[EmailValidator(message='Ingresa una dirección de correo electrónico válida.')])
    nivel_ed = models.IntegerField(choices=nivel_educacion, verbose_name='Nivel educacional')
    nivel_excel = models.IntegerField(choices=manejo_excel, verbose_name='Nivel de manejo en Excel')
    cargo = models.ForeignKey(Cargo_Postular, on_delete=models.PROTECT,verbose_name='Cargo a postular')
    experiencia = models.IntegerField(choices=nivel_conocimientos,verbose_name='Experiencia en el area')
    describir_experiencia = models.TextField(max_length=250,verbose_name='Describa su Experiencia', help_text='Máximo 250 caracteres.')
    cv = models.FileField(verbose_name='Adjuntar Currículum Vitae', upload_to="CVs",null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=["pdf","doc","docx"])])
    disponibilidad = models.BooleanField(verbose_name='Disponiblidad inmediata')
    fecha_postulacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Postulacion')


    def __str__(self):
         return self.nombre
    