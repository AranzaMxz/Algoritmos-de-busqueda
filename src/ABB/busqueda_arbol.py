from Tree import Tree
import math

#arbol_numeros = Tree(5)
#arbol_numeros.add_node(1984)
#arbol_numeros.add_node(60)
#arbol_numeros.add_node(10)
#arbol_numeros.add_node(20)
#arbol_numeros.add_node(10)
#arbol_numeros.add_node(25)
#arbol_numeros.add_node(64)
#arbol_numeros.add_node(10)
#arbol_numeros.add_node(19)
#arbol_numeros.add_node(23)
#arbol_numeros.add_node(18)
#arbol_numeros.add_node(1)
#arbol_numeros.add_node(2013)
#arbol_numeros.preorder_route()
#arbol_numeros.inorder_route()
#arbol_numeros.postorder_route()
'''
def busquedaArbol(busqueda):
    n = arbol_numeros.search(busqueda)
    if n is None:
        print(f"{busqueda} no existe")
    else:
        print(f"{busqueda} sí existe")
'''
def ingresarDatos(vector):
    # Determina el nodo raíz
    posNodoRaiz = math.ceil(len(vector)/2) - 1 # redondeamos hacia arriba el número
    nodoRaiz = vector[posNodoRaiz]
    #print("pos: ", posNodoRaiz)
    print(nodoRaiz)
    # Agregamos nodo raíz
    arbol = Tree(nodoRaiz)
    arbol.inorder_route()



def ABB(vector):
    ingresarDatos(vector)