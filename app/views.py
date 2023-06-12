from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.views import View
from .models import *
from .forms import PostulacionForm, CustomUserCreationForm, PerfilClienteForm
from .filters import FiltroPostulacion
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.db.models.query_utils import Q
from django.db.models import Count
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import razorpay


# Create your views here.

def home(request):    
    return render(request, 'app/home.html')

def empresa(request): 
    return render(request, 'app/empresa.html')

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

@staff_member_required
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


class VistaCategoria(View):
    def get(self,request,val):
        
        producto = Producto.objects.filter(categoria=val)
        nombre = Producto.objects.filter(categoria=val)
        return render(request,'app/categoria.html',locals())  

    
class ProductoDetalle(View):
    def get(self,request,pk):
        producto = Producto.objects.get(pk=pk)
        return render(request,'app/productodetalle.html',locals())
    
class VistaPerfil(View):
    def get(self,request):
        form = PerfilClienteForm()
        return render(request, 'app/perfil.html', locals())
    def post(self,request):
        form = PerfilClienteForm(request.POST)
        if form.is_valid():
            usuario = request.user
            nombre = form.cleaned_data['nombre']
            region = form.cleaned_data['region']
            ciudad = form.cleaned_data['ciudad']
            comuna = form.cleaned_data['comuna']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            codigo_postal = form.cleaned_data['codigo_postal']

            reg = Cliente(usuario=usuario,nombre=nombre,region=region,ciudad=ciudad,comuna=comuna,direccion=direccion,telefono=telefono,codigo_postal=codigo_postal)
            reg.save()
            messages.success(request, "Perfil guardado correctamente.")
        else:
            messages.success(request, "Ocurrio un problema! Revisa nuevamente los datos ingresados.")
        return render(request, 'app/perfil.html', locals())

def direccion(request):
    add = Cliente.objects.filter(usuario=request.user)
    return render(request, 'app/direccion.html',locals())

class actualizarDireccion(View):
    def get(self,request,pk):
        add = Cliente.objects.get(pk=pk)
        form = PerfilClienteForm(instance=add)
        return render(request, 'app/actualizarDireccion.html',locals())
    def post(self,request,pk):
        form = PerfilClienteForm(request.POST)
        if form.is_valid():
            add = Cliente.objects.get(pk=pk)
            add.nombre = form.cleaned_data['nombre']
            add.region = form.cleaned_data['region']
            add.ciudad = form.cleaned_data['ciudad']
            add.comuna = form.cleaned_data['comuna']
            add.direccion = form.cleaned_data['direccion']
            add.telefono = form.cleaned_data['telefono']
            add.codigo_postal = form.cleaned_data['codigo_postal']
            add.save()
            messages.success(request, "Perfil guardado correctamente.")
        else:
            messages.success(request, "Ocurrio un problema! Revisa nuevamente los datos ingresados.")
        return redirect("direccion")    

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Resquest'
                    email_template_name = 'app/password_message.txt'
                    parameters = {
                        'email': user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name':'ArtePlastica',
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'token':default_token_generator.make_token(user),
                        'protocol':'http',
                    }
                    email=render_to_string(email_template_name,parameters)
                    try:
                        send_mail(subject,email,'', [user.email],fail_silently=False)
                    except:
                        return HttpResponse('Invalid Header')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetForm
    context = {
        'password_form':password_form
    }
    return render(request, 'app/password_reset.html', context)

def add_to_cart(request):
    usuario=request.user
    producto_id=request.GET.get('prod_id')
    producto = Producto.objects.get(id=producto_id)
    Cart(usuario=usuario,producto=producto).save()
    return redirect('/cart')


def show_cart(request):
    usuario = request.user
    cart = Cart.objects.filter(usuario=usuario)
    amount = 0
    for p in cart:
        value = p.quantity * p.producto.precio
        amount = amount + value
    totalamount = amount
    return render(request, 'app/addtocart.html',locals())

class checkout(View):
    def get(self,request):
        usuario = request.user
        add=Cliente.objects.filter(usuario=usuario)
        cart_items=Cart.objects.filter(usuario=usuario)
        amount = 0
        for p in cart_items:
            value = p.quantity * p.producto.precio
            amount = amount + value
        totalamount = amount * 100
        razoramount = int(totalamount)
        cliente = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = {"amount":razoramount, "currency": "INR","receipt":"order_rcptid_11"}
        payment_response = cliente.order.create(data=data)
        print(payment_response)
        #{'id': 'order_M0occXNT76FBxJ', 'entity': 'order', 'amount': 3198000, 'amount_paid': 0, 'amount_due': 3198000, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1686528578}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                usuario = usuario,
                cantidad = totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()
        return render(request, 'app/checkout.html', locals())

def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    usuario=request.user
    cliente=Cliente.objects.get(id=cust_id)
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid=True
    payment.razorpay_payment_id = payment_id
    payment.save()
    #para guardar los detalles de la orden
    cart=Cart.objects.filter(usuario=usuario)
    for c in cart:
        OrderPlaced(usuario=usuario,cliente=cliente,producto=c.producto,quantity=c.quantity,payment=payment).save()
        c.delete()
    
    return redirect("orders")

def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(producto=prod_id) & Q(usuario=request.user))
        c.quantity+=1
        c.save()
        usuario = request.user
        cart = Cart.objects.filter(usuario=usuario)
        amount = 0
        for p in cart:
            value = p.quantity * p.producto.precio
            amount = amount + value
        totalamount = amount      
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(producto=prod_id) & Q(usuario=request.user))
        c.quantity-=1
        c.save()
        usuario = request.user
        cart = Cart.objects.filter(usuario=usuario)
        amount = 0
        for p in cart:
            value = p.quantity * p.producto.precio
            amount = amount + value
        totalamount = amount        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(producto=prod_id) & Q(usuario=request.user))
        c.delete()
        usuario = request.user
        cart = Cart.objects.filter(usuario=usuario)
        amount = 0
        for p in cart:
            value = p.quantity * p.producto.precio
            amount = amount + value
        totalamount = amount        
        data={            
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)