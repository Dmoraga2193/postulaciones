from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import CambiarContraseñaForm

urlpatterns = [    
    path('', views.home, name='home'),
    path('postulacion/', views.postulacion, name='postulacion'),
    path('listar-postulaciones/', views.listar_postulaciones,name='listar_postulaciones'),
    path('leer-postulacion/<id>/', views.leer_postulacion, name='leer_postulacion'),
    path('eliminar-postulacion/<id>/', views.eliminar_postulacion, name='eliminar_postulacion'),
    path('registro/', views.registro, name='registro'),
    path('perfil/',views.VistaPerfil.as_view(),name='perfil'),
    # aprendiendo con arte plastica
    path('cargas/',views.cargas,name='cargas'),
    path('resina-epoxica/',views.resina_epoxica,name='resina_epoxica'),
    path('fibra-de-vidrio/',views.fibra_vidrio,name='fibra_vidrio'),
    path('gel-coat/',views.gel_coat,name='gel_coat'),
    path('poliuretano/',views.poliuretano,name='poliuretano'),

    path('direccion/',views.direccion,name='direccion'),
    path('actualizarDireccion/<int:pk>',views.actualizarDireccion.as_view(),name='actualizarDireccion'),
    

    # cambiar contraseña
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=CambiarContraseñaForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    # olvide mi contraseña   
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html'),name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),

    path('empresa/',views.empresa,name='empresa'),
    path("categoria/<slug:val>",views.VistaCategoria.as_view(),name='categoria'),
    path("producto-detalle/<int:pk>",views.ProductoDetalle.as_view(),name='producto-detalle')
]