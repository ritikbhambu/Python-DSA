
class BstNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = BstNode(10)
root.left = BstNode(5)
root.right = BstNode(15)

root.left.left = BstNode(3)
root.left.right = BstNode(7)

root.right.left = BstNode(12)
root.right.right = BstNode(18)        

#---------------------------


def checkBST_limit(root, minimum, maximum):
    if root is None:
        return True

    if root.data < minimum or root.data > maximum:
        return False

   # the maximum value in a left subtree is less than root
   # the minimum value in right subtree is greater than root
   # it applies to every node which has a subtree 
   # -1 means we doesnt allow duplicates in our tree

    ansLeft = checkBST_limit(root.left, minimum, root.data - 1) # max value on leftsubtree is root.data so check for 1 less than it
    ansRight = checkBST_limit(root.right, root.data + 1, maximum) # min value on right subtree is root.data so check for 1 more than it

    return ansLeft and ansRight

print(checkBST_limit(root,float("-inf"),float("inf")))
