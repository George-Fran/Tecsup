from django.shortcuts import render, redirect
from .models import Noticia, Evento, Proyecto, Carrera, Periodo
from .forms import UserRegisterForm, NoticiaForm, EventoForm, ProyectoForm, CarreraForm, PeriodoForm, CustomAuthenticationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


def home(request):
	noticias = Noticia.objects.raw('SELECT * FROM backend_noticia ORDER  BY id_noticia DESC LIMIT  4;')
	eventos = Evento.objects.raw('SELECT * FROM backend_evento ORDER  BY id_evento DESC LIMIT 4;')
	proyectos = Proyecto.objects.raw('SELECT * FROM backend_proyecto ORDER  BY id_proyecto DESC LIMIT 3;')
	context = {'noticias':noticias, 'eventos':eventos, 'proyectos':proyectos}
	return render(request, 'backend/index.html', context)

def noticias(request):
	noticias = Noticia.objects.raw('SELECT * FROM backend_noticia ORDER  BY id_noticia DESC')
	context = {'noticias':noticias}
	return render(request, 'backend/noticias.html', context)

def noticia(request, id):
	noticia = Noticia.objects.get(id_noticia=id)
	context = {'noticia':noticia}
	return render(request, 'backend/noticia.html', context)

def eventos(request):
	eventos = Evento.objects.raw('SELECT * FROM backend_evento ORDER  BY id_evento DESC')
	context = {'eventos':eventos}
	return render(request, 'backend/eventos.html', context)

def proyectos(request):
	proyectos = Proyecto.objects.raw('SELECT * FROM backend_proyecto ORDER  BY id_proyecto DESC')
	context = {'proyectos':proyectos}
	return render(request, 'backend/proyectos.html', context)

def proyecto(request, id):
	proyecto = Proyecto.objects.get(id_proyecto=id)
	context = {'proyecto':proyecto}
	return render(request, 'backend/proyecto.html', context)

@login_required
def dashboard(request):
    cantidad_noticias = Noticia.objects.count()
    cantidad_eventos = Evento.objects.count()
    cantidad_proyectos = Proyecto.objects.count()

    noticias = Noticia.objects.order_by('-id_noticia')[:2]
    eventos = Evento.objects.order_by('-id_evento')[:2]
	proyectos = Proyecto.objects.order_by('-id_proyecto')[:2]

    context = {
        'noticias': noticias,
        'eventos': eventos,
		'proyectos': proyectos,
        'cantidad_noticias': cantidad_noticias,
        'cantidad_eventos': cantidad_eventos,
        'cantidad_proyectos': cantidad_proyectos
    }
    return render(request, 'backend/dashboard.html', context)

@login_required
def agregarnoticia(request):
	if request.method == 'POST':
		form = NoticiaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('noticiasdashboard')
	else: form = NoticiaForm()

	if request.method == 'POST':
		form2 = CarreraForm(request.POST, request.FILES)
		if form2.is_valid():
			form2.save()
			return redirect('agregarnoticia')
	else: form2 = CarreraForm()
	context = {'form' : form, 'form2' : form2}
	return render(request, 'backend/agregarnoticia.html', context)

@login_required
def agregarevento(request):
	if request.method == 'POST':
		form = EventoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	else: form = EventoForm()
	context = {'form' : form}
	return render(request, 'backend/agregarevento.html', context)

@login_required
def agregarproyecto(request):
	if request.method == 'POST':
		form = ProyectoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('proyectosdashboard')
	else: form = ProyectoForm()
	if request.method == 'POST':
		form2 = CarreraForm(request.POST, request.FILES)
		if form2.is_valid():
			form2.save()
			return redirect('agregarproyecto')
	else: form2 = CarreraForm()

	if request.method == 'POST':
		form3 = PeriodoForm(request.POST, request.FILES)
		if form3.is_valid():
			form3.save()
			return redirect('agregarproyecto')
	else: form3 = PeriodoForm()
	context = {'form' : form, 'form2' : form2, 'form3' : form3}
	return render(request, 'backend/agregarproyecto.html', context)

@login_required
def noticiasdashboard(request):
	busqueda = request.GET.get('buscar')
	noticias = Noticia.objects.raw('SELECT * FROM backend_noticia ORDER  BY id_noticia DESC')
	
	if busqueda:
		noticias = Noticia.objects.filter(
			Q(titulo__icontains = busqueda) |
			Q(carrera__carrera__icontains = busqueda)
		).distinct()

	context = {'noticias':noticias}
	return render(request, 'backend/noticiasdashboard.html', context)

