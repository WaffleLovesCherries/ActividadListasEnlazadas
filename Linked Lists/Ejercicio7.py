#7.	Dadas dos listas enlazadas simples ya creadas (PTR1 y PTR2) ordenadas
#ascendentemente, hacer un algoritmo que cree una tercera lista PTR3 
#ordenada descendentemente con los elementos comunes de las dos listas.

PTR1 = [1,3,5,7,9,10]
PTR2 = [1,2,4,5,6,6,7,8,9,11]

PTR3 = []

for i in PTR1:
    if PTR2.count(i) > 0:
        PTR3.append(i)
PTR3.reverse()

for i in PTR3: print(i)