class Node:
    def __init__(self,data):
        self.data =data
        self.child = [] # in starting no childrens are there so taking a empty list

root = Node(1) # assuming its a root node
child1 = Node(3)        
child2 = Node(4)         # appending all childs inside root child list
child3 = Node(5) 

root.child.append(child1)
root.child.append(child3)
child1.child.append(child2)

# ----------------------------------------------------------------------


def preorder_traversal(root):  # ( N,L,R)
    if root == None:
        return
    print(root.data)
    for eachchild in root.child:
        preorder_traversal(eachchild)

def postorder_traversal(root): # ( L,R,N)
    if root ==None:
        return
    for eachchild in root.child:
        preorder_traversal(eachchild)
    print(root.data)
    
preorder_traversal(root)   
print()
postorder_traversal(root)     