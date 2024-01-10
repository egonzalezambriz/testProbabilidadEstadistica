
# Para generar numeros aleatorios
import random

# Para obtener la media con funciones de una libreria de Python
import statistics

# Para obtener varianza y desviacion estandar
import numpy as np


# Para obtener raiz quadrada
import math

########################################################################################
# Se obtiene la media de una lista de numeros. Normalmente se utiliza X para una muestra 
def media (X) :
########################################################################################
    return sum(X) / len (X)


########################################################################################
# Se obtiene la varianza de una lista de numeros
def varianza (X) :
########################################################################################
    mu = media (X)

    acum = 0
    for x in X :
        acum = acum + ( x - mu) ** 2
    
    return (acum / len(X))


########################################################################################
# Se obtiene la desviacion estandar
def desviacion_estandar (X) :
########################################################################################
    return math.sqrt (varianza (X))




# Entrada principal al programa
if __name__ == '__main__' :
    X = [random.randint(1,20) for i in range(20)]
    print (X)
    
    # Calculo manual de la media de la poblacion total
    mu = media (X)    
    print ('Media obtenida manualmente: ', mu)

    # Calculo utilizando una funcion estadistica de python
    print ('Media obtenida por funcion estadistica: ', statistics.mean(X))

    # Calculo manual de la varianza y de la desviacion estandar
    Var = varianza (X)
    print ('Varianza obtenida manualmente: ', Var)

    Sigma = desviacion_estandar (X)
    print ('Deviacion estandar obtenida manualmente: ', Sigma)

    # Calculo por funcion de numpy de la varianza  y de la desviacion estandar
    Var = np.var (X)
    print ('Varianza obtenida por funcion de numpy: ', Var)

    Sigma = np.std(X)
    print ('Deviacion estandar obtenida por funcion de numphy: ', Sigma)


