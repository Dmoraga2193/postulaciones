from django.shortcuts import render, redirect, get_object_or_404
from .models import Postulacion
from .forms import PostulacionForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .filters import FiltroPostulacion
from django.db.models.query_utils import Q

# Create your views here.

def home(request):    
    return render(request, 'app/home.html')

def postulacion(request):
    data = {
        'form' : PostulacionForm()
    }

    if request.method ==  'POST':
        formulario = PostulacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():           
            formulario.save()
            messages.success(request,'Postulacion Enviada Correctamente')
            return redirect(to="home")            
        else:
            data["form"] = formulario  
    return render(request, 'app/postulacion.html',data)

@permission_required('app.view_postulacion')
def listar_postulaciones(request):    
    postulaciones = Postulacion.objects.all()
    filtro = FiltroPostulacion(request.GET, queryset=postulaciones)
    postulaciones = filtro.qs
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(postulaciones,10)
        postulaciones = paginator.page(page)
    except:
        raise Http404
      
    data = {
        'postulaciones': postulaciones,
        'paginator': paginator,  
        'filtro':filtro      
    }    

    return render(request, 'app/listar_postulaciones.html',data)

@permission_required('app.view_postulacion')
def leer_postulacion(request, id):

    postulacion = get_object_or_404(Postulacion,id=id)

    data ={
        'form': PostulacionForm(instance=postulacion)
    }

    if request.method == 'POST':
        formulario = PostulacionForm(data=request.GET, instance=postulacion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_postulaciones")
        data["form"] = formulario

    return render(request, 'app/leer_postulacion.html',data)

@permission_required('app.view_postulacion')
def eliminar_postulacion(request, id):
    postulacion = get_object_or_404(Postulacion, id=id)
    postulacion.delete()
    messages.success(request,'Postulacion Eliminada Correctamente')
    return redirect(to="listar_postulaciones")

@login_required
def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Exitoso")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)