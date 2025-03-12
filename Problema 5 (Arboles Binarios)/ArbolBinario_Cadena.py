class Nodo:
    def __init__(self, palabra):
        self.izquierda = None
        self.derecha = None
        self.valor = palabra
        
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = Nodo(palabra)
        else:
            self.insertarRecursivo(palabra, self.raiz)

    def insertarRecursivo(self, palabra, nodo):
        if palabra < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(palabra)
            else:
                self.insertarRecursivo(palabra, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(palabra)
            else:
                self.insertarRecursivo(palabra, nodo.derecha)

    def inorden(self, nodo):
        elementos = []
        self.inordenRecursivo(nodo, elementos)
        print(self.formatear_salida(elementos))

    def preorden(self, nodo):
        elementos = [] 
        self.preordenRecursivo(nodo, elementos)
        print(self.formatear_salida(elementos))

    def postorden(self, nodo):
        elementos = []
        self.postordenRecursivo(nodo, elementos)
        print(self.formatear_salida(elementos))

    def inordenRecursivo(self, nodo, elementos):
        if nodo is not None:
            self.inordenRecursivo(nodo.izquierda, elementos)
            elementos.append(str(nodo.valor))
            self.inordenRecursivo(nodo.derecha, elementos)

    def preordenRecursivo(self, nodo, elementos):
        if nodo is not None:
            elementos.append(str(nodo.valor))
            self.preordenRecursivo(nodo.izquierda, elementos)
            self.preordenRecursivo(nodo.derecha, elementos)

    def postordenRecursivo(self, nodo, elementos):
        if nodo is not None:
            self.postordenRecursivo(nodo.izquierda, elementos)
            self.postordenRecursivo(nodo.derecha, elementos)
            elementos.append(str(nodo.valor))

    def formatear_salida(self, elementos):
        if len(elementos) == 0:
            return ""
        elif len(elementos) == 1:
            return elementos[0]
        else:
            return ", ".join(elementos[:-1]) + " y " + elementos[-1]

arbol = ArbolBinario()
palabras = ["manzana", "banana", "cereza", "uva", "pera", "sandia", "limon"]

for palabra in palabras:
    arbol.insertar(palabra)

print("\nInorden:")
arbol.inorden(arbol.raiz)

print("\nPreorden:")
arbol.preorden(arbol.raiz)

print("\nPostorden:")
arbol.postorden(arbol.raiz)