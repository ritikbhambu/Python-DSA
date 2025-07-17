class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)      

#--------------------------------------------------------------------------------
def diameter(root):
    if root ==None:
        return 0,0
    Leftheight,Leftdiameter = diameter(root.left)
    Rightheight,Rightdiameter = diameter(root.right)
    diameter_through_root =Leftheight+Rightheight

    res_diameter = max(Leftdiameter,Rightdiameter,diameter_through_root)
    current_tree_height = 1 + max(Leftheight,Rightheight)
    return res_diameter,current_tree_height

diameter,height = diameter(root)
print(diameter,height)
