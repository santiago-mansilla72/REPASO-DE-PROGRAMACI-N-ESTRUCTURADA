#Escribe un programa que simule una carrera entre dos corredores. Cada corredor avanza un número de 
#metros generado aleatoriamente en cada iteración del ciclo. El programa debe mostrar quién ganó la carrera y en cuántos segundos.
import random
corredor_1 = 0
corredor_2 = 0
c = 0
Meta = False
while Meta != True:
    c += 1
    corredor_1 += random.randint(1, 10)
    print(corredor_1)
    corredor_2 += random.randint(1, 10)
    if corredor_1 >= 100:
        print(f"el corredor 1 llego a la meta en {c} segundos")
        Meta = True
    if corredor_2 >= 100:
        print(f"el corredor 2 llego a la metaen en {c} segundos")
        Meta = True
