from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from django.contrib.auth.mixins import LoginRequiredMixin

class LibroListView(ListView):
    model = Libro
    template_name = "libros/lista.html"

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/detalle.html"

# Vistas protegidas con login
class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ["titulo", "autor", "anio_publicacion", "descripcion"]
    template_name = "libros/formulario.html"
    success_url = reverse_lazy("lista_libros")
    login_url = "/accounts/login/"

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ["titulo", "autor", "anio_publicacion", "descripcion"]
    template_name = "libros/formulario.html"
    success_url = reverse_lazy("lista_libros")
    login_url = "/accounts/login/"

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "libros/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_libros")
    login_url = "/accounts/login/"
