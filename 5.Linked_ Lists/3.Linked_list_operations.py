class Node:
    def __init__(self,value):
        self.data  = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None 

    def traverse(self):
        curr = self.head
        length = 0
        while curr !=None:
            print( curr.data )   
            curr = curr.next
            length+=1
        print("length =",length)    

    def insert_head(self,value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
    def insert_tail(self,value):
        newnode = Node(value)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = newnode  
ll = Linkedlist()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.traverse()
ll.insert_tail(6)