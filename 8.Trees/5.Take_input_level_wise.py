from commons import print_tree_detailed,Node
from collections import deque 

def take_input_levelwise():
    data = int(input('enter the root data:'))
    root = Node(data)

    queue = deque([root])
    while len(queue) != 0:
        current_node = queue.popleft()  # pop the left node from queue
        num_children = int(input(f'enter the num of childrens for node {current_node.data} : '))
        for i in range(num_children): # iterate for every child
            child_data= int(input(f'enter data for node {current_node.data} and child {i+1} : '))
            child_node = Node(child_data) # make NOde of data
            current_node.child.append(child_node) # connect node to current_node
            queue.append(child_node) # append the child node to queue so that it can iterate for child node's childrens
    return root

value = take_input_levelwise()
print_tree_detailed(value)        



 
