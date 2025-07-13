class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class Queueusinglinkedlist:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def lenofqueue(self):
        return self.length
    
    def frontitem(self):
        return self.front.data
    
    def is_empty(self):
        return self.length ==0    
    
    def enqueue(self,data):
        newnode = Node(data)
        self.length+=1

        if self.front ==None: # if queue is empty
            self.front = newnode # insert the element and both front and rear will point to it
            self.rear= newnode
        else:
            self.rear.next = newnode # if its not empty then add the element at the node 
            self.rear = newnode    # and make rear point to it

    def dequeue(self) :
        if self.front == None:
            return "queue is empty cant dequeue"   
        self.length -=1
        datatobedeleted = self.front.data
        self.front = self.front.next
        # if there is 1 element in the queue and we delete it then the front will point to none
        # but we have to make rear too point to None otherwise as the front is none the queue will be considered
        # as empty but the tail still point to that deleted node

        if self.front ==None: 
            self.rear = None
        return datatobedeleted    
    
q = Queueusinglinkedlist()

print("Is queue empty?", q.is_empty())         
print("Length of queue:", q.lenofqueue())      

q.enqueue(5)
q.enqueue(8)
q.enqueue(3)
q.enqueue(7)
q.enqueue(9)

print("Dequeued:", q.dequeue())                 
print("Front item:", q.frontitem())             
print("Length of queue:", q.lenofqueue())       
