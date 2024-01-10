
# Para correrlo y graficarlo en un ambiente virtual:
# en la consola :  -m venv env


from borracho import Borracho
from campo import Campo
from coordenada import Coordenada


############################################################################################
def caminata (campo, borracho, pasos) :
############################################################################################
    inicio = campo.obtener_coordenada (borracho)   
    for _ in range (pasos) :
        campo.mover_borracho (borracho)
    
    return inicio.distancia (campo.obtener_coordenada(borracho))


############################################################################################
def simular_caminata (pasos, numero_de_intentos) :
############################################################################################
        
    borracho = Borracho ('David')
    origen = Coordenada (0,0)
    distancias = []

    for _ in range (numero_de_intentos) :
        campo = Campo()
        campo.agregar_borracho (borracho, origen)
        simulacion_caminata = caminata (campo, borracho, pasos)
        distancias.append (round(simulacion_caminata, 1))

    return (distancias)


############################################################################################
def main (distancias_de_caminata, numero_de_intentos) :
############################################################################################
    
    for pasos in distancias_de_caminata :
        distancias = simular_caminata (pasos, numero_de_intentos)
        distancia_media = round (sum(distancias) / len(distancias), 4)      # a 4 decimales
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        print ('Caminata aleatoria de ', pasos)
        print ('Media ', distancia_media)
        print ('Maxima ', distancia_maxima)
        print ('Minima ', distancia_minima)


if __name__ == '__main__' :
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    main (distancias_de_caminata, numero_de_intentos)




