class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)      

def print_tree(root):
    if root ==None:
        return
    print(root.data,end=': ')
    if root.left != None:
        print(f'L->{root.left.data}',end=', ')
    else:
        print('L->None',end=' ')    
    if root.right != None:
        print(f'R->{root.right.data}' ) 
    else:
        print('R->None')          
    print_tree(root.left)
    print_tree(root.right)   
print_tree(root)      