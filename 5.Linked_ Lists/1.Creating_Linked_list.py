class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

a = Node(1)  
b = Node(2)
c = Node(3)

print('value of node a' , a.data)
print('value of node b' , b.data)      
print('value of node c' , c.data)      

a.next = b
b.next =c
print('current list: a->b->c->None')

print('value at the next node of a :', a.next.data)
print('value at the next node of b :',b.next.data)

Head = a
print(Head.data)  # value of first node
print(Head.next)  # address of second node
print(Head.next.data) # value of second node
print(Head.next.next.data) # value of third node

