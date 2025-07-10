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
        print('start')
        while curr !=None:
            print( curr.data )   
            curr = curr.next
            length+=1
        print('end')    
        print("length =",length)  



    def insert_head(self,value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode


    def insert_tail(self,value):
        length = 0
        newnode = Node(value)
        if self.head ==None:
            self.head = newnode
        curr = self.head
        while curr.next != None:
            curr = curr.next
            length +=1
        curr.next = newnode  
        print('length is',length +1)



    def insert_at_index(self,value,index):
        newnode = Node(value)
        curr = self.head
        count = 0
        while curr!= None and count <index-1:
            count+=1
            curr = curr.next
        if curr is None:
            print("Index out of bounds")
            return    
        newnode.next = curr.next # its possible that loop never finds the value and current just stops before none
        curr.next = newnode


    
    
    def after_value(self,value,afterdata):
        newnode = Node(value) 
        curr = self.head
        while curr!= None:
            if curr.data ==afterdata:
                break
            curr = curr.next
            if curr!= None:
                newnode.next = curr.next
                curr.next = newnode



    def delete_head(self):
        if self.head==None:
            print('empty list')
            return
        self.head = self.head.next


    def delete_tail(self):
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None: # when we have to insert data ,we just stop on that node
            curr = curr.next          # when we have to delete data we stop before that node
        curr.next= None   


    def delete_index(self,index):
        if self.head ==None:
            return
        if index == 0:
            return self.delete_head
        curr = self.head
        count =0
        while curr.next!= None and count<index-1:
            curr = curr.next
            count+=1
        if curr.next == None:
            return 'not found'
        else:
            curr.next  = curr.next.next   


    def delete_specific_node(self,value):  
        if self.head ==None:
            return
        if self.head.data ==value:
            return self.delete_head()
        curr = self.head
        while curr.next!= None:
            if curr.next.data == value:
                break
            curr = curr.next
             
        if curr.next == None:
            return 'not found'
        else:
            curr.next  = curr.next.next 
                 
    def search_by_val(self,value):
        pos = 0
        curr = self.head
        while curr!= None:
            if curr.data ==value:
                print('node found at',pos)
                return pos
            curr =curr.next
            pos+=1
        return 'Not found'    
    
    def search_by_index(self,index):
        pos = 0
        curr = self.head
        while curr!= None :
            if pos==index:
                return curr.data
            curr =curr.next
            pos+=1
        return 'Not found'    

    def midofll(self):
        if self.head ==None:
            return 'empty'
        curr = self.head
        counter = 0
        while curr!=None:
            counter+=1
            curr = curr.next
        mid = counter//2
        newcount = 0
        curr = self.head
        while curr != None:
            if newcount ==mid:
                print("data at mid",curr.data)
            newcount+=1
            curr = curr.next       
                
        
ll = Linkedlist()

# ll.insert_head(1)
# ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
# ll.insert_tail(6)
# ll.insert_at_index(7,4) #(7,300)
# ll.after_value(9,3)

# ll.traverse()

# ll.delete_head()
# ll.delete_tail()
# ll.delete_index(2)
# ll.delete_specific_node(7)

ll.search_by_val(3)
print(ll.search_by_index(1))

ll.midofll()
ll.traverse()
