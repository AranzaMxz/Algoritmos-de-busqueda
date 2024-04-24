import random
import math
import numpy as np

# Determina el número de filas y columnas para que el número de elementos sea entre 50-100
def numFilCol():
    x = random.randint(50,100)

    # Calcular número de filas y columnas
    raiz = math.sqrt(x) # Raíz cuadrada de x

    y = random.randint(1,2) # valor que nos determina qué valor se redondea hacia arriba o abajo
    if y == 1:
        nFil = math.ceil(raiz) # redondeo hacia arriba
        mCol = math.floor(raiz) # redondeo hacia abajo
    else:
        nFil = math.floor(raiz) # redondeo hacia abajo
        mCol = math.ceil(raiz) # redondeo hacia arriba
    
    if nFil * mCol < x:
        mCol = mCol + 1 
    #print(x)
    #print(nFil)
    #print(mCol)
    return nFil,mCol

# Verifica que sea un valor único en la matriz
def esUnico(matriz, valor):
    for row in matriz:
        if valor in row:
            return False
    return True

# Genera la matriz con n elementos
def generarMatriz():
    nFil, mCol = numFilCol()

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
    array = np.array(matriz) # Convierte la matriz en array
    array = array.flatten() # Convierte el array en lista
    return matriz, array