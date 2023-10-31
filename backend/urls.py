from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from .views import CustomLoginView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('noticia/<int:id>/', views.noticia, name='noticia'),
    path('noticias/', views.noticias, name='noticias'),
    path('eventos/', views.eventos, name='eventos'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyecto/<int:id>/', views.proyecto, name='proyecto'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/noticias/agregar/', views.agregarnoticia, name='agregarnoticia'),
    path('dashboard/eventos/agregar/', views.agregarevento, name='agregarevento'),
    path('dashboard/proyectos/agregar/', views.agregarproyecto, name='agregarproyecto'),
    path('dashboard/noticias/', views.noticiasdashboard, name='noticiasdashboard'),
    path('dashboard/noticias/eliminar/<int:id>', views.eliminarnoticia, name='eliminarnoticia'),
    path('dashboard/noticias/editar/<int:id>', views.editarnoticia, name='editarnoticia'),
    path('dashboard/eventos' , views.eventosdashboard, name='eventosdashboard'),
    path('dashboard/eventos/eliminar/<int:id>', views.eliminarevento, name='eliminarevento'),
    path('dashboard/eventos/editar/<int:id>', views.editarevento, name='editarevento'),
    path('dashboard/proyectos', views.proyectosdashboard, name='proyectosdashboard'),
    path('dashboard/proyectos/eliminar/<int:id>', views.eliminarproyecto, name='eliminarproyecto'),
    path('dashboard/proyectos/editar/<int:id>', views.editarproyecto, name='editarproyecto'),
    path('dashboard/carreras', views.carreras, name='carreras'),
    path('dashboard/carreras/eliminar/<int:id>/', views.eliminarcarrera, name='eliminarcarrera'),
    path('dashboard/periodos', views.periodos, name='periodos'),
    path('dashboard/periodos/eliminar/<int:id>/', views.eliminarperiodo, name='eliminarperiodo'),
    path('salir/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)