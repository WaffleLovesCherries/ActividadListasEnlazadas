#2.	Hacer un algoritmo que escriba el número total de elementos diferentes 
#en una lista enlazada ya creada. ¿Cuáles son?

list = [1,2,3,4,5,6,1,4,5,6]

c = 0
print('Elementos unicos: ')
for i in list:
    if list.count(i) == 1:
        c += 1
        print('- ' + str(i))
print('Total: ' + str(c))
        
