![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 3: Operaciones con Conjuntos**

## **📖 Descripción del Problema**
Dado dos conjuntos AAA y BBB, implementar operaciones para:
1. Obtener la **unión** de ambos conjuntos.
2. Obtener la **intersección** de ambos conjuntos.
3. Obtener la **diferencia**  A−BA - BA−B.

### **📥 Entrada**
- Dos conjuntos AAA y BBB.

### **📤 Salida**
- La unión, intersección y diferencia de los conjuntos.

### **📋 Requisitos**
1. Utilizar alguna de las siguientes estructuras de datos:
   - Arreglos, conjuntos, registros, listas, listas enlazadas, pilas o colas.
2. Implementar las operaciones de unión, intersección y diferencia sin el uso de funciones adicionales.
3. Determinar la complejidad temporal de cada operación.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
Se utiliza la estructura de **conjuntos** (`set`) en Python, que es ideal para este tipo de operaciones debido a su eficiencia y soporte nativo para operaciones como unión, intersección y diferencia.

### **💻 Explicación del Código**
El código realiza las siguientes operaciones directamente sobre los conjuntos sin el uso de funciones adicionales:

1. **🌐 Unión**:
   - Combina todos los elementos de AAA y BBB, eliminando duplicados.
   - Se utiliza el método `.union()`.

2. **🔍 Intersección**:
   - Encuentra los elementos comunes entre AAA y BBB.
   - Se utiliza el método `.intersection()`.

3. **➖ Diferencia AAA - BBB (A−B)**:
   - Encuentra los elementos que están en AAA pero no en BBB.
   - Se utiliza el método `.difference()`.

### **📊 Tabla de Ejecución Paso a Paso**
Dados los conjuntos AAA = {1, 2, 3, 4, 5} y BBB = {4, 5, 6, 7, 8}, las operaciones funcionan así:

| Operación                       | Resultado                    |
|---------------------------------|------------------------------|
| Unión (AAA ∪ BBB)               | {1, 2, 3, 4, 5, 6, 7, 8}     |
| Intersección (AAA ∩ BBB)        | {4, 5}                       |
| Diferencia (AAA - BBB)          | {1, 2, 3}                    |

### **⏱️ Complejidad Temporal**
1. **Unión**:
   - Complejidad: O(|AAA| + |BBB|), donde |AAA| y |BBB| son los tamaños de los conjuntos AAA y BBB.
   - Explicación: Se recorre cada elemento de ambos conjuntos para combinarlos.

2. **Intersección**:
   - Complejidad: O(min(|AAA|, |BBB|)).
   - Explicación: Se comparan los elementos de ambos conjuntos para encontrar los comunes.

3. **Diferencia**:
   - Complejidad: O(|AAA|).
   - Explicación: Se recorre el conjunto AAA para eliminar los elementos que también están en BBB.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza un **conjunto** (`set`) como estructura de datos principal.
   - Los conjuntos son ideales para este problema porque permiten realizar operaciones como unión, intersección y diferencia de manera eficiente.

2. **Por Qué Se Usó un Conjunto**:
   - Los conjuntos en Python son implementaciones de tablas hash, lo que garantiza tiempos de búsqueda, inserción y eliminación promedio de O(1).
   - No se necesitan estructuras adicionales como arreglos, listas enlazadas, pilas o colas, ya que los conjuntos ya están optimizados para estas operaciones.

3. **Eficiencia**:
   - Complejidad temporal: O(|AAA| + |BBB|) para la unión, O(min(|AAA|, |BBB|)) para la intersección y O(|AAA|) para la diferencia.
   - Complejidad espacial: O(|AAA| + |BBB|), ya que se crean nuevos conjuntos para almacenar los resultados.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Conjunto AAA: {1, 2, 3, 4, 5}
Conjunto BBB: {4, 5, 6, 7, 8}
Unión de AAA y BBB: {1, 2, 3, 4, 5, 6, 7, 8}
Intersección de AAA y BBB: {4, 5}
A−BA - BA−B: {1, 2, 3}
```
