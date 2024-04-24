from ABB.Tree import Tree

def busquedaABB(arbol, busqueda):
    n = arbol.search(busqueda)
    if n is None:
        print(f"\nEl valor {busqueda} no existe en la lista")
    else:
        print(f"\nEl valor {busqueda} sí existe en la lista")
