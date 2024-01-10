
import random
import collections

PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']


# Se crea una baraja de 52 cartas combinando los palos con los valores 
def crear_baraja () :
    barajas = []
    for palo in PALOS :
        for valor in VALORES :
            barajas.append ( (palo, valor) )

    return barajas


# Se genera una mano de cartas
def obtener_mano (barajas, tamano_mano) :
    mano = random.sample (barajas, tamano_mano)

    return (mano)


# Entrada del programa
def main (tamano_mano, intentos) :
    barajas = crear_baraja ()

    manos = []
    for _ in range (intentos) :
        mano = obtener_mano (barajas, tamano_mano)
        manos.append(mano)

    # Se calculara la probabilidad de obtener un par
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano :
            valores.append(carta[1])    # en el indice 0 se tiene el PALO y en el indice 1 se tiene el VALOR

        counter = dict(collections.Counter(valores))
        # print (counter)
        for val in counter.values () :
            if val == 2 :     # porque deseaos la probabilidad de que nos salga un par
                pares = pares + 1
                break       # porque ya se encontro un par
    
    probabilidad_par = pares / intentos
    print ('La probabilidad de obtener un par en una mano de:', tamano_mano, ' cartas es:', probabilidad_par)




if __name__ == '__main__' :
    tamano_mano = int (input ('De cuantas cartas sera la mano?: ')) 
    intentos = int (input ('Cuantos intentos para calcular la probabilidad?: '))
    main (tamano_mano, intentos)

    

