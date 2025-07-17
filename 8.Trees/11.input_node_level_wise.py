class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)      
#---------------------------------------------------------------------
from collections import deque
def input_Level_Wise():
    data= int(input('enter root data'))
    if data == -1:
        return None
    root = BinaryTreeNode(data)
    q = deque([root])
    while len(q) != 0:
        curr_node = q.popleft()
        left_children = int(input(f'enter the left child for node {curr_node.data} '))
        if left_children != -1:
            left = BinaryTreeNode(left_children)
            curr_node.left = left
            q.append(left)


        Right_children = int(input(f'enter the Right child for node {curr_node.data} '))
        if Right_children != -1:
            right = BinaryTreeNode(Right_children)
            curr_node.right = right
            q.append(right)
    return root

input_Level_Wise()    