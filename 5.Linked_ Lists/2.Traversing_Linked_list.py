class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    def traverse(self):
        curr= Head
        while curr!= None:
            print(curr.data)
            curr = curr.next    

a = Node(1)  
b = Node(2)
c = Node(3)

a.next = b
b.next =c
Head = a
a.traverse()


# When you write:
#   head
# You are referring to the entire node, which consists of two parts:
#   head.data → the value stored in the node
#   head.next → the reference to the next node (or None)
# So yes:
# 🔹 head includes both: data and next

#  When you write: 
#     head.next
# You are now referring to the next node (the one pointed to by head.next).
# And since every node has two parts:
# 🔹 head.next is also a full node, with:
#         head.next.data → value of the next node
#         head.next.next → pointer to the node after that