from django.contrib import admin
from .models import Cargo_Postular,Postulacion
from .forms import PostulacionForm
# Register your models here.

class PostulacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','celular','cargo','fecha_postulacion')
    list_filter = ('edad','cargo')
    list_per_page = 10
    form = PostulacionForm

admin.site.register(Cargo_Postular)
admin.site.register(Postulacion,PostulacionAdmin)