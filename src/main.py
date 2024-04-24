from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz
#from ABA.busqueda_ABB import busquedaArbol
from ABB.ingresarDatos import ABB
from Busqueda_binaria.BusquedaBinaria_Lista import BB_Lista
from Busqueda_binaria.BusquedaBinaria_Matriz import BB_Matriz
import time

# Genera la matriz y el vector con valores aleatorios
matriz, array= generarMatriz()
matrizOrd,arrayOrd = ordenarMatriz(matriz)

# Solicita el número a buscar
print("--------- Matriz ordenada ---------\n", matrizOrd)
print("--------- Lista ordenada ---------\n", arrayOrd)
numBuscar = int(input("\nIngresa el número a buscar: "))

#  ------- ABB --------
#inicio = time.time()
ABB(array, numBuscar)
#fin = time.time()
#tiempoABB = fin - inicio

# ------ Busqueda binaria --------
    # Lista
BB_Lista(arrayOrd, 0, len(arrayOrd) - 1, numBuscar) 
    # Matriz
BB_Matriz(matrizOrd, numBuscar)
#print(f"ABB: {tiempoABB:.4f} segundos")