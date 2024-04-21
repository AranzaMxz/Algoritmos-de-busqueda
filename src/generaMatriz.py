import random
import math
import numpy as np

# Verifica que sea un valor único en la matriz
def esUnico(matriz, valor):
    for row in matriz:
        if valor in row:
            return False
    return True

# Genera la matriz con n elementos
def generarMatriz():
    # Genera un número de filas y columnas entre 2-10 (para máximo 100 elementos)
    nFil = random.randrange(2,10,1)
    mCol = random.randrange(2,10,1)

    matriz = np.zeros((nFil, mCol), dtype = int) # Llenamos la matriz de 0

    # Llenamos la matriz
    for i in range(nFil):
        for j in range(mCol):
            while True:
                valorAl = random.randrange(0,200,1) # Obtenemos un valor aleatorio  
                if esUnico(matriz,valorAl): # Verificamos que no exista en la matriz
                    matriz[i,j] = valorAl
                    break
    #print("fil ", nFil,"| col ", mCol)
    #print(matriz)
    return matriz
