from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# Create your models here.
class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.periodo}'
    
class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=150)
    abreviatura = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.carrera}'
    
class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=150)
    resumen = models.CharField(max_length=250, default="Para ver el contenido completo de la noticia, haga click en el boton de abajo.")
    contenido = models.TextField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    sede = models.CharField(default="Trujillo",max_length=50)
    image = models.ImageField(default='estudiantes.jpg')
    image2 = models.ImageField(default='estudiantes.jpg')
    image3 = models.ImageField(default='estudiantes.jpg')
    def __str__(self):
        return f'Noticia: {self.titulo}'
    
class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    titulo = models.CharField(max_length=250)
    lugar = models.CharField(max_length=150)
    descripcion = models.TextField()
    link = models.CharField(max_length=599)
    image = models.ImageField(default='evento.jpg')
    def __str__(self):
        return f'Evento: {self.titulo}'

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    integrantes = models.CharField(max_length=450)
    asesor = models.CharField(max_length=150)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=50)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    url = models.CharField(max_length=599)
    resumen = models.TextField()
    image = models.ImageField(default='estudiantes.jpg')
    image2 = models.ImageField(default='estudiantes.jpg')
    image3 = models.ImageField(default='estudiantes.jpg')
    def __str__(self):
        return f'Proyecto: {self.titulo}'