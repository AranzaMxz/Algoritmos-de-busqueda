import random
import math
import numpy as np

# Ordena los elementos de la matriz vertical y horizontal
def ordenarMatriz(matriz):
    # Convierte la matriz en un arreglo
    matrizArray = np.array(matriz)
    # Convierte la matriz en una lista y la ordena ascendentemente
    lista = np.sort(matrizArray.flatten())
    # Ordena los elementos de la lista y la regresa a forma de matriz con las dimensiones originales
    matrizOrd = lista.reshape(matrizArray.shape)
    return matrizOrd, lista