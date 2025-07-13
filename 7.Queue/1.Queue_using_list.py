class queue:
    def __init__(self):
        self.__queue = [] # making it private variable
    
    def sizeofqueue(self):
        return len(self.__queue)
    
    def frontelemnt(self):
        if len(self.__queue)==0:
            return 'queue is empty'
        return self.__queue[0]

    def isempty(self):
        if len(self.__queue) == 0:
            return True
    
    def enqueue(self,value):
        self.__queue.append(value)
        return f" { value} is inserted"
    
    def dequeue(self):
        if len(self.__queue)==0:
            return 'queue is empty'
        print(f"{self.__queue[0]} is deleted")
        self.__queue.pop(0)

q = queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(1)
q.enqueue(8)
q.frontelemnt()
q.sizeofqueue()
q.isempty()
q.dequeue()
q.dequeue()
q.sizeofqueue()
q.frontelemnt()