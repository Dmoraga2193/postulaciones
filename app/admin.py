from django.contrib import admin
from .models import *
from .forms import PostulacionForm
# Register your models here.

class PostulacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','celular','cargo','fecha_postulacion')
    list_filter = ('edad','cargo')
    list_per_page = 10
    form = PostulacionForm

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','precio')
    list_per_page = 10

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','region','ciudad')
    list_per_page = 10

admin.site.register(Cargo_Postular)
admin.site.register(Postulacion,PostulacionAdmin)