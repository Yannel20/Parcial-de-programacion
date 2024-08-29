from datetime import datetime, timedelta

class Persona:
    def __init__(self, nombre, numero_tarjeta):
        self.nombre = nombre
        self.numero_tarjeta = numero_tarjeta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Estado del libro, True si está disponible, False si está prestado

class Prestamo:
    def __init__(self, persona, libro, fecha_retiro):
        self.persona = persona
        self.libro = libro
        self.fecha_retiro = fecha_retiro
        self.fecha_devolucion = fecha_retiro + timedelta(days=14)  # Fecha límite de devolución (14 días)

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, persona, titulo_libro):
        libro = self.buscar_libro_disponible(titulo_libro)
        if libro:
            libro.disponible = False
            fecha_retiro = datetime.now()
            nuevo_prestamo = Prestamo(persona, libro, fecha_retiro)
            self.prestamos.append(nuevo_prestamo)
            print(f"Libro '{libro.titulo}' prestado a {persona.nombre}. Fecha límite de devolución: {nuevo_prestamo.fecha_devolucion}")
        else:
            print(f"El libro '{titulo_libro}' no está disponible.")

    def buscar_libro_disponible(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo == titulo_libro and libro.disponible:
                return libro
        return None

    def mostrar_prestamos(self):
        if self.prestamos:
            print("Préstamos actuales:")
            for prestamo in self.prestamos:
                print(f"Libro: '{prestamo.libro.titulo}' prestado a {prestamo.persona.nombre} con fecha límite de devolución {prestamo.fecha_devolucion}")
        else:
            print("No hay préstamos en este momento.")

# Momento de usarlo
biblioteca = Biblioteca()

# Crear libros y agregarlos a la biblioteca
libro1 = Libro("La Metamorfosis", "Franz Kafka")
libro2 = Libro("Orgullo y Prejuicio", "Jane Austen")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear persona
persona = Persona("Daniela Pacheco", "123456")

# Prestar un libro
biblioteca.prestar_libro(persona, "La metamorfosis")
biblioteca.prestar_libro(persona, "1915")

# Mostrar préstamos actuales
biblioteca.mostrar_prestamos()
