#7.	Dadas dos listas enlazadas simples ya creadas (PTR1 y PTR2) ordenadas
#ascendentemente, hacer un algoritmo que cree una tercera lista PTR3 
#ordenada descendentemente con los elementos comunes de las dos listas.

from List import List,Node

PTR1 = List(list=[1,3,5,7,9,10])
PTR2 = List(list=[1,2,4,5,6,6,7,8,9,11])

PTR3 = List()

i = PTR1.first
while i:
    if PTR2.count(i.data) > 0:
        PTR3.append(i.data)
    i = i.next
    
PTR3.reverse()

PTR3.show()
