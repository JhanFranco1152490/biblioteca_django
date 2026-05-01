import random
from biblioteca.models import *

#Borrar todo lo que haya
Author.objects.all().delete()
Libro.objects.all().delete()
Resena.objects.all().delete()

# Crear Autores
autor1 = Author.objects.create(nombre="Edgar Allan Poe", nacionalidad="Estado Unidense")
autor2 = Author.objects.create(nombre="Jane Austen", nacionalidad="Inglesa")
autor3 = Author.objects.create(nombre="Miguel de Cervantes", nacionalidad="Español")
autor4 = Author.objects.create(nombre="Agatha Chistie", nacionalidad="Inglesa")
autor5 = Author.objects.create(nombre="Paulo Coelho", nacionalidad="Brazileña")
autor6 = Author.objects.create(nombre="Charles Dickens", nacionalidad="Inglesa")
autor7 = Author.objects.create(nombre="Gabriel Garcia Marquez", nacionalidad="Colombiana")
autor8 = Author.objects.create(nombre="Victor Hugo", nacionalidad="Francia")
autor9 = Author.objects.create(nombre="James Joyce", nacionalidad="Irlandes")
autor10 = Author.objects.create(nombre="Franz Kafka", nacionalidad="Checo")

# Crear Libros
libros = [
    Libro.objects.create(
        titulo="El cuervo",
        autor=autor1,
        fecha_publicacion="1845-01-29",
        resumen="Poema oscuro sobre la pérdida.",
    ),
    Libro.objects.create(
        titulo="El corazón delator",
        autor=autor1,
        fecha_publicacion="1843-01-01",
        resumen="Relato psicológico de culpa.",
    ),
    Libro.objects.create(
        titulo="La caída de la casa Usher",
        autor=autor1,
        fecha_publicacion="1839-01-01",
        resumen="Historia gótica de decadencia.",
    ),
    Libro.objects.create(
        titulo="Orgullo y prejuicio",
        autor=autor2,
        fecha_publicacion="1813-01-28",
        resumen="Romance y crítica social.",
    ),
    Libro.objects.create(
        titulo="Emma",
        autor=autor2,
        fecha_publicacion="1815-01-01",
        resumen="Historia de enredos amorosos.",
    ),
    Libro.objects.create(
        titulo="Don Quijote I",
        autor=autor3,
        fecha_publicacion="1605-01-01",
        resumen="Caballero y locura.",
    ),
    Libro.objects.create(
        titulo="Don Quijote II",
        autor=autor3,
        fecha_publicacion="1615-01-01",
        resumen="Continuación de aventuras.",
    ),
    Libro.objects.create(
        titulo="Asesinato en el Orient Express",
        autor=autor4,
        fecha_publicacion="1934-01-01",
        resumen="Misterio en tren.",
    ),
    Libro.objects.create(
        titulo="Diez negritos",
        autor=autor4,
        fecha_publicacion="1939-01-01",
        resumen="Suspenso en una isla.",
    ),
    Libro.objects.create(
        titulo="El alquimista",
        autor=autor5,
        fecha_publicacion="1988-01-01",
        resumen="Búsqueda personal.",
    ),
    Libro.objects.create(
        titulo="Brida",
        autor=autor5,
        fecha_publicacion="1990-01-01",
        resumen="Espiritualidad y amor.",
    ),
    Libro.objects.create(
        titulo="Oliver Twist",
        autor=autor6,
        fecha_publicacion="1838-01-01",
        resumen="Infancia difícil.",
    ),
    Libro.objects.create(
        titulo="Grandes esperanzas",
        autor=autor6,
        fecha_publicacion="1861-01-01",
        resumen="Crecimiento personal.",
    ),
    Libro.objects.create(
        titulo="Cien años de soledad",
        autor=autor7,
        fecha_publicacion="1967-01-01",
        resumen="Realismo mágico.",
    ),
    Libro.objects.create(
        titulo="El amor en los tiempos del cólera",
        autor=autor7,
        fecha_publicacion="1985-01-01",
        resumen="Amor eterno.",
    ),
    Libro.objects.create(
        titulo="Crónica de una muerte anunciada",
        autor=autor7,
        fecha_publicacion="1981-01-01",
        resumen="Destino inevitable.",
    ),
    Libro.objects.create(
        titulo="Los miserables",
        autor=autor8,
        fecha_publicacion="1862-01-01",
        resumen="Justicia social.",
    ),
    Libro.objects.create(
        titulo="Ulises",
        autor=autor9,
        fecha_publicacion="1922-01-01",
        resumen="Narrativa experimental.",
    ),
    Libro.objects.create(
        titulo="La metamorfosis",
        autor=autor10,
        fecha_publicacion="1915-01-01",
        resumen="Transformación absurda.",
    ),
    Libro.objects.create(
        titulo="El proceso",
        autor=autor10,
        fecha_publicacion="1925-01-01",
        resumen="Juicio incomprensible.",
    ),
]


# Crear Reseñas
reseñasTextos = [
    "Muy Bueno",
    "Muy Aburrido",
    "Espero la secuela",
    "Nunca habia leido algo peor",
    "Sigue asi",
    "Estuvo regular",
    "<3",
    ":)",
    "No se que poner",
    "Borralo por favor",
    "Ojala tener un autografo",
    "Nuevo Fan",
    "Me encanto",
    "Mi nuevo libro favorito",
    "Por fin lo termine",
    "",
    "Se lo voy a recomendar a mis amigos",
]

for i in range(50):
    libro = random.choice(libros)
    texto = random.choice(reseñasTextos)
    Resena.objects.create(libro=libro, texto=texto, calificacion=random.randint(1, 5))
