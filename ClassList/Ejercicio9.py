#9.	Escribir un algoritmo que verifique si dos listas simples son semejantes.
#Dos listas enlazadas son semejantes si tienen los mismos elementos, 
#no importa el orden. Si un elemento se repite en una lista en la otra debe 
#repetirse igual número de veces.

from List import List,Node

l1 = List(list=[1,3,4,2,1,6,1,5,6])
l2 = List(list=[3,1,5,4,1,6,6,1,2])

t = True
i = l1.first
while i:
    if l1.count(i.data) != l2.count(i.data):
        t = False
        break
    i = i.next

if t:
    print('Son iguales')
else:
    print('No son iguales')