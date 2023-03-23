#5.	Hacer un algoritmo que recorra una lista y regrese dos listas L1 y L2. 
#L1 debe contener los elementos de la lista inicial (sin repetir) y L2 
#debe contener las veces que se repite ese número.

from List import List,Node

L1 = List()
L2 = List()

list = List(list=[0,2,3,4,5,1,5,6,5,1,5,6])

i = list.first
while i:
    if L1.count(i.data) == 0:
        L1.append(i.data)
        L2.append(list.count(i.data))
    i = i.next

for i in range(L1.lenght): print('Item ' + str(L1.get(i)) + ': ' + str(L2.get(i)))