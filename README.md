# 📚 Proyecto Gestión de Libros – Django

## 📌 Descripción
Este proyecto consiste en una aplicación web desarrollada en **Django 5.2.6** que permite gestionar libros mediante un sistema **CRUD (Crear, Leer, Actualizar y Eliminar)**.  

El proyecto se desarrolló aplicando metodologías ágiles (**Scrum + XP**), con control de versiones en **GitHub**, y **Integración Continua (CI)** usando GitHub Actions.  

---

## 👥 Integrantes y Roles
- **Mark Alexis Rodriguez Perez – Scrum Master**  
  Facilita las ceremonias Scrum (Planning, Daily, Review, Retrospective), organiza las tareas en Trello, asegura la correcta aplicación de prácticas ágiles y coordina la integración en GitHub y CI.  

- **Developer 1 – [Nicolas Quiroz]**  
  Implementó el registro y listado de libros (HU03, HU04) y diseñó las plantillas base con Bootstrap.  

- **Developer 2 – [Cesar Lopez]**  
  Implementó la edición y eliminación de libros (HU05, HU06), configuró validaciones y protegió vistas con LoginRequiredMixin.  

- **Developer 3 – [Alexander Pielago]**  
  Configuró pruebas unitarias (HU07), documentó Pair Programming y configuró la Integración Continua en GitHub Actions (HU10).  

- **Product Owner (Luis Gonzales)** – Cliente ficticio representando los requerimientos del usuario final.  

---

## 🚀 Funcionalidades principales
- Registrar libros con **título, autor, género y fecha de publicación**.  
- Listar libros en un catálogo visual con portadas.  
- Editar información de libros registrados.  
- Eliminar libros del sistema.  
- Login y Logout de usuarios para proteger creación, edición y eliminación.  
- Interfaz intuitiva con **Bootstrap** (cards, navbar, botones).  

---

## 📂 Historias de Usuario principales
- **HU01** – Configuración inicial del entorno Django.  
- **HU02** – Creación del proyecto base "Gestión de Libros".  
- **HU03** – Registro de un libro.  
- **HU04** – Listado de libros.  
- **HU05** – Edición de libros.  
- **HU06** – Eliminación de libros.  
- **HU07** – Pruebas unitarias (TDD básico).  
- **HU08** – Refactorización del código.  
- **HU09** – Evidencia de Pair Programming y GitHub.  
- **HU10** – Configuración de Integración Continua (CI).  

---

## ⚙️ Instalación y ejecución
1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/usuario/proyecto-gestion-libros.git
   cd proyecto-gestion-libros
