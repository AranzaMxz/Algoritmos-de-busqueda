import timeit

def busquedaLineal(lista, valor_busqueda):
    tam = len(lista)
    for i in range(tam) :
        x = lista[i]
        if x == valor_busqueda: 
            return i
    return -1
            

def BL_Lista(lista, valor_busqueda):
    print("\n________________________________________________________________________")
    print("\n            BUSQUEDA LINEAL         \n")
    print("      Lista     ")
    start_time = timeit.default_timer()
    resultado = busquedaLineal(lista, valor_busqueda)
    end_time = timeit.default_timer()

    if resultado != -1:
        print(f"El valor {valor_busqueda} se encuentra en la posición {resultado}")
    else:
        print(f"El valor {valor_busqueda} no existe en la lista")
    
    temporizador = end_time - start_time
    print(f"Tiempo de ejecución: {temporizador:f} segundos")
