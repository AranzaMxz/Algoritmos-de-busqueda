from Tree import Tree
import math
import numpy as np


def busquedaABB(arbol, busqueda):
    n = arbol.search(busqueda)
    if n is None:
        print(f"{busqueda} no existe")
    else:
        print(f"{busqueda} sí existe")

def ingresarDatos(vector):
    # Determina el nodo raíz
    posNodoRaiz = math.ceil(len(vector)/2) - 1 # redondeamos hacia arriba el número
    nodoRaiz = vector[posNodoRaiz]
    
    vector = np.delete(vector,posNodoRaiz)
    #print("pos: ", posNodoRaiz)
    print(nodoRaiz)
    # Agregamos nodo raíz
    arbol = Tree(nodoRaiz)
    for i in range(len(vector)):
        x = vector[i]
        arbol.add_node(x)

    return arbol
    #arbol.inorder_route()

def ABB(vector, numBuscar):
    arbol = ingresarDatos(vector)
    busquedaABB(arbol, numBuscar)