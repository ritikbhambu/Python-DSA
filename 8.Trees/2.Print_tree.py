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
       

def print_tree(root): # not much efficient
    print(root.data)
    for eachnode in root.child:
        print_tree(eachnode)

print_tree(root)      

# def print_tree_detailed(root):
#     if root==None:
#         return
#     print(root.data)
#     for eachnode in root.child:
#         print(eachnode.data)

#     for eachnode in root.child:
#         print_tree_detailed(eachnode)    

# print_tree_detailed(root)     



