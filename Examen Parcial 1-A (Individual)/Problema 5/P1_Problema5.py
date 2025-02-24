# Definimos una clase para representar a un estudiante
class Estudiante:
    def __init__(self, nombre, matricula, calificacion):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion = calificacion

# Creamos una lista de estudiantes
estudiantes = [
    Estudiante(nombre="Juan Carlos", matricula="A001", calificacion=85.5),
    Estudiante(nombre="María López", matricula="A002", calificacion=92.3),
    Estudiante(nombre="Carlos Gómez", matricula="A003", calificacion=78.0),
    Estudiante(nombre="Ana Torres", matricula="A004", calificacion=95.0)
]

# Manejo del caso especial: lista vacía
if not estudiantes:
    raise ValueError("La lista de estudiantes no puede estar vacía.")

# Inicializamos el mejor estudiante como el primero
mejor_estudiante = estudiantes[0]

# Iteramos sobre los estudiantes para encontrar al mejor
for estudiante in estudiantes:
    if estudiante.calificacion > mejor_estudiante.calificacion:
        mejor_estudiante = estudiante

# Salida del resultado
print(f"El estudiante con la calificación más alta es: {mejor_estudiante.nombre}")