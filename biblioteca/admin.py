from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nacionalidad'] #Lista de campos que se mostraran en el admin
    search_fields = ['nombre'] #Barra de busqueda para campos

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'resumen'] #Lista de campos que se mostraran en el admin
    search_fields = ['titulo'] #Barra de busqueda para campos

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ['libro', 'texto', 'calificacion', 'fecha'] #Lista de campos que se mostraran en el admin
    search_fields = ['libro'] #Barra de busqueda para campos
    list_filter = ['libro'] #Filtra por libro para que queden juntos
    date_hierarchy = 'fecha' #Filtra el listado por fechas mas facilmente
    list_editable = ['calificacion'] #Permite editar campos desde la vista general
    list_per_page = 50 #Limita la cantidad maxima de filas
    readonly_fields = ['fecha'] #Prohibe editar campos  
