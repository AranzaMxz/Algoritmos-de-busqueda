import time
from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz

# Algoritmo de la busqueda binaria
def busqueda_binaria(matriz_ord, inicio, fin, valor):
    global fila_menor, columna_menor
    while inicio <= fin:
        medio = (inicio + fin) // 2

        if matriz_ord[medio // len(matriz_ord[0])][medio % len(matriz_ord[0])] == valor:
            fila_menor = medio // len(matriz_ord[0])
            columna_menor = medio % len(matriz_ord[0])
            return medio

        if matriz_ord[medio // len(matriz_ord[0])][medio % len(matriz_ord[0])] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# Generar y ordenar la matriz
matriz = generarMatriz()
matriz_ord, vector = ordenarMatriz(matriz)

# Generar indices de la matriz
num_filas = len(matriz_ord)
num_columnas = len(matriz_ord[0])
fila_menor = 0
columna_menor = 0

print("Matriz generada y ordenada:", matriz_ord)

valor_busqueda = int(input("\n\nIngresa el número que quieres buscar en la matriz: "))

start_time = time.time()

resultado = busqueda_binaria(matriz_ord, 0, num_filas * num_columnas - 1, valor_busqueda)

if resultado == -1:
    print("El valor no se encuentra en la matriz")
else:
    print(f"El valor {valor_busqueda} se encuentra en la posición: [{fila_menor}][{columna_menor}]")

end_time = time.time()

temporizador = end_time - start_time
print(f"Tiempo de ejecución: {temporizador:.6f} segundos")
