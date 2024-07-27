from django.urls import path
#Importamos todos las vistas que crearemos en esta aplicacion
from .import views

#Crear arreglo
urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('listaGeneros/',views.listaGeneros, name='listaGeneros'),
    path('eliminarGenero/<idBdd>',views.eliminarGenero, name="eliminarGenero"),
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('insertarGenero/',views.insertarGenero, name='insertarGenero'),
    path('editarGenero/<idBdd>',views.editarGenero, name='editarGenero'),
    path('actualizarGenero/',views.procesarActualizacionGenero,name='procesarActualizacionGenero'),

    #DIRECTOR
    path('listaDirectores/',views.listaDirectores, name='listaDirectores'),
    path('eliminarDirector/<idBdd>',views.eliminarDirector,name="eliminarDirector"),
    path('nuevoDirector/',views.nuevoDirector, name='nuevoDirector'),
    path('insertarDirector/',views.insertarDirector, name='insertarDirector'),
    path('editarDirector/<idBdd>',views.editarDirector, name='editarDirector'),
    path('actualizarDirector/',views.procesarActualizacionDirector,name='procesarActualizacionDirector'),
   
    #PAIS
    path('listaPaises/',views.listaPaises, name="listaPaises"),
    path('eliminarPais/<idBdd>',views.eliminarPais,name="eliminarPais"),
    path('nuevoPais/',views.nuevoPais, name='nuevoPais'),
    path('insertarPais/',views.insertarPais, name='insertarPais'),
    path('editarPais/<idBdd>',views.editarPais, name='editarPais'),
    path('actualizarPais/',views.procesarActualizacionPais,name='procesarActualizacionPais'),

    #PELICULA
    path('listaPeliculas/',views.listaPeliculas, name="listaPeliculas"),
    path('eliminarPelicula/<idBdd>',views.eliminarPelicula,name="eliminarPelicula"),
    path('nuevaPelicula/',views.nuevaPelicula, name='nuevaPelicula'),
    path('insertarPelicula/',views.insertarPelicula, name='insertarPelicula'),
    path('editarPelicula/<idBdd>',views.editarPelicula, name='editarPelicula'),
    path('actualizarPelicula/',views.procesarActualizacionPelicula,name='procesarActualizacionPelicula'),

    #GESTIONAR CINES
    path('gestionarCines/',views.gestionarCines, name='gestionarCines'),
    path('listadoCines/',views.listadoCines, name='listadoCines'),
    path('insertarCine/',views.insertarCine, name='insertarCine'),

    #*********************************************************METODO FETCH********************************************************#
    
    #DIRECTOR FETCH
    path('gestionarDirectores/',views.gestionarDirectores, name='gestionarDirectores'),
    path('listadoDirectores/',views.listadoDirectores, name='listadoDirectores'),
    path('agregarDirector/',views.agregarDirector, name='agregarDirector'), # INSERTAR DIRECTOR POR METODO FETCH

    #PELICULA FETCH
    path('gestionarPeliculas/',views.gestionarPeliculas, name='gestionarPeliculas'),
    path('listadoPeliculas/',views.listadoPeliculas,name='listadoPeliculas'),
    path('agregarPelicula/',views.agregarPelicula, name='agregarPelicula'),

]