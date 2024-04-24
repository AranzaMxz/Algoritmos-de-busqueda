from ABB.Tree import Tree
from ABB.busqueda_ABB import busquedaABB
import math
import numpy as np
import time

def ingresarDatos(lista):
    # Determina el nodo raíz
    posNodoRaiz = math.ceil(len(lista)/2) - 1 # redondeamos hacia arriba el número
    nodoRaiz = lista[posNodoRaiz]
    
    #lista = np.delete(lista,posNodoRaiz)
    
    # Agregamos nodo raíz
    arbol = Tree(nodoRaiz)
    arbol.root.position = posNodoRaiz

    for i in range(len(lista)):
        x = lista[i]
        arbol.add_node(x, i)

    return arbol
    #arbol.inorder_route()

def ABB(vector, valor_busqueda):
    print("\n----------- ÁRBOL DE BUSQUEDA BINARIA -----------\n")
    print("____ Lista desordenada ____\n", vector)
    
    arbol = ingresarDatos(vector)
    
    start_time = time.time()
    busquedaABB(arbol, valor_busqueda)
    end_time = time.time()

    temporizador = end_time - start_time
    print(f"Tiempo de ejecución: {temporizador:f} segundos")

