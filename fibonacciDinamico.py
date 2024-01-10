
# PROGRAMACION DINAMICA

import sys


# El fibonacci recursivo se comporta bien solo para números pequeños
def fibonacci_recursivo (n) :
    if n == 0 or n == 1 :
        return 1
    
    return fibonacci_recursivo (n - 1) + fibonacci_recursivo (n - 2)




# El fibonacci dinamico se comporta bien aun para numeros grandes
# La idea es guardar resultados parciales en un diccionario para utilizarlos en tiempo O(1) y no recalcular algo ya calculado en 
# llamadas recursivas previas, ahorrando tiempo de calculo
def fibonacci_dinamico (n, memoria={}) :
    if n == 0 or n == 1 :
        return 1

    try :
        return memoria[n] 

    except KeyError :
        resultado = fibonacci_dinamico (n - 1, memoria) + fibonacci_dinamico (n - 2, memoria)
        memoria [n] = resultado
        return memoria[n] 




if __name__ == '__main__' :                 # Para definir el punto de entrada
    sys.setrecursionlimit = 10000           # Para evitar error por un limite bajo de recursiones

    n = int (input ('Escoge un numero entero: '))
    res = fibonacci_dinamico (n)
    print ('resultado', res)


