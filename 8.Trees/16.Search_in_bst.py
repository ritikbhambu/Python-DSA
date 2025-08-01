class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = BST(6)
node2 = BST(4)
node3 = BST(7)
node4 = BST(2)
node5 = BST(5)
node6 = BST(8)
node7 = BST(9)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.right = node7
node3.left = node6

#---------------------

def search_bst(root,value):
    if root ==None:
        return
    
    if root.data ==value:
        print('data found')
        return
    if value<root.data:
        search_bst(root.left,value)
    elif value > root.data:
        search_bst(root.right,value)

search_bst(root,5)