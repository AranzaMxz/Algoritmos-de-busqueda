from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz
from ABB.ingresarDatos import ABB
from Busqueda_binaria.BusquedaBinaria_Lista import BB_Lista
from Busqueda_binaria.BusquedaBinaria_Matriz import BB_Matriz
from Busqueda_lineal.busquedaLineal_Lista import BL_Lista
from Busqueda_lineal.busquedaLineal_matriz import BL_matriz
import time

# Genera la matriz y el vector con valores aleatorios
matriz, array= generarMatriz()
matrizOrd,arrayOrd = ordenarMatriz(matriz)

# Solicita el número a buscar
print("--------- Matriz ordenada ---------\n", matrizOrd)
print("--------- Lista ordenada ---------\n", arrayOrd)
numBuscar = int(input("\nIngresa el número a buscar: "))

# ------- Busqueda lineal -------
    # Lista
BL_Lista(arrayOrd, numBuscar)
BL_matriz(matrizOrd, numBuscar)
# ------ Busqueda binaria --------
    # Lista
BB_Lista(arrayOrd, 0, len(arrayOrd) - 1, numBuscar) 
    # Matriz
BB_Matriz(matrizOrd, numBuscar)

#  ------- ABB --------
ABB(array, numBuscar)



