# Arreglo de ejemplo
valores = [3, -1, 2, -1, 5, -3, 4]

# Manejo del caso especial: arreglo vacío
if not valores:
    raise ValueError("El arreglo no puede estar vacío.")

# Inicialización de variables
suma_en_progreso = suma_optima = valores[0]

# Iteración a través del arreglo
for elemento in valores[1:]:
    suma_en_progreso = max(elemento, suma_en_progreso + elemento)  # Decide si continuar o iniciar un nuevo subarreglo
    suma_optima = max(suma_optima, suma_en_progreso) # Actualiza la suma máxima global

# Salida del resultado
print(f"La suma máxima del subarreglo es: {suma_optima}")