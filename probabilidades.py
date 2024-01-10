
import random


##########################################################
def tirar_dado (numero_de_tiros) :
##########################################################
    secuencia_de_tiros = []
    for _ in range (numero_de_tiros) :
        tiro = random.choice ([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append (tiro)

    return (secuencia_de_tiros)


##########################################################
def main (numero_de_tiros, numero_de_intentos) :
##########################################################
    tiros = []
    for _ in range (numero_de_intentos) :
        secuencia_de_tiros = tirar_dado (numero_de_tiros)
        tiros.append (secuencia_de_tiros)

    # Probabilidad de tiros con 1
    tiros_con_1 = 0
    for tiro in tiros :
        if 1 in tiro :
            tiros_con_1 = tiros_con_1 + 1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print ('Probabilidad de obtener al menos un 1 en numero de tiros ', numero_de_tiros, ' tiros, es ', probabilidad_tiros_con_1)



if __name__ == '__main__' :
    numero_de_tiros = int (input ('Cuantos tiros del dado: '))
    numero_de_intentos = int (input ('Cuantas veces se realizara la simulacion: '))   # Ayuda a promediar los tiros_con_1 con los intentos

    # numero_de_tiros       numero_de_intentos      resultado corrida      probabilidad de obtener al menos un 1
    # ===============       ==================      ===========            =====================================
    #       1                   10,000              0.1684                    1/6 = 0.16666666
    #       1                   50,000              0.1672                    1/6 = 0.16666666

 # numero_de_tiros       numero_de_intentos      resultado corrida      probabilidad de no obtener al menos un 1
    # ===============       ==================      ===========            =====================================   
    #       10                  10,000              0.8442                    1 - 1/6 = 0.8333333
    main (numero_de_tiros, numero_de_intentos)
