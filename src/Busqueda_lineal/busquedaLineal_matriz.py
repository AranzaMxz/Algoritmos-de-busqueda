indices = []

def busquedaLineal(matriz, valor_busqueda):
    fil = len(matriz)
    col = len(matriz[0])

    for i in range(fil) :
        for j in range(col):
            x = matriz[i][j]
            if x == valor_busqueda: 
                return (i,j)

    return -1        

def BL_matriz(matriz, valor_busqueda):
    resultado = busquedaLineal(matriz, valor_busqueda)
    print(" ___ Matriz ___")
    if resultado != -1:
        print(f"El valor {valor_busqueda} se encuentra en la posición: [{resultado[0]}][{resultado[1]}]")
    else:
        print("El valor no se encuentra en la matriz")