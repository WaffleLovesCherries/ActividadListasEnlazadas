#4.	Hacer un algoritmo que realice las siguientes operaciones a medida que recorre una lista:
#   a.	Si la información del nodo es negativa insertar un nuevo nodo antes de este con igual a -1000
#   b.	Si la información del nodo es positiva insertar un nuevo nodo después de este con información igual a 1000
#   c.	Si la información del nodo es cero eliminarlo.
#   d.	información 
#No se permite recorrer la lista más de una vez.

list = [-1,1,-1,0,1,1,0]

i = 0
while i < len(list):
    if list[i] < 0:
        list.insert(i,-1000)
        i += 2
    elif list[i] == 0:
        list.pop(i)
    else:
        list.insert(i+1,1000)
        i += 2

for i in list: print(i)