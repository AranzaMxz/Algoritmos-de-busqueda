from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz
#from ABA.busqueda_arbol import busquedaArbol
from busqueda_arbol import ABB

# Genera la matriz y el vector con valores aleatorios
matriz = generarMatriz()
matrizOrd,vector = ordenarMatriz(matriz)

print(matrizOrd)
print("Lista ", vector)

# Solicita el número a buscar
numBuscar = int(input("Ingresa el número a buscar: "))

# ABA
ABB(vector, numBuscar)