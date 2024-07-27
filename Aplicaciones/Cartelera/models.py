from django.db import models

#Crear Clase Genero
class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

    foto = models.FileField(upload_to='generos', null=True,blank=True)
    
    # Modificar la vista 
    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.descripcion)
    
#Crear clase Director
class Director(models.Model):
    id = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    foto = models.FileField(upload_to='directores', null=True,blank=True)

    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.apellido)

#Crear clase Pais
class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    continente=models.CharField(max_length=30,default='')
    capital=models.CharField(max_length=30,default='')
    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.capital)

#Crear clase Pelicula
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    duracion = models.TimeField(null=True)
    sinopsis = models.TextField()
    #Claves foraneas
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    portada = models.FileField(upload_to='portadas', null=True,blank=True)

    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id,self.titulo,self.duracion)

#Crear Clase Cine
class Cine(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    # Modificar la vista 
    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.direccion)