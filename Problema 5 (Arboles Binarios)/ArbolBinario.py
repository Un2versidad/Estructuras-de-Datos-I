# Arboles Binarios (Estructura de Datos I)

# Preorden (Todo lo que esta en la izquierda, luego lo que esta en la raiz y luego lo que esta en la derecha).
# Inorden (Raiz, luego todo lo que esta en la izquierda y luego todo lo que esta en la derecha).
# Postorden (Todo lo que esta en la izquierda, luego todo lo que esta en la derecha y la raiz).

class Nodo:
  def __init__(self, clave):
      self.izquierda = None
      self.derecha = None
      self.valor = clave

class ArbolBinario:
  def __init__(self):
    self.raiz = None

  def insertar(self, clave):
    if self.raiz is None:
      self.raiz = Nodo(clave)
    else:
      self.insertarRecursivo(clave, self.raiz)

  def insertarRecursivo(self, clave, nodo):
    if clave < nodo.valor:
      if nodo.izquierda is None:
        nodo.izquierda = Nodo(clave)
      else:
        self.insertarRecursivo(clave, nodo.izquierda)
    else:
      if nodo.derecha is None:
        nodo.derecha = Nodo(clave)
      else:
        self.insertarRecursivo(clave, nodo.derecha)

  def inorden(self, nodo):
    if nodo is not None:
      self.inorden(nodo.izquierda)
      print(nodo.valor, end=" ")
      self.inorden(nodo.derecha)
  
  def preorden(self, nodo):
    if nodo is not None:
      print(nodo.valor, end=" ")
      self.preorden(nodo.izquierda)
      self.preorden(nodo.derecha)
    
  def postorden(self, nodo):
    if nodo is not None:
      self.postorden(nodo.izquierda)
      self.postorden(nodo.derecha)
      print(nodo.valor, end=" ")

arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("\nRecorrido Inorden:")
arbol.inorden(arbol.raiz)

print("\nRecorrido Preorden:")
arbol.preorden(arbol.raiz)

print("\nRecorrido Postorden:")
arbol.postorden(arbol.raiz)

print()