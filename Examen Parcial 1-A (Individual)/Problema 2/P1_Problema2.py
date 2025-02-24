# Arreglo de ejemplo
datos = [22, 15, 8, 3, 7, 10]
print("Arreglo original:", datos)

# Algoritmo de Ordenamiento por Inserción
for indice_actual in range(1, len(datos)):
    valor_actual = datos[indice_actual]  # Elemento que vamos a insertar en su posición correcta
    indice_previo = indice_actual - 1

    # Movemos los elementos mayores que 'valor_actual' una posición hacia adelante
    while indice_previo >= 0 and datos[indice_previo] > valor_actual:
        datos[indice_previo + 1] = datos[indice_previo]
        indice_previo -= 1

    # Insertamos 'valor_actual' en su posición correcta
    datos[indice_previo + 1] = valor_actual

# Salida del arreglo ordenado
print("Arreglo Ordenado:", datos)