import timeit

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
    print("\n     Matriz      ")
    start_time = timeit.default_timer()
    resultado = busquedaLineal(matriz, valor_busqueda)
    end_time = timeit.default_timer()

    if resultado != -1:
        print(f"El valor {valor_busqueda} se encuentra en la posición: [{resultado[0]}][{resultado[1]}]")
    else:
        print("El valor no se encuentra en la matriz")
    
    temporizador = end_time - start_time
    print(f"Tiempo de ejecución: {temporizador:f} segundos")