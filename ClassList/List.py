class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class List: 
    def __init__(self, list = None):
        if list:
            self.first = None
            self.lenght = 0
            for i in list:
                self.append(i)

        else:
            self.lenght = 0
            self.first = None


    def append(self, data):
        self.lenght += 1
        if not self.first:
            self.first = Node( data = data )
            return
        node = self.first
        while node.next:
            node = node.next
        node.next = Node( data = data )
    
    def clear(self):
        self.first = None
        self.lenght = 0

    def extend(self, list):
        self.lenght += list.lenght
        if not self.first:
            self.first = list.first
            return
        node = self.first
        while node.next:
            node = node.next
        node.next = list.first
    
    def count(self, data):
        node = self.first
        c = 0
        while node:
            if node.data == data:
                c += 1
            node = node.next
        return c
    
    def index(self, data):
        node = self.first
        c = 0
        while node.next:
            if node.data == data:
                return c
            else:
                c += 1
        return None
    
    def insert(self, data, index):
        if self.lenght <= index:
            self.append( data )
        else:
            self.lenght += 1
            node = self.first
            for i in range(index):
                node = node.next
            node.next = Node( data = node.data, next = node.next )
            node.data = data

    def reverse(self):
        node = self.first
        p = None
        while node:
            next = node.next
            node.next = p
            p = node
            node = next
        self.first = p

    def get(self, index):
        if index == 0:
            return self.first.data
        elif index < self.lenght:
            node = self.first
            for i in range(index):
                node = node.next
            return node.data

    def pop(self, index):
        if index == 0:
            self.first = self.first.next
        elif index > self.lenght - 1:
            return
        elif index == self.lenght - 1:
            node = self.first
            p = None
            while node.next:
                p = node
                node = node.next
            p.next = None
            self.lenght -= 1
        else:
            node = self.first
            p = None
            for i in range(index):
                p = node
                node = node.next
            p.next = node.next
            self.lenght -= 1

    def show( self ):
        node = self.first
        while node:
            print(node.data)
            node = node.next





