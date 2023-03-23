#9.	Escribir un algoritmo que verifique si dos listas simples son semejantes.
#Dos listas enlazadas son semejantes si tienen los mismos elementos, 
#no importa el orden. Si un elemento se repite en una lista en la otra debe 
#repetirse igual número de veces.

l1 = [1,3,4,2,1,6,1,5,6]
l2 = [3,1,5,4,1,6,6,1,2]

t = True
for i in l1:
    if l1.count(i) != l2.count(i):
        t = False
        break

if t:
    print('Son iguales')
else:
    print('No son iguales')