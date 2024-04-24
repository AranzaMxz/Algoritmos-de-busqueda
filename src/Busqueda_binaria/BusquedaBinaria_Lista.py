import timeit
from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz

# Algoritmo de la busqueda binaria
def busqueda_binaria(lista, inicio, fin, valor):
    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == valor:
            return medio

        if lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

def BB_Lista(array, inicio, fin, valor_busqueda):
    print("________________________________________________________________________")
    print("\n         BUSQUEDA BINARIA         \n")
    print("     Lista     ")
    start_time = timeit.default_timer()
    resultado = busqueda_binaria(array, inicio, fin, valor_busqueda)
    end_time = timeit.default_timer()

    if resultado == -1:
        print("El valor no se encuentra en la lista")
    else:
        print(f"El valor {valor_busqueda} se encuentra en la posición {resultado}")

    temporizador = end_time - start_time
    print(f"Tiempo de ejecución: {temporizador:e} segundos")
