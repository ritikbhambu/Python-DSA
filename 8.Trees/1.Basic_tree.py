class Node:
    def __init__(self,data):
        self.data =data
        self.child = [] # in starting no childrens are there so taking a empty list

root = Node(1) # assuming its a root node
child1 = Node(3)        
child2 = Node(4)         # appending all childs inside root child list
child3 = Node(5) 

root.child.append(child1)
root.child.append(child2)
root.child.append(child3)      

print(root.child[0].data)
print(root.child[1].data)
print(root.child[2].data)

