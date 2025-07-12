class stackusinglist:
    def __init__(self):
        self.stack = []  # initially the list is empty 

    def push(self,value):
        self.stack.append(value)  # using inbuilt list method
        print(f"appending {value} in the stack")

    def size(self):
        print(len(self.stack))
         
    
    def top(self):
        print(self.stack[-1])
    
    def isempty(self):
        return len(self.stack)==0
    
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty") 
        else:
            self.stack.pop()   
mystack = stackusinglist()
mystack.isempty()
mystack.push(1)                    
mystack.push(2)                    
mystack.push(3)                    
mystack.push(4)                    
mystack.push(5)
mystack.top()
mystack.isempty()
mystack.size()
mystack.pop()
mystack.pop()
mystack.size()                    