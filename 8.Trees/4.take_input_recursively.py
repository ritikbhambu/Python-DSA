from  commons import print_tree_detailed,Node

def take_input():
    data = int(input("enter the data for node"))
    node= Node(data) # creating a node for the provided data
    numofchildnode = int(input(f'enter the num of childs of {data}'))
    for i in range(numofchildnode):
        child_node = take_input() # take input,numofchildnodes for every child  
        node.child.append(child_node) # make the node as child of root
    return node
res =take_input()
print_tree_detailed(res)