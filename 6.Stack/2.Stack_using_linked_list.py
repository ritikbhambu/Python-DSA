class stack:
    def __init__(self,data):
        self.data = data
        self.next = None

class stackusingll:
    
    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):
        if self.top ==None:
            return "stack is empty"
        return self.top.data  
           
    def push(self,value):  # assume state is top->node1->node2
            newnode = stack(value)  # then will add node 3 and now state is
            self.length+=1          # node3->node1->node2
            if self.top ==None:     # now make node3 as top
                self.top = newnode
                return f" element {value} added in empty stack"

            newnode.next = self.top
            self.top = newnode
            return f"element { value} added to the stack "
    
    def pop(self):
         if self.top ==None:
              return " stack is empty"
         else:
              print(f"element {self.top.data} is deleted")
              self.top = self.top.next   
              self.length -=1

    def is_empty(self):
         return self.top ==None
    
    def lengthofstack(self):
         return self.length    

mystack = stackusingll()
mystack.push(4)          
mystack.push(9)          
mystack.push(2)          
mystack.push(8)          
mystack.peek()
mystack.is_empty() # print its value 
mystack.lengthofstack() # print
mystack.pop()
mystack.pop()
mystack.pop()
mystack.peek()

