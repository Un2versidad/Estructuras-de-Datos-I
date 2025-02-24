![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 2: Ordenamiento por Inserción**

## **📖 Descripción del Problema**
Implementa un algoritmo que ordene un arreglo de números enteros utilizando el algoritmo de Ordenamiento por Inserción y determine su complejidad temporal.

## **📋 Ejemplo de Entrada y Salida**

### **📥 Entrada**
```python
datos = [22, 15, 8, 3, 7, 10]
```

### **📤 Salida**
```
Arreglo original: [22, 15, 8, 3, 7, 10]
Arreglo ordenado: [3, 7, 8, 10, 15, 22]
```

## **💡 Solución Propuesta**

### **🚀 Algoritmo de Ordenamiento por Inserción**
El algoritmo sigue estos pasos:

1. **📝 Inicialización**:
   - Comenzamos desde el segundo elemento del arreglo (`indice_actual = 1`).
   - Suponemos que el primer elemento ya está ordenado.

2. **🔄 Iteración**:
   - Para cada `valor_actual`, lo comparamos con los elementos anteriores.
   - Si encontramos un elemento mayor que `valor_actual`, lo movemos una posición hacia adelante.
   - Continuamos este proceso hasta encontrar la posición correcta para `valor_actual`.

3. **📍 Inserción**:
   - Insertamos `valor_actual` en su posición correcta dentro de la parte ordenada del arreglo.

4. **🏆 Resultado**:
   - Al final de la iteración, el arreglo estará completamente ordenado.

## **💻 Explicación del Código**

1. **📝 Nombres de Variables Mejorados**:
   - `indice_actual`: Representa el índice del elemento que estamos procesando.
   - `valor_actual`: El valor del elemento que queremos insertar en su posición correcta.
   - `indice_previo`: Índice del elemento anterior que estamos comparando con `valor_actual`.

2. **🔧 Optimización**:
   - El uso de nombres descriptivos mejora la legibilidad del código.
   - No se realizan cambios significativos en la lógica, ya que el algoritmo de inserción es inherentemente simple y eficiente para su propósito.

3. **📊 Salida**:
   - Se imprime el arreglo antes y después de ordenarlo para facilitar la verificación.

## **⏱️ Complejidad Temporal y Espacial**

### **⏳ Complejidad Temporal**
- **Peor Caso**: O(N²), donde N es el número de elementos en el arreglo.
  - Ocurre cuando el arreglo está en orden inverso.
- **Mejor Caso**: O(N), cuando el arreglo ya está ordenado.
  - En este caso, el bucle interno no se ejecuta.
- **Caso Promedio**: O(N²).

### **💾 Complejidad Espacial**
- **Espacio**: O(1).
  - El algoritmo opera directamente sobre el arreglo original sin usar memoria adicional.

## **🌟 Casos de Prueba Adicionales**

### **✅ Caso 1: Arreglo Casi Ordenado**
```python
datos = [1, 2, 4, 3, 5]
```
**Salida**:
```
Arreglo original: [1, 2, 4, 3, 5]
Arreglo ordenado: [1, 2, 3, 4, 5]
```

### **❌ Caso 2: Arreglo en Orden Inverso**
```python
datos = [10, 9, 8, 7, 6]
```
**Salida**:
```
Arreglo original: [10, 9, 8, 7, 6]
Arreglo ordenado: [6, 7, 8, 9, 10]
```

### **⚠️ Caso 3: Arreglo Vacío**
```python
datos = []
```
**Salida**:
```
Arreglo original: []
Arreglo ordenado: []
```

### **📍 Caso 4: Arreglo con Un Solo Elemento**
```python
datos = [42]
```
**Salida**:
```
Arreglo original: [42]
Arreglo ordenado: [42]
```

## **📢 Salida del Código**
Observa la salida en la consola:
```
Arreglo original: [22, 15, 8, 3, 7, 10]
Arreglo ordenado: [3, 7, 8, 10, 15, 22]
```
