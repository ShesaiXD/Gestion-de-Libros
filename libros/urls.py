from django.urls import path
from .views import (
    LibroListView, LibroDetailView,
    LibroCreateView, LibroUpdateView, LibroDeleteView
)

urlpatterns = [
    path("", LibroListView.as_view(), name="lista_libros"),
    path("<int:pk>/", LibroDetailView.as_view(), name="detalle_libro"),
    path("nuevo/", LibroCreateView.as_view(), name="crear_libro"),
    path("editar/<int:pk>/", LibroUpdateView.as_view(), name="editar_libro"),
    path("eliminar/<int:pk>/", LibroDeleteView.as_view(), name="eliminar_libro"),
]
