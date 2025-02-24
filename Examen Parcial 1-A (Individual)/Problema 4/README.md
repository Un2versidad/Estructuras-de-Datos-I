![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 4: Determinar Subconjuntos entre Conjuntos**

## **📖 Descripción del Problema**
Se tienen dos conjuntos de números enteros. Escribe un programa que determine 
si uno es subconjunto del otro.

- Si A es subconjunto de B.
- Si B es subconjunto de A.
- Si ambos conjuntos son iguales.

### **📥 Entrada**
- Dos conjuntos A y B.

### **📤 Salida**
- Indicar si A es subconjunto de B, si B es subconjunto de A, y si ambos conjuntos son iguales.

### **📋 Requisitos**
1. Utilizar alguna de las siguientes estructuras de datos:
   - Arreglos, conjuntos, registros, listas, listas enlazadas, pilas o colas.
2. Implementar las operaciones de verificación de subconjuntos.
3. Determinar la complejidad temporal de cada operación.

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
Se utiliza la estructura de **conjuntos** (`set`) en Python, que es ideal para este tipo de operaciones debido a su eficiencia y soporte nativo para verificar subconjuntos.

### **💻 Explicación del Código**
El código realiza las siguientes operaciones directamente sobre los conjuntos:

1. **🔍 Verificar si A ⊆ B**:
   - Se utiliza el método `.issubset()` para determinar si todos los elementos de A están en B.

2. **🔍 Verificar si B ⊆ A**:
   - Se utiliza el mismo método `.issubset()` para determinar si todos los elementos de B están en A.

3. **🔍 Verificar si A y B son iguales**:
   - Se verifica si A es subconjunto de B y B es subconjunto de A. Esto implica que ambos conjuntos tienen exactamente los mismos elementos.

### **📊 Tabla de Ejecución Paso a Paso**
Dados los conjuntos A = {2, 4, 6} y B = {1, 2, 3, 4, 5, 6}, las operaciones funcionan así:

| Operación                     | Resultado                     |
|-------------------------------|-------------------------------|
| ¿Es A ⊆ B?                    | Sí                            |
| ¿Es B ⊆ A?                    | No                            |
| ¿Son A y B iguales?           | No                            |

### **⏱️ Complejidad Temporal**
1. **Verificar si A ⊆ B**:
   - Complejidad: O(|A|), donde |A| es el tamaño del conjunto A.
   - Explicación: Se verifica si cada elemento de A está en B. La búsqueda en un conjunto tiene complejidad promedio de O(1).

2. **Verificar si B ⊆ A**:
   - Complejidad: O(|B|), donde |B| es el tamaño del conjunto B.
   - Explicación: Similar al caso anterior, pero ahora se verifica cada elemento de B en A.

3. **Verificar si A y B son iguales**:
   - Complejidad: O(min(|A|, |B|)).
   - Explicación: Se realizan ambas verificaciones (A ⊆ B y B ⊆ A), pero solo hasta el tamaño del conjunto más pequeño.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza un **conjunto** (`set`) como estructura de datos principal.
   - Los conjuntos son ideales para este problema porque permiten realizar operaciones como verificación de subconjuntos de manera eficiente.

2. **Por Qué Se Usó un Conjunto**:
   - Los conjuntos en Python son implementaciones de tablas hash, lo que garantiza tiempos de búsqueda, inserción y eliminación promedio de O(1).
   - No se necesitan estructuras adicionales como arreglos, listas enlazadas, pilas o colas, ya que los conjuntos ya están optimizados para estas operaciones.

3. **Eficiencia**:
   - Complejidad temporal: O(|A| + |B|) para verificar ambas relaciones de subconjunto.
   - Complejidad espacial: O(1), ya que no se crean nuevos conjuntos adicionales.

### **📢 Salida del Código**
Observa la salida en la consola:
```
Conjunto A: {2, 4, 6}
Conjunto B: {1, 2, 3, 4, 5, 6}
El conjunto A ({2, 4, 6}) es subconjunto del conjunto B ({1, 2, 3, 4, 5, 6}).
El conjunto B ({1, 2, 3, 4, 5, 6}) NO es subconjunto del conjunto A ({2, 4, 6}).
Los conjuntos A y B NO son iguales.
```
