from collections import deque

# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ").lower()

# Inicializar cola y pila
cola = deque(palabra)  # Cola (FIFO)
pila = list(palabra)   # Pila (LIFO)

# Verificar si la palabra es un palíndromo
es_palindromo = True
while cola and pila:
    if cola.popleft() != pila.pop():
        es_palindromo = False
        break

# Mostrar el resultado
print("Es un palíndromo" if es_palindromo else "No es un palíndromo")