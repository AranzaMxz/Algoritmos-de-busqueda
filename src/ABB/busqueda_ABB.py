from ABB.Tree import Tree

def busquedaABB(arbol, busqueda):
    n = arbol.search(busqueda)
    if n is None:
        print(f"{busqueda} no existe en el vector")
    else:
        print(f"{busqueda} sí existe en el vector")
