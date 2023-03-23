#1.	Dadas dos listas simples enlazadas ya creadas cuyos inicios 
#son PTR1 y PTR2, hacer un algoritmo que elimine de la lista PTR1 
#los elementos en común entre las dos listas. Nota: No se puede asumir 
#que las listas están ordenadas.

from List import List, Node

def sin( l1 : List, l2 : List):
    l : List = List()
    i : Node = l1.first
    while i:
        if l2.count(i.data) == 0:
            l.append(i.data)
        i = i.next
    return l

PTR1 = List(list=[-1,5,-2,2,6,1,-6,-5,-7,0,-3,-7,6,-4,3])
PTR2 = List(list=[-5,7,0,3,1,6,2,-6,-2,5])

PTR1 = sin(PTR1,PTR2)

PTR1.show()