![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 1: Suma Máxima de Subarreglo (Algoritmo de Kadane)**

## **📖 Descripción del Problema**
Dado un arreglo de enteros de tamaño NNN, escribir una función que encuentre el subarreglo contiguo con la suma más grande y devuelva dicha suma.

## **📋 Ejemplo de Entrada y Salida**

### **📥 Entrada**
```python
valores = [3, -1, 2, -1, 5, -3, 4]
```

### **📤 Salida**
```
La suma máxima del subarreglo es: 9
```

### **🔍 Explicación**
El subarreglo con la suma máxima es `[3, -1, 2, -1, 5]`, cuya suma es `9`.

## **💡 Solución Propuesta**

### **🚀 Algoritmo de Kadane**
El algoritmo sigue estos pasos:

1. **📝 Inicialización**:
   - `suma_en_progreso`: Almacena la suma máxima del subarreglo que termina en el índice actual.
   - `suma_optima`: Almacena la suma máxima global encontrada hasta el momento.

2. **🔄 Iteración**:
   - Para cada `elemento` del arreglo, decidimos si incluirlo en el subarreglo actual o comenzar un nuevo subarreglo desde ese elemento.
   - Actualizamos `suma_en_progreso` como el máximo entre el valor actual (`elemento`) y la suma acumulada (`suma_en_progreso + elemento`).
   - Si `suma_en_progreso` supera `suma_optima`, actualizamos `suma_optima`.

3. **🏆 Resultado**:
   - Al final de la iteración, `suma_optima` contiene la suma máxima del subarreglo.

## **💻 Explicación del Código**

1. **⚠️ Manejo del Caso Especial**:
   - Si el arreglo está vacío, se lanza una excepción indicando que el arreglo no puede estar vacío.

2. **📝 Inicialización**:
   - `suma_en_progreso` y `suma_optima` se inicializan con el primer elemento del arreglo.

3. **🔄 Iteración**:
   - Se recorre el arreglo desde el segundo elemento.
   - En cada paso, se decide si continuar el subarreglo actual o iniciar uno nuevo.
   - Si `suma_en_progreso` supera `suma_optima`, se actualiza `suma_optima`.

4. **📊 Salida**:
   - Se imprime la suma máxima del subarreglo.

## **🌟 Casos de Prueba Adicionales**

### **✅ Caso 1: Todos los Elementos Positivos**
```python
valores = [1, 2, 3, 4, 5]
```
**Salida**:
```
La suma máxima del subarreglo es: 15
```

### **❌ Caso 2: Todos los Elementos Negativos**
```python
valores = [-5, -2, -3, -1]
```
**Salida**:
```
La suma máxima del subarreglo es: -1
```

### **⚠️ Caso 3: Arreglo Vacío**
```python
valores = []
```
**Salida**:
```
ValueError: El arreglo no puede estar vacío.
```

### **📍 Caso 4: Un Solo Elemento**
```python
valores = [7]
```
**Salida**:
```
La suma máxima del subarreglo es: 7
```

## **📢 Salida del Código**
Observa la salida en la consola:
```
La suma máxima del subarreglo es: 9
```

### **🔍 Verificación de la Salida**
Para el arreglo `[3, -1, 2, -1, 5, -3, 4]`, sigamos paso a paso el algoritmo:

1. **📝 Inicialización**:
   - `suma_en_progreso = suma_optima = 3` (primer elemento).

2. **🔄 Iteración**:
   - **Índice 1**: `elemento = -1`
     - `suma_en_progreso = max(-1, 3 + (-1)) = max(-1, 2) = 2`
     - `suma_optima = max(3, 2) = 3`
   - **Índice 2**: `elemento = 2`
     - `suma_en_progreso = max(2, 2 + 2) = max(2, 4) = 4`
     - `suma_optima = max(3, 4) = 4`
   - **Índice 3**: `elemento = -1`
     - `suma_en_progreso = max(-1, 4 + (-1)) = max(-1, 3) = 3`
     - `suma_optima = max(4, 3) = 4`
   - **Índice 4**: `elemento = 5`
     - `suma_en_progreso = max(5, 3 + 5) = max(5, 8) = 8`
     - `suma_optima = max(4, 8) = 8`
   - **Índice 5**: `elemento = -3`
     - `suma_en_progreso = max(-3, 8 + (-3)) = max(-3, 5) = 5`
     - `suma_optima = max(8, 5) = 8`
   - **Índice 6**: `elemento = 4`
     - `suma_en_progreso = max(4, 5 + 4) = max(4, 9) = 9`
     - `suma_optima = max(8, 9) = 9`
