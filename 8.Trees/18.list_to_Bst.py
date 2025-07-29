class BstNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_Bst(root):
    if root is None:
        return
    print_Bst(root.left)
    print(root.data , end = '')
    print_Bst(root.right)

#------------------------------------
def list_to_BSt(arr):
    if len(arr)==0:
        return None
    middle = len(arr)//2
    data_at_mid = arr[middle]
    mid_node = BstNode(data_at_mid)
    mid_node.left = arr[:middle]
    mid_node.right = arr[middle+1:]    
    return mid_node
            