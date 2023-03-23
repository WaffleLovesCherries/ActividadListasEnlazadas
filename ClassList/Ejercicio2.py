#2.	Hacer un algoritmo que escriba el número total de elementos diferentes 
#en una lista enlazada ya creada. ¿Cuáles son?

from List import List,Node

list = List(list=[1,2,3,4,5,6,1,4,5,6,2,4,5,10])

c = 0
print('Elementos unicos: ')
i = list.first
while i:
    if list.count(i.data) == 1:
        c += 1
        print('- ' + str(i.data))
    i = i.next
print('Total: ' + str(c))