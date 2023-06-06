import django_filters
from .models import *

class FiltroPostulacion(django_filters.FilterSet):
    class Meta:
        model = Postulacion
        fields = ['comuna','cargo','experiencia','disponibilidad']