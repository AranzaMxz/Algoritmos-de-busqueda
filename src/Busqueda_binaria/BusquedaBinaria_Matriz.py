import timeit
from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz

fila_menor = 0
columna_menor = 0

# Algoritmo de la busqueda binaria
def busqueda_binaria(matriz, inicio, fin, valor):
    global fila_menor, columna_menor
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if matriz[medio // len(matriz[0])][medio % len(matriz[0])] == valor:
            fila_menor = medio // len(matriz[0])
            columna_menor = medio % len(matriz[0])
            return medio

        if matriz[medio // len(matriz[0])][medio % len(matriz[0])] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

def BB_Matriz(matriz, valor_busqueda):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    print("\n     Matriz     ")
    start_time = timeit.default_timer()
    resultado = busqueda_binaria(matriz, 0, num_filas * num_columnas - 1, valor_busqueda)
    end_time = timeit.default_timer()

    if resultado == -1:
        print("El valor no se encuentra en la matriz")
    else:
        print(f"El valor {valor_busqueda} se encuentra en la posición: [{fila_menor}][{columna_menor}]")

    temporizador = end_time - start_time
    print(f"Tiempo de ejecución: {temporizador:f} segundos")
