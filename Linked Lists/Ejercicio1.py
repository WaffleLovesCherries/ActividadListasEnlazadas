#1.	Dadas dos listas simples enlazadas ya creadas cuyos inicios 
#son PTR1 y PTR2, hacer un algoritmo que elimine de la lista PTR1 
#los elementos en común entre las dos listas. Nota: No se puede asumir 
#que las listas están ordenadas.

def sin(l1,l2):
    l = []
    for i in l1:
        if l2.count(i) == 0:
            l.append(i)
    return l

PTR1 = [1,1,2,3,4,5,8,10,3]
PTR2 = [1,3,5,2,8]

PTR1 = sin(PTR1,PTR2)

for i in PTR1: print(i)

