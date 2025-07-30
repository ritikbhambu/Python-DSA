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



def  print_range(root,low,high):
    if root is None:
        return
    if low <root.data:
        print_range(root.left,low,high)
    if low <= root.data<=high:
        print(root.data , end =" ")
    if high> root.data:
        print_range(root.right,low,high)



print_range(root,5,15)