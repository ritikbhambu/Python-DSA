class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)      

#------------------------------------------------------
def preorder(root):
    if root ==None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root ==None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def postorder(root):
    if root ==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

preorder(root)   
print('---')
inorder(root)   
print('---')
postorder(root)   