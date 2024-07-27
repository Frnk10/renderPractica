from django.contrib import messages

from django.http import JsonResponse
from django.shortcuts import redirect, render
# tokens CSRF
from django.views.decorators.csrf import csrf_exempt
#Importar los modelos
from .models import Cine, Genero,Director,Pais,Pelicula

# Create your views here.
def inicio(request):
    return render(request,"inicio.html")

#Renderizacion del template listaGeneros
def listaGeneros(request):
    generosBdd = Genero.objects.all()
    return render(request,"listaGeneros.html",{'generos':generosBdd})
#ELIMINAR GENERO POR ID
def eliminarGenero(request,idBdd):
    generoEliminar = Genero.objects.get(id=idBdd)
    messages.success(request,"Género eliminado correctamente")
    generoEliminar.delete()
    return redirect('listaGeneros')

#RENDERIZAR FORMULARIO AGREGAR GENERO
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')
#AGREGAR GENERO
def insertarGenero(request):
    nombre = request.POST["nombre"]
    detalle = request.POST["descripcion"]
    nuevoGenero = Genero.objects.create(nombre=nombre,descripcion=detalle)
    messages.success(request,"Género registrado exitosamente")
    return redirect('listaGeneros')
#RENDERIZAR FORMULARIO PARA ACTUALIZACION GENERO
def editarGenero(request,idBdd):
    generoEditar = Genero.objects.get(id=idBdd)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})
#ACTULIZAR GENERO
def procesarActualizacionGenero(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    detalle = request.POST["descripcion"]

    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = detalle    
    generoConsultado.save()
    messages.success(request,'Género actualizado correctamente.')
    return redirect('listaGeneros')



#Renderizacion del template listaDirectores
def listaDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request,"listaDirectores.html",{'directores':directoresBdd})
#ELIMINAR DIRECTOR POR ID
def eliminarDirector(request,idBdd):
    directorEliminar = Director.objects.get(id=idBdd)
    messages.success(request,"Director eliminado correctamente")
    directorEliminar.delete()
    return redirect('listaDirectores')

#RENDERIZAR FORMULARIO AGREGAR DIRECTOR
def nuevoDirector(request):
    return render(request,'nuevoDirector.html')
#AGREGAR DIRECTOR
def insertarDirector(request):
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    estado = request.POST.get("estado") == 'on'
    foto = request.FILES.get("foto")

    nuevoDirector = Director.objects.create(apellido=apellido,nombre=nombre,estado=estado,foto=foto)
    messages.success(request,"Director registrado exitosamente")
    return redirect('listaDirectores')
#RENDERIZAR FORMULARIO PARA ACTUALIZACION DIRECTOR
def editarDirector(request,idBdd):
    directorEditar = Director.objects.get(id=idBdd)
    return render(request,'editarDirector.html',{'directorEditar':directorEditar})
#ACTULIZAR DIRECTOR
def procesarActualizacionDirector(request):
    id = request.POST["id"]
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    estado = request.POST.get("estado") == 'on'
    foto = request.FILES.get("foto")
    directorConsultado = Director.objects.get(id=id)
    directorConsultado.apellido = apellido
    directorConsultado.nombre = nombre
    directorConsultado.estado = estado
    directorConsultado.foto = foto
    directorConsultado.save()
    messages.success(request,'Director actualizado correctamente.')
    return redirect('listaDirectores')



#Renderizacion del template listaPaises
def listaPaises(request):
    paisesBdd = Pais.objects.all()
    return render(request,"listaPaises.html",{'paises':paisesBdd})
#ELIMINAR PAIS POR ID
def eliminarPais(request,idBdd):
    paisEliminar = Pais.objects.get(id=idBdd)
    messages.success(request,"País eliminado correctamente")
    paisEliminar.delete()
    return redirect('listaPaises')

#RENDERIZAR FORMULARIO AGREGAR PAIS
def nuevoPais(request):
    return render(request,'nuevoPais.html')
#AGREGAR PAIS
def insertarPais(request):
    nombre = request.POST["nombre"]
    continente = request.POST["continente"]
    capital = request.POST["capital"]
    nuevoPais = Pais.objects.create(nombre=nombre,continente=continente,capital=capital)
    messages.success(request,"País registrado exitosamente")
    return redirect('listaPaises')
#RENDERIZAR FORMULARIO PARA ACTUALIZACION PAIS
def editarPais(request,idBdd):
    paisEditar = Pais.objects.get(id=idBdd)
    return render(request,'editarPais.html',{'paisEditar':paisEditar})
