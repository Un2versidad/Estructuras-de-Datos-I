![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# **🎯 Problema 10: Verificación de Expresiones Balanceadas**

## **📖 Descripción del Problema**
Escribe un programa que verifique si una expresión matemática con paréntesis, corchetes y llaves está bien balanceada utilizando una pila.  
Por ejemplo:  
- `({[()]})` → Balanceado  
- `({[(])})` → No balanceado  

## **💡 Solución Propuesta**

### **🗃️ Estructura de Datos Utilizada**
1. **Clase `Pila`**:
   - Implementa una pila utilizando un **arreglo dinámico** (`list` en Python).
   - Contiene métodos para realizar las operaciones `push`, `pop`, `top` y verificar si está vacía.

2. **Función `esta_balanceada(expres)`**:
   - Utiliza una pila para verificar si una expresión está balanceada.
   - Empareja símbolos de cierre con sus correspondientes de apertura utilizando un diccionario.

### **💻 Explicación del Código**

#### **Clase `Pila`**
- **Constructor (`__init__`)**:
  - Inicializa un arreglo vacío (`self.arreglo`) para almacenar los elementos de la pila.

- **Método `push(x)`**:
  - Agrega un elemento al final del arreglo, que representa el tope de la pila.

- **Método `pop()`**:
  - Elimina y devuelve el último elemento del arreglo, que representa el tope de la pila.
  - Si la pila está vacía, devuelve `None`.

- **Método `top()`**:
  - Devuelve el último elemento del arreglo sin eliminarlo.
  - Si la pila está vacía, devuelve `None`.

- **Método `esta_vacia()`**:
  - Verifica si la pila está vacía comprobando si su longitud es cero.

#### **Función `esta_balanceada(expresion)`**
- **Diccionario `parejas`**:
  - Asocia cada símbolo de cierre (`)`, `]`, `}`) con su correspondiente símbolo de apertura (`(`, `[`, `{`).

- **Conjunto `simbolos_apertura`**:
  - Contiene los símbolos de apertura para identificarlos fácilmente.

- **Lógica Principal**:
  1. Recorre cada carácter de la expresión.
  2. Si es un símbolo de apertura, lo agrega a la pila.
  3. Si es un símbolo de cierre, verifica si coincide con el tope de la pila:
     - Si coincide, elimina el símbolo de apertura de la pila.
     - Si no coincide, la expresión no está balanceada.
  4. Al final, verifica si la pila está vacía:
     - Si está vacía, la expresión está balanceada.
     - Si no está vacía, la expresión no está balanceada.

### **📋 Tabla de Ejecución Paso a Paso**

#### **Expresiones de Ejemplo**
1. `"({[()]})"` → Balanceado
   - Apilado: `(`, `{`, `[`, `(`.
   - Desapilado correctamente: `)`, `]`, `}`, `)`.
   - Resultado: Balanceado.

2. `"({[(])})"` → No Balanceado
   - Apilado: `(`, `{`, `[`, `(`.
   - Error al desapilar: `]` no coincide con `(`.
   - Resultado: No balanceado.

3. `"([]{})"` → Balanceado
   - Apilado: `(`, `[`.
   - Desapilado correctamente: `]`, `)`, `{`, `}`.
   - Resultado: Balanceado.

4. `"([)]"` → No Balanceado
   - Apilado: `(`, `[`.
   - Error al desapilar: `)` no coincide con `[`.
   - Resultado: No balanceado.

5. `"{{[[(())]]}}"` → Balanceado
   - Apilado: `{`, `{`, `[`, `[`, `(`, `(`.
   - Desapilado correctamente: `)`, `)`, `]`, `]`, `}`, `}`.
   - Resultado: Balanceado.

### **⏱️ Complejidad Temporal**
1. **Recorrido de la Expresión**:
   - Complejidad: O(N), donde N es la longitud de la expresión.
   - Se recorre cada carácter una sola vez.

2. **Operaciones de la Pila**:
   - Complejidad: O(1) para `push`, `pop` y `top`.

3. **Verificación Final**:
   - Complejidad: O(1) para verificar si la pila está vacía.

### **✅ Cumplimiento de los Requisitos**
1. **Estructura de Datos Utilizada**:
   - Se utiliza una **pila** para manejar los símbolos de apertura y verificar su correspondencia con los símbolos de cierre.

2. **Por Qué Se Usó una Pila**:
   - Las pilas son ideales para este problema porque permiten manejar estructuras anidadas (como paréntesis, corchetes y llaves) en orden inverso al que fueron insertadas.

3. **Eficiencia**:
   - Complejidad temporal: O(N), donde N es la longitud de la expresión.
   - Complejidad espacial: O(N), ya que la pila puede almacenar hasta N/2 elementos en el peor caso.

### **📢 Salida del Código**
Observa la salida en la consola:
```
La expresión '({[()]})' está balanceada.
La expresión '({[(])})' NO está balanceada.
La expresión '([]{})' está balanceada.
La expresión '([)]' NO está balanceada.
La expresión '{{[[(())]]}}' está balanceada.
```
