from generaMatriz import generarMatriz
from ordenaDatos import ordenarMatriz

matriz = generarMatriz()
matrizOrd,vector = ordenarMatriz(matriz)

print(matrizOrd)
print("Lista ", vector)