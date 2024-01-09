
# Estimacion de PI a traves de un metodo estocastico

# importar librerias
import random
import math
from estadisticas import desviacion_estandar, media


###################################################################
def aventar_agujas (numero_agujas) :
###################################################################
    dentro_del_circulo = 0

    for _ in range (numero_agujas) :

        # numeros aleatorios entre -1 y 1
        x = random.random() * random.choice ([-1, 1])
        y = random.random() * random.choice ([-1, 1])
        
        # calcular distancia del centro del circulo hacia el punto generado
        distancia_desde_el_centro = math.sqrt (x**2 + y**2)
        if (distancia_desde_el_centro <= 1) :
            dentro_del_circulo = dentro_del_circulo + 1

    return (4 * dentro_del_circulo) /  numero_agujas



###################################################################
def estimacion (numero_agujas, numero_de_intentos) :
###################################################################

    estimados = []
    for _ in range (numero_de_intentos) :
        porcentaje_agujas_dentro_del_circulo = aventar_agujas (numero_agujas)
        estimados.append (porcentaje_agujas_dentro_del_circulo)
        media_estimados = media (estimados)
        sigma = desviacion_estandar (estimados)
        print ('Media_estimada: ', round (media_estimados, 5), ' Sigma: ', round (sigma, 5), ' Agujas: ', numero_agujas)

    return (media_estimados, sigma)



###################################################################
def estimar_pi (precision, numero_de_intentos, numero_agujas) :
###################################################################

    sigma = precision
    while sigma >= precision / 1.96 :    # para el 99.5% de confiabilidad en una distribucion normal
        media, sigma = estimacion (numero_agujas, numero_de_intentos)
        numero_agujas = numero_agujas * 2

    return (media)



if __name__ == '__main__' :
    estimar_pi (0.002, 300, 1000)     # Al revisar los resultados de las iteraciones es importante notar que sigma va disminuyendo

