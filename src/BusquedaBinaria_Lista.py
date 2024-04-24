import time
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

# Generar y ordenar la matriz
matriz = generarMatriz()
matriz_ord, _ = ordenarMatriz(matriz)

# Convertir la matriz en una lista
Lnumeros = matriz_ord.flatten().tolist()

tam = len(Lnumeros)

print("Lista generada y ordenada:", Lnumeros)

valor_busqueda = int(input("\n\nIngresa el número que quieres buscar en la lista: "))

start_time = time.time()

resultado = busqueda_binaria(Lnumeros, 0, tam - 1, valor_busqueda)

if resultado == -1:
    print("El valor no se encuentra en la lista")
else:
    print(f"El valor {valor_busqueda} se encuentra en la posición {resultado}")

end_time = time.time()

temporizador = end_time - start_time
print(f"Tiempo de ejecución: {temporizador:.6f} segundos")