#ACTULIZAR PAIS
def procesarActualizacionPais(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    continente = request.POST["continente"]
    capital = request.POST["capital"]

    paisConsultado = Pais.objects.get(id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request,'País actualizado correctamente.')
    return redirect('listaPaises')



#Renderización del template listaPeliculas
def listaPeliculas(request):
    peliculasBdd =  Pelicula.objects.all()
    return render(request,'listaPeliculas.html',{'peliculas':peliculasBdd})
#ELIMINAR PELICULA POR ID
def eliminarPelicula(request,idBdd):
    peliculaEliminar = Pelicula.objects.get(id=idBdd)
    messages.success(request,"Película eliminada correctamente")
    peliculaEliminar.delete()
    return redirect('listaPeliculas')

#RENDERIZAR FORMULARIO AGREGAR PELICULA
def nuevaPelicula(request):
    generosBdd = Genero.objects.all()
    directoreBdd = Director.objects.all()
    return render(request,'nuevaPelicula.html',{'generos':generosBdd,'directores':directoreBdd})
#AGREGAR PELICULA
def insertarPelicula(request):
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinopsis = request.POST["sinopsis"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]

    portada = request.FILES.get("portada")

    # Obtener instancias de Genero y Director
    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)

    nuevaPelicula = Pelicula.objects.create(titulo=titulo,duracion=duracion,sinopsis=sinopsis,
                                            genero=genero,director=director,portada=portada)
    messages.success(request,"Película registrada exitosamente")
    return redirect('listaPeliculas')
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, 'insertarPelicula', {
        'generos': generos,
        'directores': directores
    })
#RENDERIZAR FORMULARIO PARA ACTUALIZACION PELICULA
def editarPelicula(request,idBdd):
    peliculaEditar = Pelicula.objects.get(id=idBdd)
    generosBdd = Genero.objects.all()
    directoreBdd = Director.objects.all()
    return render(request,'editarPelicula.html',{'peliculaEditar':peliculaEditar,'generos':generosBdd,'directores':directoreBdd})
#ACTULIZAR PELICULA
def procesarActualizacionPelicula(request):
    id = request.POST["id"]
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinopsis = request.POST["sinopsis"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]
    # Obtener instancias de Genero y Director
    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)
    
    paisConsultado = Pelicula.objects.get(id=id)
    paisConsultado.titulo = titulo
    paisConsultado.duracion = duracion
    paisConsultado.sinopsis = sinopsis
    paisConsultado.genero = genero
    paisConsultado.director = director
    paisConsultado.save()
    messages.success(request,'Película actualizada correctamente.')
    return redirect('listaPeliculas')


#******************************************CINE**************************************************#

#RENDERIZAR FORMULARIO GESTION CINES
def gestionarCines(request):
    return render(request,'gestionarCines.html')
def listadoCines(request):
    cinesBdd =  Cine.objects.all()
    return render(request,'listadoCines.html',{'cines':cinesBdd})
#AGREGAR CINE MÉTODO AJAX
@csrf_exempt
def insertarCine(request):
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    telefono = request.POST["telefono"]
    nuevoCine = Cine.objects.create(nombre=nombre,direccion=direccion,telefono=telefono)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Cine registrado exitosamente',
    })



#*********************************************METODO FETCH******************************************#

#*********************************DIRECTOR*******************************************#

def gestionarDirectores(request):
    return render(request,'director/gestionarDirectores.html')
# AGREGAR DIRECTOR CON FETCH
@csrf_exempt
def agregarDirector(request):
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    estado = request.POST.get("estado") == 'on'
    foto = request.FILES.get("foto")

    nuevoDirector = Director.objects.create(apellido=apellido,nombre=nombre,estado=estado,foto=foto)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Director registrado exitosamente',
    })

def listadoDirectores(request):
    directoresBdd =  Director.objects.all()
    return render(request,'director/listadoDirectores.html',{'directores':directoresBdd})



#*********************************PELICULA*******************************************#

def gestionarPeliculas(request):
    generosBdd = Genero.objects.all()
    directoreBdd = Director.objects.all()
    return render(request,'pelicula/gestionarPeliculas.html',{'generos':generosBdd,'directores':directoreBdd})
# AGREGAR PELICULA CON FETCH
def agregarPelicula(request):
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinopsis = request.POST["sinopsis"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]

    portada = request.FILES.get("portada")

    # Obtener instancias de Genero y Director
    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)

    nuevaPelicula = Pelicula.objects.create(titulo=titulo,duracion=duracion,sinopsis=sinopsis,
                                            genero=genero,director=director,portada=portada)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return JsonResponse({
        'estado': True,
        'mensaje': 'Pelicula registrada exitosamente',
    })
# Listar Peliculas
def listadoPeliculas(request):
    peliculasBdd =  Pelicula.objects.all()
    return render(request,'pelicula/listadoPeliculas.html',{'peliculas':peliculasBdd})



#*********************************************METODO AXIOS******************************************#

#*********************************DIRECTOR*******************************************#

def gestionarDirectoresAxios(request):
    return render(request,'director/gestionarDirectoresAxios.html')
# AGREGAR DIRECTOR CON FETCH
def agregarDirectorAxios(request):
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    estado = request.POST.get("estado") == 'on'
    foto = request.FILES.get("foto")

    nuevoDirector = Director.objects.create(apellido=apellido,nombre=nombre,estado=estado,foto=foto)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Director registrado exitosamente',
    })
