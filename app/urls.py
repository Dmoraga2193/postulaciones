from django.urls import path
from .views import home, postulacion, listar_postulaciones,leer_postulacion, eliminar_postulacion, registro

urlpatterns = [
    path('', home, name="home"),
    path('postulacion/', postulacion, name="postulacion"),
    path('listar-postulaciones/', listar_postulaciones,name="listar_postulaciones"),
    path('leer-postulacion/<id>/', leer_postulacion, name="leer_postulacion"),
    path('eliminar-postulacion/<id>/', eliminar_postulacion, name="eliminar_postulacion"),
    path('registro/', registro, name="registro"),
]
