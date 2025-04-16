grafos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D'],
}

#Imprimir grado de cada nodo
def imprimir_Grados(grafo):
    print('Grado de cada vertice:')
    for nodo in grafo:
        grado = len(grafo[nodo])
        print(f'{nodo}: {grado}')

def vertice_mayor_grado(grafo):
    max_nodo = None
    max_grado = -1
    for nodo in grafo:
        grado = len(grafo[nodo])
        if grado > max_grado:
            max_grado = grado
            max_nodo = nodo

    return max_nodo, max_grado

def es_regular(grafo):
    grados = [len(grafo[nodo])for nodo in grafo]
    return all(grado == grados[0] for grado in grados)

#ejecutar funcion
imprimir_Grados(grafos)

nodo_max, grado_max = vertice_mayor_grado(grafos)
print(f"Nodo con mayor grado: {nodo_max} (grado {nodo_max})")

if es_regular(grafos):
    print("El grafo es  regular (todos los nodos tienen el mismo grado")
else:
    print("El grafo no es regular")