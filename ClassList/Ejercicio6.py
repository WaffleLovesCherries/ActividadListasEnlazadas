#6.	Dada una lista enlazada simple ya creada, hacer un algoritmo que vaya 
#formando dos listas (PTR1 y PTR2) con los mismos nodos de la lista inicial
#de tal forma que en la lista PTR1 vayan quedando todos los elementos 
#positivos, y en la lista PTR2 todos los elementos negativos. 
#Si hay nodos que tengan como información el 0 se eliminan.

from List import List,Node

PTR1 = List()
PTR2 = List()

list = List(list=[1,-3,4,1,0,5,6,-1,-3,-5,7,-2])

i = list.first
while i:
    if i.data > 0:
        PTR1.append(i.data)
    elif i.data < 0:
        PTR2.append(i.data)
    i = i.next

PTR1.show()
PTR2.show()