def eliminarnoticia(request, id):
	noticia = Noticia.objects.get(id_noticia=id)
	noticia.delete()
	return redirect('noticiasdashboard')

@login_required
def editarnoticia(request, id):
	noticia = Noticia.objects.get(id_noticia=id)
	if request.method == 'POST':
		form = NoticiaForm(request.POST, request.FILES, instance=noticia)
		if form.is_valid():
			form.save()
			return redirect('noticiasdashboard')
	else: form = NoticiaForm(instance=noticia)
	context = {'form' : form}
	return render(request, 'backend/editarnoticia.html', context)

@login_required
def eventosdashboard(request):
	busqueda = request.GET.get('buscar')
	eventos = Evento.objects.raw('SELECT * FROM backend_evento ORDER  BY id_evento DESC')

	if busqueda:
		eventos = Evento.objects.filter(
			Q(titulo__icontains = busqueda) |
			Q(lugar__icontains = busqueda)
		).distinct()

	context = {'eventos':eventos}
	return render(request, 'backend/eventosdashboard.html', context)

def eliminarevento(request, id):
	evento = Evento.objects.get(id_evento=id)
	evento.delete()
	return redirect('eventosdashboard')

@login_required
def editarevento(request, id):
	evento = Evento.objects.get(id_evento=id)
	if request.method == 'POST':
		form = EventoForm(request.POST, request.FILES, instance=evento)
		if form.is_valid():
			form.save()
			return redirect('eventosdashboard')
	else: form = EventoForm(instance=evento)
	context = {'form' : form}
	return render(request, 'backend/editarevento.html', context)

@login_required
def proyectosdashboard(request):
	busqueda = request.GET.get('buscar')
	proyectos = Proyecto.objects.raw('SELECT * FROM backend_proyecto ORDER  BY id_proyecto DESC')

	if busqueda:
		proyectos = Proyecto.objects.filter(
			Q(titulo__icontains = busqueda) |
			Q(carrera__carrera__icontains = busqueda) |
			Q(periodo__periodo__icontains = busqueda) |
			Q(ciclo__icontains = busqueda) | 
			Q(asesor__icontains = busqueda)
		).distinct()
	
	context = {'proyectos':proyectos}
	return render(request, 'backend/proyectosdashboard.html', context)

def eliminarproyecto(request, id):
	proyecto = Proyecto.objects.get(id_proyecto=id)
	proyecto.delete()
	return redirect('proyectosdashboard')

@login_required
def editarproyecto(request, id):
	proyecto = Proyecto.objects.get(id_proyecto=id)
	if request.method == 'POST':
		form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
		if form.is_valid():
			form.save()
			return redirect('proyectosdashboard')
	else: form = ProyectoForm(instance=proyecto)
	context = {'form' : form}
	return render(request, 'backend/editarproyecto.html', context)

@login_required
def carreras(request):
	busqueda = request.GET.get('buscar')
	carreras = Carrera.objects.raw('SELECT * FROM backend_carrera ORDER  BY id_carrera DESC')

	if busqueda:
		carreras = Carrera.objects.filter(
			Q(carrera__icontains = busqueda) | 
			Q(abreviatura__icontains = busqueda)
		).distinct()

	if request.method == 'POST':
		form = CarreraForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('carreras')
	else: form = CarreraForm()
	context = {'carreras':carreras, 'form' : form}
	return render(request, 'backend/carreras.html', context)

@login_required
def eliminarcarrera(request, id):
	carrera = Carrera.objects.get(id_carrera=id)
	carrera.delete()
	return redirect('carreras')

def periodos(request):
	busqueda = request.GET.get('buscar')
	periodos = Periodo.objects.raw('SELECT * FROM backend_periodo ORDER  BY id_periodo DESC')

	if busqueda:
		periodos = Periodo.objects.filter(
			Q(periodo__icontains = busqueda)
		).distinct()

	if request.method == 'POST':
		form = PeriodoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('periodos')
	else: form = PeriodoForm()
	context = {'periodos':periodos, 'form' : form}
	return render(request, 'backend/periodos.html', context)

def eliminarperiodo(request, id):
	periodo = Periodo.objects.get(id_periodo=id)
	periodo.delete()
	return redirect('periodos')

class CustomLoginView(LoginView):
    form = CustomAuthenticationForm
    template_name = 'backend/login.html'
    #

# Create your views here.
