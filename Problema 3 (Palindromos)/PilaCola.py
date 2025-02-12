from collections import deque

#Cola
class Cola: #FIFO
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if  not self.esta_vacia():
            return self.elementos.popleft()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

#Pila
class Pila: #LIFO
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0