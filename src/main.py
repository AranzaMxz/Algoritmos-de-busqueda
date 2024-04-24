from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz
#from ABA.busqueda_ABB import busquedaArbol
from ABB.ingresarDatos import ABB
import time

# Genera la matriz y el vector con valores aleatorios
matriz = generarMatriz()
matrizOrd,vector = ordenarMatriz(matriz)

# Solicita el número a buscar
numBuscar = int(input("Ingresa el número a buscar: "))
print("--------- Matriz ---------\n", matrizOrd)
print("--------- Lista ---------\n", vector)

# ABB
#inicio = time.time()
ABB(vector, numBuscar)
#fin = time.time()
#tiempoABB = fin - inicio

#print(f"ABB: {tiempoABB:.4f} segundos")