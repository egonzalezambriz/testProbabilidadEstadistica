
# Estimacion de PI a traves de un metodo estocastico

import random
import math
from estadisticas import desviacion_estandar, media


###################################################################
def aventar_agujas (numero_de_agujas) :
###################################################################
    dentro_del_circulo = 0

    for _ in range (numero_de_agujas) :
        x = random.random() * random.choice ([-1, 1])
        y = random.random() * random.choice ([-1, 1])
        distancia_desde_el_centro = math.sqrt (x**2 + y**2)

        if (distancia_desde_el_centro <= 1) :
            dentro_del_circulo = dentro_del_circulo + 1

    return (4 * dentro_del_circulo) /  numero_de_agujas



###################################################################
def estimacion (numero_de_agujas, numero_de_intentos) :
###################################################################

    estimados = []
    for _ in range (numero_de_intentos) :
        porcentaje_agujas_dentro_del_circulo = aventar_agujas (numero_de_agujas)
        estimados.append (porcentaje_agujas_dentro_del_circulo)
        media_estimados = media (estimados)
        sigma = desviacion_estandar (estimados)
        print ('Media_estimada: ', round (media_estimados, 5), ' Sigma: ', round (sigma, 5), ' Agujas: ', numero_de_agujas)

    return (media_estimados, sigma)



###################################################################
def estimar_pi (precision, numero_de_intentos) :
###################################################################

    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96 :    # para el 99.5% de confiabilidad en una distribucion normal
        media, sigma = estimacion (numero_de_agujas, numero_de_intentos)
        numero_de_agujas = numero_de_agujas * 2

    return (media)



if __name__ == '__main__' :
    estimar_pi (0.001, 300)     # Al revisar los resultados de las iteraciones es importante notar que sigma va disminuyendo

