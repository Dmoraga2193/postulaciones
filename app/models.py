from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator, RegexValidator, EmailValidator
from django.contrib.auth.models import User

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

regiones_chile =(
     ("Región de Arica y Parinacota","Región de Arica y Parinacota"),
     ("Región de Tarapacá","Región de Tarapacá"),
     ("Región de Antofagasta","Región de Antofagasta"),
     ("Región de Atacama","Región de Atacama"),
     ("Región de Coquimbo","Región de Coquimbo"),
     ("Región de Valparaíso","Región de Valparaíso"),
     ("Región Metropolitana","Región Metropolitana"),
     ("Región de O'Higgins","Región de O'Higgins"),
     ("Región del Maule","Región del Maule"),
     ("Región del Ñuble","Región del Ñuble"),
     ("Región del Biobío","Región del Biobío"),
     ("Región de La Araucanía","Región de La Araucanía"),
     ("Región de Los Ríos","Región de Los Ríos"),
     ("Región de Los Lagos","Región de Los Lagos"),
     ("Región de Aysén","Región de Aysén"),
     ("Región de Magallanes","Región de Magallanes")
)

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

opciones_categoria = (
    ("AC", "Acelerante"),
    ("AD", "Aditivo"),
    ("CT", "Catalizador"),
    ("CA", "Carga"),
    ("EP", "Epóxico"),
    ("FV", "Fibra de vidrio"),
    ("GC", "Gel Coat"),
    ("PO", "Poliuretano"),
    ("RE", "Resina"),
    ("SV", "solvente"),
)
    
class Producto(models.Model):
     nombre = models.CharField(max_length=100)
     categoria = models.CharField(choices=opciones_categoria, max_length=2)
     descripcion = models.TextField()
     precio = models.FloatField()
     imagen_producto = models.ImageField(upload_to='productos')

     def __str__(self):
          return self.nombre
     
class Cliente(models.Model):
     usuario = models.ForeignKey(User,on_delete=models.CASCADE)
     nombre = models.CharField(max_length=200)
     region = models.CharField(choices=regiones_chile,max_length=100)
     ciudad = models.CharField(max_length=50)
     comuna = models.CharField(max_length=50)
     direccion = models.CharField(max_length=200)
     telefono = models.IntegerField(default=0)
     codigo_postal = models.IntegerField()
     def __str__(self):
          return self.nombre
     
class Cart(models.Model):
     usuario = models.ForeignKey(User,on_delete=models.CASCADE)
     producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)

     @property
     def total_cost(self):
          return self.quantity * self.producto.precio
     
opciones_status = (
    ("Aceptado", "Aceptado"),
    ("Empaquetado", "Empaquetado"),
    ("En Camino", "En Camino"),
    ("Entregado", "Entregado"),
    ("Cancelado", "Cancelado"),
    ("Pendiente", "Pendiente"),
)


class Payment(models.Model):
     usuario = models.ForeignKey(User,on_delete=models.CASCADE)
     cantidad = models.FloatField()
     razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
     razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
     razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
     paid = models.BooleanField(default=False)
     
class OrderPlaced(models.Model):
     usuario = models.ForeignKey(User,on_delete=models.CASCADE)
     cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
     producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)
     fecha_orden = models.DateTimeField(auto_now_add=True)
     status = models.CharField(max_length=50,choices=opciones_status,default='Pendiente')
     payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")

     @property
     def total_cost(self):
          return self.quantity * self.producto.precio