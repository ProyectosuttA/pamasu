from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse # funciona para solo mandar texto corto y de prueba en una función
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Usercreationform Permite generar un formulario de registro generico y authenticationform nos crea un formulario de autentication
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User #Para poder importarl el modelo de usuario
from django.contrib.auth.decorators import login_required #librería para requerir una session del sistema 
from .forms import *
from .models import *

# Create your views here.
"""def registro(request):
    if request.method=='GET':
        print("Enviando los datos")
        return render(request, 'registro.html', {
            'formulario' : UserCreationForm
        })#Al mandar un valor en variable cramos un direccionario y lavariable va en comillas 
    else:
        print("Tomando los datos")
        print(request.POST)
        if request.POST['password1']== request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])# Linea para crear un objeto usurio
                user.save()
                login(request, user)
                return redirect('plataforma')
            except:
                return render(request, 'registro.html',{
                    'formulario' : UserCreationForm,
                    'respuesta':"El usuario ya existe"
                })

        else:
            return render(request, 'registro.html',{
                'formulario' : UserCreationForm,
                'respuesta':"Las contraseñas no coinciden"
                })"""

def inicio(request):
    logout(request)
    return render(request, 'inicio.html')

@login_required(login_url='/') #para necesitar una sesion en la función
def plataforma(request):
    return render(request, 'plataforma.html')

@login_required(login_url='/')
def registrar(request):
    if request.method=='GET':
        return render(request, 'registrar.html',{
        'formulario':RegistroForm
        })
    else:
        print(request.POST)
        registro=Registro(id_carta=request.POST['id_carta'],pedido=request.POST['pedido'], folio=request.POST['folio'], origen=request.POST['origen'], destino=request.POST['destino'], maniobras=request.POST['maniobras'], diesel=request.POST['diesel'], gastos=request.POST['gastos'], hora_reporte=request.POST['fecha1']+' '+request.POST['hora1'], inicio_carga=request.POST['fecha2']+' '+request.POST['hora2'], termino_carga=request.POST['fecha3']+' '+request.POST['hora3'], inicio_ruta=request.POST['fecha4']+' '+request.POST['hora4'], arribo_cliente=request.POST['fecha5']+' '+request.POST['hora5'], inicio_descarga=request.POST['fecha6']+' '+request.POST['hora6'], termino_descarga=request.POST['fecha7']+' '+request.POST['hora7'], termino_viaje=request.POST['fecha8']+' '+request.POST['hora8'])
        print(registro.__dict__)
        try:
            registro.save()
            return render(request, 'registrar.html',{
            'respuesta':'Almacenado correctamente'
            })
        except:
            return render(request, 'registrar.html',{
            'respuesta':'Revisa los datos proporcionados'
            })

"""@login_required(login_url='/')
def administrador(request):
    return render(request, 'admin_home.html')
"""

def salir(request):
    logout(request)
    return redirect ('inicio')

def ingresar(request):
    logout(request)
    if request.method== 'GET':
        return render(request, 'ingresar.html', {
            'form':AuthenticationForm
        })
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ingresar.html',{
                'form':AuthenticationForm,
                'valor':"El usuario o la contraseña no exite"
            })
        else:
            login(request, user)
            return redirect('plataforma')

@login_required(login_url='/')
def consultar(request):
    if request.method== 'GET':
        return render(request, 'busqueda.html')
    else:
        try:
            consulta=Registro.objects.get(pk=request.POST['busqueda'])
            print(consulta.__dict__)
            return render(request, 'consulta.html', {
                'consultas':consulta
            })
        except:
            return render(request, 'busqueda.html', {
                'respuesta':'No se encontro el registro'
            })

@login_required(login_url='/')       
def seguimiento(request):
    if request.method== 'GET':
        return render(request, 'busqueda.html')
    else:
        try:
            consulta=Registro.objects.get(pk=request.POST['busqueda'])
            print(consulta.__dict__)
            return render(request, 'consulta.html', {
                'consultas':consulta
            })
        except:
            return render(request, 'busqueda.html', {
                'respuesta':'No se encontro el registro'
            })

@login_required(login_url='/')
def comentarios(request):
    if request.method== 'GET':
        return render(request, 'busqueda.html')
    else:
        try:
            comentarios2=Registro.objects.get(id_carta=request.POST['busqueda'])
            request.session['comentarios']=request.POST['busqueda']
            return redirect('comentario')
        except:
            return render(request, 'busqueda.html', {
                'respuesta':'No se encontro el registro'
            }) 

@login_required(login_url='/')
def comentario(request):
    if request.method=='GET':
        valor=request.session['comentarios']
        comentarios=Comentarios.objects.filter(carta=valor)
        return render(request, 'comentarios.html',{
        'comentarios':comentarios
        })
    else:
        valor=request.session['comentarios']
        comentarios=Comentarios.objects.filter(carta=valor) #consultamos los comentarios para mostrarlos
        comenta=Comentarios(carta=Registro.objects.get(pk=valor),comentario=request.POST['comentario'], user=request.user)#creamos el objeto de los comentarios
        comenta.save()
        return render(request, 'comentarios.html',{
        'comentarios':comentarios
        })





    