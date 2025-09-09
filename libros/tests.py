from django.test import TestCase
from .models import Libro

class LibroModelTest(TestCase):
    def setUp(self):
        # Crear un libro de prueba
        Libro.objects.create(titulo="Test Libro", autor="Nico", anio_publicacion=2025)

    def test_libro_creado(self):
        # Verificar que el libro existe y los datos son correctos
        libro = Libro.objects.get(titulo="Test Libro")
        self.assertEqual(libro.autor, "Nico")
        self.assertEqual(libro.anio_publicacion, 2025)

from django.urls import reverse
from django.contrib.auth.models import User

class LibroViewsTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='nicolas', password='12345')
        # Crear un libro de prueba
        self.libro = Libro.objects.create(titulo="Test Libro", autor="Nico", anio_publicacion=2025)

    def test_lista_libros(self):
        # Ver que la lista de libros funciona
        response = self.client.get(reverse('lista_libros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Libro")

    def test_create_libro_requires_login(self):
        # Intentar acceder a la vista de crear sin login → debe redirigir
        response = self.client.get(reverse('crear_libro'))
        self.assertEqual(response.status_code, 302)  # Redirige al login

    def test_create_libro_logged_in(self):
        # Acceder a la vista de crear con login → debe funcionar
        self.client.login(username='nicolas', password='12345')
        response = self.client.get(reverse('crear_libro'))
        self.assertEqual(response.status_code, 200)
