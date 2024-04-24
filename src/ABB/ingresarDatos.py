from ABB.Tree import Tree
from ABB.busqueda_ABB import busquedaABB
import math
import numpy as np
import time

def ingresarDatos(vector):
    # Determina el nodo raíz
    posNodoRaiz = math.ceil(len(vector)/2) - 1 # redondeamos hacia arriba el número
    nodoRaiz = vector[posNodoRaiz]
    
    vector = np.delete(vector,posNodoRaiz)
    #print("pos: ", posNodoRaiz)
    #print(nodoRaiz)
    # Agregamos nodo raíz
    arbol = Tree(nodoRaiz)
    for i in range(len(vector)):
        x = vector[i]
        arbol.add_node(x)

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

