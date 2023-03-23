#5.	Hacer un algoritmo que recorra una lista y regrese dos listas L1 y L2. 
#L1 debe contener los elementos de la lista inicial (sin repetir) y L2 
#debe contener las veces que se repite ese número.

L1 = []
L2 = []

list = [0,2,3,4,5,1,5,6,5,1,5,6]

for i in list:
    if L1.count(i) == 0:
        L1.append(i)
        L2.append(list.count(i))

for i in range(len(L1)): print('Item ' + str(L1[i]) + ': ' + str(L2[i]))