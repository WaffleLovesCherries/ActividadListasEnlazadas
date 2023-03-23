#4.	Hacer un algoritmo que realice las siguientes operaciones a medida que recorre una lista:
#   a.	Si la información del nodo es negativa insertar un nuevo nodo antes de este con igual a -1000
#   b.	Si la información del nodo es positiva insertar un nuevo nodo después de este con información igual a 1000
#   c.	Si la información del nodo es cero eliminarlo.
#   d.	información 
#No se permite recorrer la lista más de una vez.

from List import List,Node

list = List(list=[-1,1,-1,0,1,1,0])

i = 0
while i < list.lenght:
    if list.get(i) < 0:
        list.insert(-1000,i)
        i += 2
    elif list.get(i) == 0:
        list.pop(i)
    else:
        list.insert(1000,i+1)
        i += 2

list.show()