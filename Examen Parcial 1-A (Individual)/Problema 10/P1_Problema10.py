# Definimos una clase para implementar una pila utilizando un arreglo dinámico
class Pila:
    def __init__(self):
        self.arreglo = []  # Arreglo dinámico para almacenar los elementos

    def push(self, x):
        """
        Agrega un elemento al tope de la pila.

        :param x: El elemento a agregar.
        """
        self.arreglo.append(x)

    def pop(self):
        """
        Elimina el elemento en el tope de la pila.

        :return: El elemento eliminado, o None si la pila está vacía.
        """
        if not self.arreglo:
            return None
        return self.arreglo.pop()

    def top(self):
        """
        Obtiene el elemento en el tope de la pila sin eliminarlo.

        :return: El elemento en el tope, o None si la pila está vacía.
        """
        if not self.arreglo:
            return None
        return self.arreglo[-1]

    def esta_vacia(self):
        """
        Verifica si la pila está vacía.

        :return: True si la pila está vacía, False en caso contrario.
        """
        return len(self.arreglo) == 0


def esta_balanceada(express):
    """
    Verifica si una expresión matemática con paréntesis, corchetes y llaves está bien balanceada.

    :param express: La expresión a verificar.
    :return: Bool - True si está balanceada, False en caso contrario.
    """
    # Diccionario para emparejar símbolos de cierre con sus correspondientes de apertura
    parejas = {')': '(', ']': '[', '}': '{'}

    # Conjunto de símbolos de apertura
    simbolos_apertura = {'(', '[', '{'}

    # Crear una pila
    pila = Pila()

    # Recorrer cada carácter en la expresión
    for caracter in express:
        if caracter in simbolos_apertura:
            # Si es un símbolo de apertura, lo agregamos a la pila
            pila.push(caracter)
        elif caracter in parejas:
            # Si es un símbolo de cierre, verificamos si coincide con el tope de la pila
            if pila.top() == parejas[caracter]:
                pila.pop()  # Eliminamos el símbolo de apertura correspondiente
            else:
                return False  # No está balanceado

    # Al final, la pila debe estar vacía si la expresión está balanceada
    return pila.esta_vacia()

# Ejemplos de expresiones balanceadas y no balanceadas
expresiones = [
    "({[()]})",  # Balanceado
    "({[(])})",  # No balanceado
    "([]{})",  # Balanceado
    "([)]",  # No balanceado
    "{{[[(())]]}}"  # Balanceado
]

for expresion in expresiones:
    if esta_balanceada(expresion):
        print(f"La expresión '{expresion}' está balanceada.")
    else:
        print(f"La expresión '{expresion}' NO está balanceada.")