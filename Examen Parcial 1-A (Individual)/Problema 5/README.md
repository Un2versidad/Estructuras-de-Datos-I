![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 5: Estudiante con la Calificación Más Alta**

## **📖 Descripción del Problema**
Definir una estructura que almacene los datos de un estudiante (nombre, matrícula, calificación). Luego, escribir un programa que reciba un arreglo de estudiantes y devuelva el nombre del estudiante con la calificación más alta.

### **📥 Entrada**
- Un arreglo de objetos `Estudiante`, donde cada objeto contiene:
  - `nombre`: Nombre del estudiante.
  - `matricula`: Matrícula del estudiante.
  - `calificacion`: Calificación del estudiante.

### **📤 Salida**
- El nombre del estudiante con la calificación más alta.

### **📋 Requisitos**
1. Utilizar alguna de las siguientes estructuras de datos:
   - Arreglos, conjuntos, registros, listas, listas enlazadas, pilas o colas.
2. Implementar una solución eficiente para encontrar al estudiante con la calificación más alta.
3. Manejar casos especiales, como una lista vacía.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
Se utiliza una **clase tradicional** (`Estudiante`) para almacenar los datos de cada estudiante. Los estudiantes se almacenan en una **lista** (arreglo), que es ideal para iterar y comparar sus elementos.

### **💻 Explicación del Código**
El código realiza las siguientes operaciones:

1. **📝 Definición de la Estructura**:
   - Se define la clase `Estudiante` con tres atributos: `nombre`, `matricula` y `calificacion`.
   - El constructor (`__init__`) inicializa estos atributos cuando se crea un objeto.

2. **🔄 Inicialización de Variables**:
   - Se inicializa el primer estudiante como el "mejor estudiante".

3. **🔍 Iteración para Encontrar el Mejor Estudiante**:
   - Se recorre la lista de estudiantes y se compara la calificación de cada estudiante con la del "mejor estudiante".
   - Si se encuentra un estudiante con una calificación mayor, se actualiza el "mejor estudiante".

4. **⚠️ Manejo de Casos Especiales**:
   - Si la lista de estudiantes está vacía, se lanza una excepción (`ValueError`).

5. **📊 Salida del Resultado**:
   - Al final, se imprime el nombre del estudiante con la calificación más alta.

### **📋 Tabla de Ejecución Paso a Paso**
Dados los siguientes estudiantes:

| Nombre       | Matrícula | Calificación |
|--------------|-----------|--------------|
| Juan Carlos  | A001      | 85.5         |
| María López  | A002      | 92.3         |
| Carlos Gómez | A003      | 78.0         |
| Ana Torres   | A004      | 95.0         |

El proceso funciona así:

| Iteración | Estudiante Actual | Calificación | Mejor Estudiante Actual | Calificación Mejor |
|-----------|-------------------|--------------|-------------------------|--------------------|
| Inicial   | -                 | -            | Juan Carlos             | 85.5               |
| 1         | Juan Carlos       | 85.5         | Juan Carlos             | 85.5               |
| 2         | María López       | 92.3         | María López             | 92.3               |
| 3         | Carlos Gómez      | 78.0         | María López             | 92.3               |
| 4         | Ana Torres        | 95.0         | Ana Torres              | 95.0               |

**Resultado Final**: `Ana Torres`.

### **⏱️ Complejidad Temporal**
1. **Iteración sobre la Lista**:
   - Complejidad: O(N), donde N es el número de estudiantes en la lista.
   - Explicación: Se recorre la lista una sola vez para encontrar al estudiante con la calificación más alta.

2. **Manejo de Casos Especiales**:
   - Complejidad: O(1), ya que solo se verifica si la lista está vacía.

3. **Espacial**:
   - Complejidad: O(1), ya que no se utilizan estructuras adicionales aparte de las variables para almacenar el "mejor estudiante".

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza una **lista** para almacenar los estudiantes.
   - Cada estudiante se representa mediante una **clase tradicional** (`Estudiante`), que es una estructura de registro.

2. **Por Qué Se Usó una Lista**:
   - Las listas son ideales para este problema porque permiten iterar y comparar los elementos fácilmente.
   - No se necesitan estructuras adicionales como conjuntos, pilas o colas, ya que el problema no implica operaciones específicas de estas estructuras.

3. **Eficiencia**:
   - Complejidad temporal: O(N), ya que se recorre la lista una sola vez.
   - Complejidad espacial: O(1), ya que solo se usan variables adicionales para almacenar el "mejor estudiante".

### **📢 Salida del Código**
Observa la salida en la consola:
```
El estudiante con la calificación más alta es: Ana Torres
```
